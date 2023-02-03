FROM python:3.8-slim

WORKDIR /app
COPY ./app .

COPY requirements.txt /app/requirements.txt

RUN pip install -r requirements.txt

ENTRYPOINT [ "python" ]
CMD [ "app.py" ]