# Use the official Python image from the DockerHub
FROM python:3.8slim
# Set the working directory in the container
WORKDIR /app

# Copy requirements.txt from the local FLASK-CONTACTS-DEVOPS directory
COPY FLASK-CONTACTS-APP/requirements.txt /app/

# Install the dependencies
RUN pip install --no-cache-dir -r /app/requirements.txt

# Copy the rest of the application code into the container
COPY FLASK-CONTACTS-APP/ /app/
# Set the entrypoint to wait for MySQL and run the app
ENTRYPOINT ["python", "app.py"]