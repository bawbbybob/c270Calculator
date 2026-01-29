FROM python:3.10-slim

WORKDIR /app

# Copy all project files (app.py, calculator.py, templates, static, etc.)
COPY . .

# Install Flask
RUN pip install flask

# Expose the port your Flask app uses
EXPOSE 8080

# Start the application
CMD ["python3", "app.py"]
