FROM python:2.7.13-alpine3.6

RUN apk update && \
    apk add --virtual build-deps gcc python-dev musl-dev && \
    apk add postgresql-dev \
    bash 

COPY ./config.ini config.ini
RUN pip install nfldb
RUN cp config.ini /usr/local/share/nfldb/
## Need to copy the config.ini into the proper directory
CMD ["nfldb-update"]