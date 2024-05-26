FROM python:3.12.2

COPY . .

RUN pip3 install requests

CMD ["python3", "./main.py"] 