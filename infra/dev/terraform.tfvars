region = "eu-west-1"
execution_role_arn = "arn:aws:iam::517691465982:user/xavi-cli"
cpu=256
memory=512
vpc_cidr = "172.31.0.0/16"


public_subnet_cidrs = [
  "172.31.32.0/20",  # subnet-0cf8eb5337e85560c
  "172.31.0.0/20",   # subnet-0b3c6d430acd8631c
  "172.31.16.0/20"   # subnet-002bd2a708cab5f8d
]

availability_zones = [
  "eu-west-1a",
  "eu-west-1b",
  "eu-west-1c"
]