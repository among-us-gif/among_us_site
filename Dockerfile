FROM tiangolo/uwsgi-nginx-flask:python3.8

LABEL maintainer="david.dellsperger@gmail.com"

ENV STATIC_URL /gif
ENV STATIC_PATH /app/gif

COPY ./requirements.txt /build/requirements.txt
COPY lib/ /build/lib
WORKDIR /build
RUN pip install -r requirements.txt

VOLUME /app/gif

COPY ./app /app