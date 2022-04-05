FROM python:3.10-alpine3.15

#Since the concern is commits on (.py) files then moving both samples and requirements to the upper layers of the docker file
#Will help a great deal in utilizing the cache of docker
COPY samples /data

COPY requirements.txt /app/

RUN pip install -r app/requirements.txt

COPY src /app

WORKDIR /app
EXPOSE 8080
ENTRYPOINT [ "python3" ]
CMD [ "__init__.py", "/data","0.0.0.0" ]