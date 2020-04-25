FROM python:3.7.7

COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
EXPOSE 5005
CMD rasa run actions && rasa run -vv