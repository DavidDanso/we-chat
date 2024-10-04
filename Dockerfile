# Use the official Python image as a base image
FROM python:3.11-alpine

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1  
ENV PYTHONUNBUFFERED=1  

# Set the working directory in the container
WORKDIR /app

# Copy the requirements.txt file into the container
COPY requirements.txt /app/

# Upgrade pip version
RUN pip install --upgrade pip

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire project into the container
COPY . /app

# Expose the port that the Django app runs on
EXPOSE 8000

# Run Django server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
