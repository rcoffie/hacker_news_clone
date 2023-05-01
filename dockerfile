# We need to import a python based image
FROM python:3.9-buster

# Create a working directory for our docker file
WORKDIR /hacker_news

# Sends python output to our container logs
ENV PYTHONBUFFERED=1

# Copy all of the packages that are within our requirements.txt file
COPY requirements.txt requirements.txt

# Install all of the packages that are within our requirements.txt file
RUN pip3 install -r requirements.txt

# Copy our entire project directory for our docker image
COPY . .

# To run our Django app we need to serve it with Gunicorn 

# Please note: elevate is the name of my Django project
CMD gunicorn core.wsgi:application --bind 0.0.0.0:9000

# Expose our docker image at port 9000
EXPOSE 9000