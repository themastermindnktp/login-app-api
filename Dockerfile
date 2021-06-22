FROM python:3.6

EXPOSE 5000
WORKDIR /code
COPY requirements.txt /code/

RUN pip install --upgrade pip

RUN pip install -r requirements.txt

COPY . /code/

RUN chmod +x wait-for-it.sh

CMD ["sh", "-c", "./wait-for-it.sh mysql:3306 -t 0 -- flask db upgrade heads && flask run --host=0.0.0.0 --port=5000"]


