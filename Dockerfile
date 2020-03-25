FROM ubuntu:18.04

COPY script/before_install.sh /home
COPY script/installation.sh /home

COPY app.py /home

RUN chmod 775 home/before_install.sh
RUN chmod 775 home/installation.sh

RUN home/before_install.sh
RUN home/installation.sh

RUN chmod 775 home/app.py
RUN python3 home/app.py