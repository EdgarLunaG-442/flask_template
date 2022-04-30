FROM public.ecr.aws/docker/library/python:3.9.12-buster

COPY . .

RUN pip install -r requirements.txt

EXPOSE 5000

CMD ["gunicorn","-c", "gunicorn.conf.py"]