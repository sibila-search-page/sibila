#! /bin/bash

# Load  superclass
cd /app



cd /app

ps -ef | grep gunic | grep -v grep | awk '{ print $2 }' | xargs kill -9 ;
if [ `echo $HOSTNAME | grep -i -e virtualbox -e mac` ]
then
  conda activate python36
  gunicorn  -b 0.0.0.0:5000  -w 3  app:app   --timeout 45 --log-level=debug
else
  scl  enable rh-python36 " gunicorn  -b 0.0.0.0:5000  -w 3  app:app   --timeout 45 --log-level=debug"
fi
