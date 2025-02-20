
FROM ubuntu


RUN apt update -y && apt install python3 python3-pip pipenv -y


WORKDIR /app


COPY . /app/


RUN pip install -r requirements.txt


EXPOSE 80


CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80", "--reload"]
