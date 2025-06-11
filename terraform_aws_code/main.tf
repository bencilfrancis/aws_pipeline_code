provider "aws" {
    region = "us-east-1"
}

data "aws_vpc" "default" {
  default = true
}

data "aws_ami" "ubuntu" {
  most_recent = true
  owners      = ["099720109477"]

  filter {
    name   = "name"
    values = ["ubuntu/images/hvm-ssd/ubuntu-jammy-22.04-amd64-server-*"]
  }

  filter {
    name   = "virtualization-type"
    values = ["hvm"]
  }
}


variable "key_name" {
    description = "Name of the AWS key pair"
    default = "terraform-key"
}

resource "aws_security_group" "devops_sg" {
    name = "devops-security-group"
    description = "Allow SSH, Jenkins, SonarQube, Nexus"
    vpc_id = data.aws_vpc.default.id 

    ingress {
        description = "Allow SSH"
        from_port = 22
        to_port = 22
        protocol = "tcp"
        cidr_blocks = ["0.0.0.0/0"]
    }

    ingress {
        description = "Allow Jenkins"
        from_port = 8080
        to_port = 8080
        protocol = "tcp"
        cidr_blocks = ["0.0.0.0/0"]
    }

    ingress {
        description = "Allow SonarQube"
        from_port = 9000
        to_port = 9000
        protocol = "tcp"
        cidr_blocks = ["0.0.0.0/0"]
    }

    ingress {
        description = "Allow Nexus"
        from_port = 8081
        to_port = 8081
        protocol = "tcp"
        cidr_blocks = ["0.0.0.0/0"]
    }

    ingress {
        description = "Allow HTTPS"
        from_port = 443
        to_port = 443
        protocol = "tcp"
        cidr_blocks = ["0.0.0.0/0"]
    }

    ingress {
        description = "Allow HTTP"
        from_port = 80
        to_port = 80
        protocol = "tcp"
        cidr_blocks = ["0.0.0.0/0"]
    }

    egress {
        description = "Allow all outbound traffic"
        from_port = 0
        to_port = 0
        protocol = "-1"
        cidr_blocks = ["0.0.0.0/0"]
    }

    tags = {
      Name = "devops-security-group"
    }
  
}

resource "aws_instance" "jenkins" {
    ami = data.aws_ami.ubuntu.id
    instance_type = "t2.large"
    key_name = var.key_name
    vpc_security_group_ids = [ aws_security_group.devops_sg.id ]
    tags = {
      Name = "Jenkins"
    }
}

resource "aws_instance" "sonarqube" {
    ami = data.aws_ami.ubuntu.id
    instance_type = "t2.medium"
    key_name = var.key_name
    vpc_security_group_ids = [ aws_security_group.devops_sg.id ]
    tags = {
      Name = "Sonarqube"
    }
}


resource "aws_instance" "server" {
    ami = data.aws_ami.ubuntu.id
    instance_type = "t2.medium"
    key_name = var.key_name
    vpc_security_group_ids = [ aws_security_group.devops_sg.id ]
    tags = {
      Name = "Server"
    }
}

resource "aws_instance" "nexus" {
    ami = data.aws_ami.ubuntu.id
    instance_type = "t2.medium"
    key_name = var.key_name
    vpc_security_group_ids = [ aws_security_group.devops_sg.id ]
    tags = {
      Name = "Nexus"
    }
}

resource "local_file" "inventory_json" {
  content  = jsonencode({
    jenkins_ip   = aws_instance.jenkins.public_ip
    sonarqube_ip = aws_instance.sonarqube.public_ip
    nexus_ip     = aws_instance.nexus.public_ip
    server_ip    = aws_instance.server.public_ip
  })
  filename = "${path.module}/../ansible/inventory.json"
}
