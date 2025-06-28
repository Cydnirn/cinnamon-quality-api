# Use Python 3.9 as base image for compatibility
FROM python:3.9-slim

# Set working directory
WORKDIR /app

# Copy only the necessary files
COPY ./model /app/model/
COPY ./requirements.txt /app/

# Install required packages
RUN pip install --no-cache-dir -r /app/requirements.txt

# Copy the Flask API application
COPY app.py /app/

# Set environment variables
ENV PYTHONPATH=/app
ENV FLASK_APP=app.py
ENV FLASK_ENV=production

# Expose the port the app runs on
EXPOSE 5000

# Command to run the application
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "app:app"]
