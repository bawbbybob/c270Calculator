FROM python:3.10-slim

WORKDIR /app

# Copy requirements first for better caching
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy all project files (app.py, calculator.py, templates, static, etc.)
COPY . .

# Expose the port your Flask app uses
EXPOSE 8080

# Start the application
CMD ["python3", "app.py"]
