# https://docs.docker.com/compose/django/#create-a-django-project
# run using :
# sudo docker build -t rahjoo_server_docker .
# sudo docker run -itd -p 18000:8000 -v ~/rahjoo_server/db.sqlite3:/root/code/db.sqlite3 rahjoo_server_docker
FROM python:3
ENV PYTHONUNBUFFERED 1
RUN mkdir /root/code
WORKDIR /root/code
ADD . /root/code/
RUN pip install -r requirements.txt
EXPOSE 8000
CMD ["python3","manage.py", "compilemessages"]
CMD ["python3","manage.py", "runserver","0.0.0.0:8000"]