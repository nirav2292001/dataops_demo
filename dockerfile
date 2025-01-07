
FROM python:3.10-slim

WORKDIR /app

# Copy the application and .env file to the container
COPY . .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Run the application
CMD ["python", "automate_eda.py"]

