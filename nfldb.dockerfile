FROM postgres:9.6-alpine

RUN apk add --update python\
    python-dev \
    py-pip 

EXPOSE 5432
CMD ["bash"]