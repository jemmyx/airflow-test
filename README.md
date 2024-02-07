![image](https://github.com/jemmyx/airflow-test/assets/595853/56257891-33ee-42db-abe4-7aa73302d08a)


# Config Python locale

## Environnement virtuel
```
Python -m venv airflow-env
source ./airflow-env/Scripts/activate
```

### Installation d'Airflow
```
Installer le package airflow (sqlalchemy, etc.)
```

### Démarrage
```
airflow standalone
```

(Optional) Editer le chemin absolut dans la config Airflow
```
vi /c/Users/<user>/airflow/airflow.cfg
```

Eteindre l'environnement virtuel
```
deactivate
```


# Docker execution

## Setup the container
```
docker build -t airflow-fm1 .
```

```
docker run -d -p 8080:8080   -v /C:/Users/meyer/Documents/toSharedDrive/ephemeral/dev/python/airflow-docker:/opt/airflow/dags  -e AIRFLOW_UID=$(id -u)     -e AIRFLOW_GID=0     -e _AIRFLOW_DB_UPGRADE=true     -e _AIRFLOW_WWW_USER_CREATE=true     -e _AIRFLOW_WWW_USER_USERNAME=admin     -e _AIRFLOW_WWW_USER_PASSWORD=admin     --name airflow airflow-fm1 webserver
```

## Run the scheduler
```
docker stop airflow
docker container rm airflow
```

## Install the dependancy (pdf parsing)
```
pip install --upgrade pip
pip install pdfplumber
```
