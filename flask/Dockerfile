FROM python:3.7.10-alpine3.13

COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
ENTRYPOINT ["python3"]
CMD ["src/server.py"]