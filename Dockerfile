FROM python
WORKDIR /tmp
RUN pip3 install requests
COPY pgreeter.py /tmp/.
RUN chmod +x /tmp/pgreeter.py
CMD [ "/tmp/pgreeter.py"]
