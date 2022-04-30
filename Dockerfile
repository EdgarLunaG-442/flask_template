FROM public.ecr.aws/docker/library/alpine:3.14

RUN apk add py3-pip \
    && pip install --upgrade pip

COPY . .

RUN pip install -r requirements.txt

EXPOSE 5000

CMD ["gunicorn","-c", "gunicorn.conf.py"]