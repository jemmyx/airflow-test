


Création et démarrage de l'environnement virtuel
```
Python -m venv airflow-env
source ./airflow-env/Scripts/activate
```

Airflow installation
```
Installer le package airflow (sqlalchemy, etc.)
```

Airflow démarrage
```
airflow standalone
```

Si besoin éditer le chemin absolut dans la config Airflow
```
vi /c/Users/<user>/airflow/airflow.cfg
```
 
Eteindre l'environnement virtuel
```
deactivate
```

Démarrer le schedule

```
docker exec -it airflow sh
airflow scheduler
```


Docker

```
docker build -t airflow-fm1 .
```

```
docker run -d -p 8080:8080   -v /C:/Users/<user>/Documents/toSharedDrive/ephemeral/dev/python/airflow-docker:/opt/airflow/dags  -e AIRFLOW_UID=$(id -u)     -e AIRFLOW_GID=0     -e _AIRFLOW_DB_UPGRADE=true     -e _AIRFLOW_WWW_USER_CREATE=true     -e _AIRFLOW_WWW_USER_USERNAME=admin     -e _AIRFLOW_WWW_USER_PASSWORD=admin     --name airflow airflow-fm1 webserver
```