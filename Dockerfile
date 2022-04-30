FROM public.ecr.aws/docker/library/python:3.9.12-buster

RUN pip3 install -r requirements.txt

EXPOSE 5000

CMD ["gunicorn","-c", "gunicorn.conf.py"]