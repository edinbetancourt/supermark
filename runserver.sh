#!/bin/sh
service nginx start
gunicorn project.wsgi
