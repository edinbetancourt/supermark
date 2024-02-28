FROM python:3.12.2-slim-bullseye
WORKDIR /app
COPY . /app
ENV PYTHONUNBUFFERED=1
RUN apt-get update
RUN apt-get -y upgrade
RUN apt-get -y install nginx
COPY default /etc/nginx/sites-available/
RUN pip3 install -r requirements.txt
EXPOSE 80
EXPOSE 8000
CMD ["sh", "runserver.sh"]
