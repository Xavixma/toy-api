resource "aws_ecs_cluster" "this" {
  name = var.cluster_name
}

resource "aws_ecs_task_definition" "this" {
  family                = var.task_family
  container_definitions = file(var.container_definitions_file)
  execution_role_arn    = var.execution_role_arn
  network_mode          = "awsvpc"
  requires_compatibilities = ["FARGATE"]
  cpu                   = var.cpu
  memory                = var.memory
}
