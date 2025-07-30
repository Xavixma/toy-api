data "aws_secretsmanager_secret_version" "rds_secret" {
  secret_id = "arn:aws:secretsmanager:eu-west-1:517691465982:secret:toy-app-secrets-727hgf"
}


resource "aws_db_subnet_group" "this" {
  name       = "toy-api-db-subnet-group"
  subnet_ids = var.db_subnet_ids

  tags = {
    Name = "toy-api-db-subnet-group"
  }
}

resource "aws_db_instance" "this" {
  identifier              = "toyapi-db"
  allocated_storage       = 20
  engine                  = "postgres"
  engine_version          = "15"
  instance_class          = "db.t3.micro"
  username                = var.db_username
  password                = jsondecode(data.aws_secretsmanager_secret_version.rds_secret.secret_string)["password"]
  db_subnet_group_name    = aws_db_subnet_group.this.name
  vpc_security_group_ids  = var.vpc_security_group_ids

  skip_final_snapshot     = true
  publicly_accessible     = false

  tags = {
    Environment = "production"
  }
}
