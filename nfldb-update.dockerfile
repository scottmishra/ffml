FROM python:2.7.13-alpine3.6
RUN pip install -r nfldb
ENTRYPOINT ["nfldb-update","bash"]