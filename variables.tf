variable "aws_region" {
  description = "AWS region"
  type        = string
}

variable "tags" {
  description = "Tags to assign to the role"
  type        = map(string)
  default     = {}
}

variable "public_subnet_cidrs" {
  description = "values for public subnets"
  type        = list(string)
  default = ["10.0.1.0/24", "10.0.2.0/24"]
}

variable "private_subnet_cidrs" {
  description = "values for private subnets"
  type        = list(string)
  default = ["10.0.3.0/24", "10.0.4.0/24"]
}