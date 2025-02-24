FROM --platform=linux/amd64 python:3.9

WORKDIR /app/
COPY . .

EXPOSE 8000

# Install python dependencies
RUN pip install -r requirements.txt

# Run test
ENTRYPOINT ["python3", "MovieRecommendationApp/manage.py", "runserver"]