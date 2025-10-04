provider "aws" {
  region = "us-east-1"
}
resource "aws_s3_bucket" "logs" {
  bucket = "mybucket71198"
  acl    = "private"
}
