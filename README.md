


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
vi /c/Users/meyer/airflow/airflow.cfg
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


