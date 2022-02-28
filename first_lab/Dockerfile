FROM fedora:latest
LABEL version="1.0"
RUN mkdir ISP
WORKDIR /home
COPY first_lab.py /home/ISP/first_lab_ISP.py
ENV PERSON_NAME="Matuamod"
ENTRYPOINT ["/usr/bin/python3", "/home/ISP/first_lab_ISP.py"]
