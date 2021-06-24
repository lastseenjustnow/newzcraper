FROM python:3.7-alpine
RUN apk add nmap


COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
ENTRYPOINT ["python3"]
CMD ["main.py"]