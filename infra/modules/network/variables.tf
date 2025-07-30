variable "vpc_cidr" {
  type    = string
  default = "172.31.0.0/16"
}

variable "availability_zones" {
  type    = list(string)
  default = ["eu-west-1a", "eu-west-1b", "eu-west-1c"]
}


variable "public_subnet_cidrs" {
  type = list(string)
  description = "List of public subnet CIDR blocks"
}

