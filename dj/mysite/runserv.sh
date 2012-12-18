#!/bin/bash
IP=`./getMyIP.sh`
python manage.py runserver $IP:8080
