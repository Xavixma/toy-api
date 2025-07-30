variable "region" {
  description = "AWS region"
  type        = string
}

variable "execution_role_arn" {
  description = "IAM role for ECS tasks"
  type        = string
}

variable "container_definitions_file" {
  description = "Path to the container definitions JSON file"
  type        = string
}

variable "cpu" {
  description = "CPU units for the ECS task"
  type        = string
}

variable "memory" {
  description = "Memory in MiB for the ECS task"
  type        = string
}

variable "vpc_cidr" {
  description = "CIDR block for the VPC"
  type        = string
}

variable "availability_zones" {
  description = "List of availability zones to use"
  type        = list(string)
}

variable "public_subnet_cidrs" {
  description = "CIDR blocks for public subnets"
  type        = list(string)
}
