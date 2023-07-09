FROM alpine
ADD https://bootstrap.pypa.io/get-pip.py requirements.txt main.py /opt/
RUN apk update && apk add python3 && \
    /usr/bin/python3 /opt/get-pip.py && \
    /usr/bin/pip3 install -r /opt/requirements.txt
CMD ["/usr/bin/python3", "/opt/main.py"]
