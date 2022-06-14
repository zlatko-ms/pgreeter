FROM python
WORKDIR /tmp
RUN pip3 install requests
COPY pgreeter.py /tmp/.
CMD [ "python /tmp/pgreeter.py"]
