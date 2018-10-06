# Laureategram
Instagram wannabe, based on https://github.com/pablotrinidad/platzigram. This fork enables compatibility with Google Cloud Platform (https://console.cloud.google.com). Google App Engine for hosting, Google Cloud SQL (PostgreSQL)for the DB and Google Cloud Storage to store static files and Posts Media. 


### Installation
Run the following commands:

    $ git clone git@github.com:oespirilla/laureategram.git
    
    $ cd laureategram
    
    $ python3 -m venv <ENV_NAME>
    
    # Activate enviroment (POSIX)
    $ source <ENV_NAME>/bin/activate
    # Activate enviroment (Windows)
    > \path\to\env\Scripts\activate
    
    # Installing dependencies
    (ENV)$ pip install -r requirements.txt

    # Running  migrations
	(ENV)$ python manage.py migrate
	
	# Creating a Django Admin user
	(ENV)$ python manage.py createsuperuser

	# Running an WSGI local instance
    (ENV)$ python manage.py runserver 0.0.0.0:8000

The site will now be accessible at [http://localhost:8000/](http://localhost:8000/) and the admin interface at [http://localhost:8000/admin/](http://localhost:8000/admin/) . 

### Deployment to GAE (Google App Engine)
In order to deploy this app to GAE you need to setup:
- [Install Google Cloud SDK](https://cloud.google.com/sdk/docs/)

- [Google App Engine Standard Environment for Python 3.7](https://cloud.google.com/appengine/docs/standard/python3/quickstart)

- [Google Cloud SQL for PostgreSQL](https://cloud.google.com/sql/docs/postgres/quickstart)

- [Google Cloud Storage](https://cloud.google.com/storage/docs/quickstart-gsutil)


Then you you need to create an app.yaml file based on app.template.yaml


.........



