ARG PYTHON_VERSION=3.9
FROM python:${PYTHON_VERSION}-alpine

WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .
EXPOSE 5000
CMD python app.py
