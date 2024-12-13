FROM python:3.10-slim-buster

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY code/calculadora.py /app/

COPY code/test_calc.py /app/

CMD ["pytest"] # pode ser modificado para executar a aplicação.
