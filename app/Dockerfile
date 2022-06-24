FROM python:3.8-alpine

COPY ./requirements.txt /app/requirements.txt
WORKDIR /app
RUN pip install -r requirements.txt
#maybe remove
EXPOSE 5000
COPY . /app
CMD [ "python", "app.py" ]