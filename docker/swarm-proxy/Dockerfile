FROM python:2.7-alpine

RUN apk add --update \
    ca-certificates \
  && rm -rf /var/cache/apk/*

WORKDIR /opt/app

ADD src/requirements.txt .
RUN pip install -r ./requirements.txt

ADD src .
RUN chmod +x *.py

CMD ["./server.py"]
