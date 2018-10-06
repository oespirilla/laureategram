# run this to set the environment variables in your local machine, 
# needed to debug from localhost to Google Cloud


export DEBUG='True' # "converted" to boolean in settings.py line 5
export SECRET_KEY='' # TODO: enter your Django secret key here
export DB_HOST='' # home IP for connecting to the sql proxy connection with the Google Cloud database instance
export DB_NAME='' # TODO: add the database name [instance id] (the database instance name from Google Cloud -> SQL)
export DB_USER='' # TODO: add the instance username (default is postgres if you did not make a custom one)
export DB_PASSWORD='' # TODO: add the instance password (default is the generated password associated with 'postgres')
export STATIC_URL='/static/' # the name of your static (development) directory
export GS_BUCKET_NAME=''# the name of your google cloud storage bucket 