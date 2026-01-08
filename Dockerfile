FROM python:3.12-slim

WORKDIR /app
COPY requirements.txt .

RUN python -m pip install --upgrade pip 
RUN pip install -r requirements.txt

COPY . .

EXPOSE 5000 

CMD ["python", "app.py"]

