FROM alpine:3.13

RUN apk update
RUN apk add --update python3-dev py3-pip postgresql-dev gcc musl-dev

WORKDIR /opt/django_blog

COPY requirements.txt ./

RUN python3 -m pip install -r requirements.txt

Copy . ./

EXPOSE 8000

ENTRYPOINT ["python3", "manage.py"]

CMD ["runserver", "127.0.0.1:8000"]
