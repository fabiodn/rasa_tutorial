FROM rasa/rasa:1.10.0-full

ENV BOT_ENV=production

# Create app directory
WORKDIR /app

# Install app dependencies
COPY requirements.txt ./

#RUN pip install --upgrade pip
#RUN pip install -r requirements.txt --no-cache-dir

# Bundle app source
COPY . /var/www
WORKDIR /var/www

#ENTRYPOINT [ "rasa", "run", "-p", "5555"]
ENTRYPOINT ["/var/www/run.sh"]
