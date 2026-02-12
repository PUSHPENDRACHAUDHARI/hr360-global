FROM python:3.11

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app

COPY . /app

RUN pip install --upgrade pip
COPY requirements.txt .
RUN pip install -r requirements.txt

CMD ["gunicorn", "hrms.wsgi:application", "--bind", "0.0.0.0:8000"]
