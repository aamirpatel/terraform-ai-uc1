#deny[msg] {
#  input.resource_type == "aws_s3_bucket"
#  input.acl == "public-read"
#  msg = "Public S3 buckets are not allowed"
#}

package terraform.ec2

# Allowed instance types
allowed_instance_types = {
  "t3.micro",
  "t3.small",
  "t3.medium"
}

# Main rule to validate EC2 instances
deny[msg] {
  input.resource_type == "aws_instance"

  not allowed_instance_types[input.resource.instance_type]
  msg := sprintf("Instance type '%s' is not allowed. Use one of: %v", [input.resource.instance_type, allowed_instance_types])
}

deny[msg] {
  input.resource_type == "aws_instance"

  not input.resource.tags["Environment"]
  msg := "Missing required tag: 'Environment'"
}

deny[msg] {
  input.resource_type == "aws_instance"

  input.resource.associate_public_ip_address == true
  msg := "Public IP association is not allowed for EC2 instances."
}

deny[msg] {
  input.resource_type == "aws_instance"

  not input.resource.root_block_device.encrypted
  msg := "Root volume must be encrypted."
}
