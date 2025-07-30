import os
import boto3
import json

class ProductionConfig:
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    DEBUG = False

def get_production_config():
    secret_name = os.getenv("SECRET_NAME", "myapp-prod-secrets")
    region = os.getenv("AWS_REGION", "eu-west-1")

    client = boto3.client("secretsmanager", region_name=region)
    response = client.get_secret_value(SecretId=secret_name)
    secret = json.loads(response["SecretString"])

    config = ProductionConfig()
    config.SQLALCHEMY_DATABASE_URI = secret["DATABASE_URL"]
    config.SECRET_KEY = secret["SECRET_KEY"]
    return config
