FROM public.ecr.aws/docker/library/alpine:3.14

COPY . .

RUN pip install -r requirements.txt

EXPOSE 5000

CMD ["gunicorn","-c", "gunicorn.conf.py"]