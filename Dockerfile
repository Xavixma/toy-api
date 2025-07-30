FROM python:3.9-slim
WORKDIR /app

# Instal·lem dependències
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copiem el codi
COPY app/ app/
COPY config/ config/
COPY main.py .
COPY .env.production .env.production
COPY .env.development .env.development

ENV FLASK_ENV=production
ENV FLASK_APP=main.py

EXPOSE 5000
CMD ["gunicorn", "-b", "0.0.0.0:5000", "main:app"]

