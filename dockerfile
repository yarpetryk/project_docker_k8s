FROM --platform=linux/amd64 python:3.9

WORKDIR /src/
COPY . .

EXPOSE 8000

# Install python dependencies
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Start web server
RUN  python3 app/MovieRecommendationApp/manage.py runserver 0.0.0.0:8000 &

# Install google chrome
RUN apt-get install -y wget
RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add - \
    && echo "deb http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google.list
RUN apt-get update && apt-get -y install google-chrome-stable


RUN cd tests


# Run test
ENTRYPOINT ["pytest", "-k TestMovieList"]
