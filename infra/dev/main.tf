provider "aws" {
  region = var.region
}

output "container_json_raw" {
  value = file("${path.module}/container_definitions.json")
}

resource "aws_iam_role" "ecs_task_execution_role" {
  name = "toy-api-execution-role"

  assume_role_policy = jsonencode({
    Version = "2012-10-17",
    Statement = [{
      Effect = "Allow",
      Principal = {
        Service = "ecs-tasks.amazonaws.com"
      },
      Action = "sts:AssumeRole"
    }]
  })
}

resource "aws_iam_role_policy_attachment" "ecs_execution_role_policy" {
  role       = aws_iam_role.ecs_task_execution_role.name
  policy_arn = "arn:aws:iam::aws:policy/service-role/AmazonECSTaskExecutionRolePolicy"
}


module "ecs" {
  source                   = "../modules/ecs"
  cluster_name             = "toy-api-cluster-dev"
  task_family              = "toy-api"
  container_definitions_file = "${path.module}/container_definitions.json"
  execution_role_arn       = aws_iam_role.ecs_task_execution_role.arn
  cpu                      = "256"
  memory                   = "512"
}

module "rds" {
  source = "../modules/rds"

  db_name               = "toy_api_db"
  db_username           = "postgres"
  db_subnet_ids         = module.network.public_subnet_ids
  vpc_security_group_ids = [module.network.lb_sg_id] # o un SG específic per a RDS si vols
}


module "network" {
  source              = "../modules/network"
  vpc_cidr            = var.vpc_cidr
  availability_zones  = var.availability_zones
  public_subnet_cidrs = var.public_subnet_cidrs
}


module "alb" {
  source = "../modules/alb"
  lb_name = "toy-api-alb"
  security_group_ids  = [module.network.lb_sg_id]
  subnet_ids          = module.network.public_subnet_ids
}

