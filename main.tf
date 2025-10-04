provider "aws" {
  region = "us-east-1"
}
#resource "aws_s3_bucket" "logs" {
#  bucket = "mybucket71198"
#  acl    = "private"
#}

resource "aws_instance" "example" {
  ami           = "ami-0360c520857e3138f"
  instance_type = "t3.micro"

  tags = {
    Name = "HelloWorld"
  }
}

