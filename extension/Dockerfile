FROM python:3.6
ADD . /app
WORKDIR /app
RUN pip install flask gunicorn Flask-SQLAlchemy mysqlclient
EXPOSE 8080
CMD ["gunicorn", "-b", "0.0.0.0:8080", "extension:app"]
