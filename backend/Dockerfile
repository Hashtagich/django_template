# pull official base image
FROM python:3.12.5-slim-bookworm

# set work directory
WORKDIR /usr/src/app

RUN mkdir /usr/src/app/static
RUN mkdir /usr/src/app/media

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install system dependencies
RUN apt-get update && apt-get install -y netcat-openbsd

# install dependencie
RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt

# copy entrypoint.sh
COPY ./entrypoint.sh .
#COPY ./worker-entrypoint.sh .
RUN sed -i 's/\r$//g' /usr/src/app/entrypoint.sh
RUN chmod +x /usr/src/app/entrypoint.sh
#RUN sed -i 's/\r$//g' /usr/src/app/worker-entrypoint.sh
#RUN chmod +x /usr/src/app/worker-entrypoint.sh

# copy project
COPY . .

# run entrypoint.sh
ENTRYPOINT ["/usr/src/app/entrypoint.sh"]