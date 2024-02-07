from datetime import datetime
from airflow import DAG
from airflow.operators.python_operator import PythonOperator
# from some_nlp_library import extract_text_from_pdf, analyze_contract

default_args = {
    'owner': 'airflow',
    'start_date': datetime(2024, 1, 1),
    'retries': 1,
}

def extract_text_from_pdf(pdf_path):
    # Ouvrir le fichier PDF
    with pdfplumber.open(pdf_path) as pdf:
        # Concaténer le texte de chaque page
        text = ''.join(page.extract_text() for page in pdf.pages if page.extract_text())
    return text

def process_pdf_contract(**kwargs):
    pdf_path = kwargs.get('pdf_path', '/opt/airflow/data/assurances-maladie-complementaires.pdf')

    
    # text extraction
    text = extract_text_from_pdf(pdf_path)
    
    # text analysis part...
    # analysis_results = analyze_contract(text)
    
    # additional steps to do...
    # ...

with DAG('contract_analysis_dag',
         default_args=default_args,
         description='DAG for anaalysis of contract w/LLM',
         schedule_interval='@daily',
         catchup=False) as dag:

    process_contract_task = PythonOperator(
        task_id='process_pdf_contract',
        python_callable=process_pdf_contract,
        op_kwargs={'pdf_path': '/opt/airflow/data/assurances-maladie-complementaires.pdf'},
    )

process_contract_task
