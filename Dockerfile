FROM python:3.11
WORKDIR /usr/local/app


COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .
