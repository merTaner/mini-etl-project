FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt ./
COPY ./scripts ./scripts/ 
COPY ./data ./data

RUN pip install -r requirements.txt
RUN python /app/scripts/load_to_mariadb.py && python /app/scripts/transfrom.py

CMD [ "python", "scripts/load.py"]
