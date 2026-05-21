FROM python:3.12-slim

WORKDIR /app

COPY app.py .
COPY version.txt .

CMD [ "python3", "app.py" ]