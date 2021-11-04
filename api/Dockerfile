FROM python:3.10-alpine

WORKDIR /code

RUN pip install --upgrade pip

COPY ./requirements.txt /code/
RUN pip install --no-cache-dir --upgrade -r requirements.txt

COPY ./src /code/src

CMD ["uvicorn", "src.main:api", "--host", "0.0.0.0", "--port", "80"]
