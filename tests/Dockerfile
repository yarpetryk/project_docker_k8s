FROM --platform=linux/amd64 python:3.9

WORKDIR /tests/
COPY . .

# Install python dependencies
RUN pip install -r requirements.txt

# Install google chrome
RUN apt-get install -y wget
RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add - \
    && echo "deb http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google.list
RUN apt-get update && apt-get -y install google-chrome-stable

# Run test
ENTRYPOINT ["pytest", "-m smoke"]
