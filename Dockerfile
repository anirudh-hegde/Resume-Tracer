
FROM python:3.8-slim

RUN apt-get update

RUN adduser --disabled-password --gecos "" thanos
WORKDIR /app
COPY goat.py .
COPY requirements.txt .
RUN pip install -r requirements.txt


USER thanos

CMD ["streamlit", "run", "goat.py"]