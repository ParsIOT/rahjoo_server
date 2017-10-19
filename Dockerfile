# https://docs.docker.com/compose/django/#create-a-django-project
FROM python:3
ENV PYTHONUNBUFFERED 1
RUN mkdir /root/code
WORKDIR /root/code
ADD . /root/code/
RUN pip install -r requirements.txt
EXPOSE 8000
CMD ["python3","manage.py", "runserver","0.0.0.0:8000"]