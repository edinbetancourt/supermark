#!/bin/sh
service nginx start
gunicorn -w 4 -b 0.0.0.0 project.wsgi
