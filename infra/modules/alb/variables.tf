variable "lb_name" {
  description = "the name of the load balancer"
  type        = string
}

variable "security_group_ids" {
  type = list(string)
}

variable "subnet_ids" {
  description = "List of subnet IDs for the load balancer"
  type        = list(string)
}