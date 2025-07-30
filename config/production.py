import os
import boto3
import json

class ProductionConfig:
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    DEBUG = False

def get_production_config():
    secret_name = os.getenv("SECRET_NAME", "toy-app-secrets")
    region = os.getenv("AWS_REGION", "eu-west-1")

    client = boto3.client("secretsmanager", region_name=region)
    response = client.get_secret_value(SecretId=secret_name)
    secret = json.loads(response["SecretString"])

    config = ProductionConfig()

    # Construïm la DATABASE_URL manualment
    username = secret["username"]
    password = secret["password"]
    host = secret["host"]
    port = secret["port"]
    dbname = secret["dbname"]
    config.SQLALCHEMY_DATABASE_URI = f"postgresql://{username}:{password}@{host}:{port}/{dbname}"

    config.SECRET_KEY = secret.get("SECRET_KEY", "default-secret-key")
    return config

