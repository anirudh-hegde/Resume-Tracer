FROM python:3-alpine
WORKDIR /app
COPY goat.py .
COPY requirements.txt .
RUN pip install -r requirements.txt
CMD ["streamlit", "run" ,"goat.py"]