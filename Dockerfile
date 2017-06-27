# Import the python/pip 3.5 package
FROM python:3.5

# Install uwsgi
RUN pip install uwsgi

COPY requirements.txt requirements.txt

# Install the apps requirements
RUN pip install -r requirements.txt

# Move the source over to a folder called app in this container 
COPY . /app

# Make the source folder the environment and work directory.
ENV HOME /app
WORKDIR /app

# Expose port 8080 to connect to flask
EXPOSE 8080

# Start uwsgi (merely for rapid testing, production may require you to use nginx) when the container is run.
ENTRYPOINT ["uwsgi", "--http", "0.0.0.0:8080", "--module", "app:app"]
