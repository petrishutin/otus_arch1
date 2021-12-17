FROM python:3.8.10
ENV PYTHONUNBUFFERED 1
WORKDIR /
RUN pip install --upgrade pip
COPY ./requirements.txt /
RUN pip install -r requirements.txt
COPY . .
ENV PYTHONPATH=/
