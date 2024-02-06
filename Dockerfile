FROM apache/airflow:latest

# user / group Airflow
ARG AIRFLOW_UID=1000
ARG AIRFLOW_GID=0

# general config
ENV AIRFLOW_UID=${AIRFLOW_UID}
ENV AIRFLOW_GID=${AIRFLOW_GID}
ENV _AIRFLOW_DB_UPGRADE=true
ENV _AIRFLOW_WWW_USER_CREATE=true
ENV _AIRFLOW_WWW_USER_USERNAME=admin
ENV _AIRFLOW_WWW_USER_PASSWORD=admin

USER root

RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        poppler-utils \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

RUN pip install pdfplumber

USER airflow

# for info
VOLUME ["/opt/airflow/dags"]

# web interface
EXPOSE 8080

CMD ["airflow", "webserver"]
