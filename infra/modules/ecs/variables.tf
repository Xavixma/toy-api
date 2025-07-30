variable "cluster_name" {
  description = "the name of the ECS cluster"
  type        = string
}

variable "task_family" {
  description = "the name of the task family for the ECS task definition"
  type        = string
}

variable "execution_role_arn" {
  description = "IAM role for ECS tasks"
  type        = string
}

variable "container_definitions_file" {
  description = "Path to the container definitions JSON file"
  type        = string
  default     = "/mnt/c/Users/Biel/toy-api/infra/dev/container_definitions.json"
}

variable "cpu" {
  description = "CPU units for the ECS task"
  type        = string
}

variable "memory" {
  description = "Memory in MiB for the ECS task"
  type        = string
}