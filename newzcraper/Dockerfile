FROM python:3.7.10-alpine3.13
RUN apk add \
    nmap \
    gcc \
    musl-dev \
    python3-dev \
    libffi-dev \
    openssl-dev \
    libxml2-dev \
    libxslt-dev \
    cargo


COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
ENTRYPOINT ["python3"]
CMD ["src/main.py"]