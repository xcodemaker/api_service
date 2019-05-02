FROM python:3.6.6-alpine3.6
ENV PYTHONUNBUFFERED 1
WORKDIR /server
COPY ./requirements.txt /server
RUN apk --update add python py-pip openssl ca-certificates py-openssl wget
RUN apk --update add --virtual build-dependencies libffi-dev openssl-dev python-dev py-pip build-base \
  && pip install --upgrade pip \
  && pip install -r requirements.txt \
  && apk del build-dependencies
COPY ./api_service /server
EXPOSE 8888
ENTRYPOINT [ "python", "manage.py" ]
CMD [ "runserver", \
      "0.0.0.0:8888" ]
