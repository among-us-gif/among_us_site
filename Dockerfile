FROM tiangolo/uwsgi-nginx-flask:python3.12

LABEL maintainer="david.dellsperger@gmail.com"
LABEL org.opencontainers.image.source="https://github.com/among-us-gif/among_us_site"

ENV STATIC_URL /static
ENV STATIC_PATH /app/static

COPY ./requirements.txt /build/requirements.txt
COPY lib/ /build/lib
WORKDIR /build
RUN pip install -r requirements.txt

WORKDIR /app
VOLUME /app/gifs

COPY ./app /app
