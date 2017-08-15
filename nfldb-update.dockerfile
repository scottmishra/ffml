FROM python:2.7.13-alpine3.6
COPY ./config.ini config.ini
RUN pip install virtualenv
RUN mkdir ~/.virtual
RUN virtualenv ~/.virtual/nflapi
RUN source ~/.virtual/nflapi/bin/activate
RUN pip install -r nfldb
## Need to copy the config.ini into the proper directory
RUN cp config.ini ~/.virtual/nflapi/share/nfldb
ENTRYPOINT ["nfldb-update","bash"]