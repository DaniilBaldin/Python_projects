FROM alpine:3.13

RUN apk update
RUN apk add --update python3-dev py3-pip postgresql-dev gcc musl-dev

WORKDIR /opt/blog_ui

COPY requirements.txt ./

RUN python3 -m pip install -r requirements.txt

COPY . ./

EXPOSE 9001

ENTRYPOINT ["python3", "manage.py"]

CMD ["runserver", "0.0.0.0:9001"]
