from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.operators.empty import EmptyOperator
from datetime import datetime
from pymongo import MongoClient
from airflow.models import Variable
from airflow.hooks.base import BaseHook
import os
import json


conn = BaseHook.get_connection("mongo_pi")

MONGO_USER = conn.login       # usuário
MONGO_PASSWORD = conn.password  # senha
DB_NAME = conn.schema         # banco
HOST = conn.host              # host
PORT = conn.port  
COLLECTION_NAME = "api" 

MONGO_URI = f"mongodb+srv://{MONGO_USER}:{MONGO_PASSWORD}@{HOST}/{DB_NAME}?retryWrites=true&w=majority"

LOCAL_FILE = "/opt/airflow/dags/data/arquivo.txt"

default_args = {
    "start_date": datetime(2023, 1, 1),
}

def extrair_dados_arduino():
    if not os.path.exists(LOCAL_FILE):
        print(f"Arquivo {LOCAL_FILE} não encontrado!")
        return

    json_docs = []

    with open(LOCAL_FILE, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            try:
                json_docs.append(json.loads(line))
            except json.JSONDecodeError as e:
                print("Linha inválida, ignorando:", line, e)

    print(f"{len(json_docs)} JSONs carregados com sucesso")

    if not json_docs:
        print("Nenhum JSON válido para inserir")
        return


    client = MongoClient(MONGO_URI)
    db = client[DB_NAME]
    collection = db[COLLECTION_NAME]

    collection.insert_many(json_docs)
    print(f"{len(json_docs)} documentos inseridos no MongoDB")

with DAG(
    "pipeline_pi",
    default_args=default_args,
    schedule=None,
    catchup=False,
    tags=["projeto", "pi", "arduino"],
) as dag:

    task_send_txt = PythonOperator(
        task_id="extrair_dados_arduino",
        python_callable=extrair_dados_arduino
    )

    task_dummy = EmptyOperator(task_id="final_task")

    task_send_txt >> task_dummy
