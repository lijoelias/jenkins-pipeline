# Initialize the AWS provider
provider "aws" {
  region = "us-east-1"  # Set your desired AWS region
}

# Define an EC2 instance resource
resource "aws_instance" "example" {
  ami           = "ami-067d1e60475437da2"  # Replace with your desired Amazon Machine Image (AMI)
  instance_type = "t2.micro"      # Replace with your desired instance type
}

# Output the public IP address of the created instance
output "public_ip" {
  value = aws_instance.example.public_ip
}
