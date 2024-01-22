# FROM alpine:latest
# RUN apk update
# RUN apk add py-pip
# RUN apk add --no-cache python3-dev 
# WORKDIR /app
# COPY . /app
# RUN pip --no-cache-dir install --break-system-packages -r requirements.txt
# CMD ["python3", "app.py"]

FROM python:3.8-slim-buster
WORKDIR /app

# We copy just the requirements.txt first to leverage Docker cache
COPY ./requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r requirements.txt
COPY . /app
ENTRYPOINT [ "python" ]
CMD [ "main.py" ]