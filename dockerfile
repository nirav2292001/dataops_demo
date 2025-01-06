FROM python:3.9-slim

WORKDIR /app

COPY automate_eda.py /app
COPY SampleSuperstore.csv /app  

RUN pip install --no-cache-dir pandas numpy pandas-profiling

CMD ["python", "automate_eda.py"]
