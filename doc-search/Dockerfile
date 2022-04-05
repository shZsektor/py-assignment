FROM python:3.10-slim-bullseye
COPY samples /data

COPY requirements.txt /app/

RUN pip install -r app/requirements.txt

COPY src /app

WORKDIR /app
EXPOSE 8080
ENTRYPOINT [ "python3" ]
CMD [ "__init__.py", "/data" ]