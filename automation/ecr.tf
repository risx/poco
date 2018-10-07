provider "aws" {
  region = "us-west-2"
}

variable "r53_zone" { default="" }

terraform {
  backend "s3" {
    bucket = "sui-terraform-state" //If you want to use this, change this.
    region = "us-west-2"
    key    = "docker-image-ecr.tfstate"
  }
}

data "terraform_remote_state" "sui" {
  backend = "s3"
  config {
    bucket = "sui-terraform-state"
    region = "us-west-2"
    key    = "docker-image-ecr.tfstate"
  }
}

resource "aws_ecr_repository" "sui" {
    name = "sui"
}

resource "aws_route53_record" "sui" {
  zone_id = "${var.r53_zone}"
  name = "sui-ecr.notuncomfy.com" //Also change this 
  type = "CNAME"
  ttl  = "300"
  records = ["${aws_ecr_repository.sui.repository_url}"]
}

#To run: terraform plan -var "r53_zone=ZONEID"