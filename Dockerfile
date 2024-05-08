FROM --platform=linux/amd64 python:3.9-bullseye

ENV APP_HOME /app
WORKDIR $APP_HOME
COPY . ./
RUN pip install -r requirements.txt

EXPOSE 8080
CMD exec uvicorn main:app --host 0.0.0.0 --port 8080 --workers 1