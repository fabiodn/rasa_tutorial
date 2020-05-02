FROM python:3.7.7


# Create app directory
WORKDIR /app

# Install app dependencies
COPY requirements.txt ./

RUN pip install -r requirements.txt

# Bundle app source
COPY . /app

EXPOSE 5005

CMD /app/run.sh
