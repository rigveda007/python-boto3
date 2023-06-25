FROM ubuntu

MAINTAINER Bodhisatwya

WORKDIR /var/www/html

RUN apt-get update && \
    apt-get install nginx vim git -y

COPY indexfile.txt ${WORKDIR}

