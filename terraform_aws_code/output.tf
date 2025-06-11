output "jenkins_ip" {
  value = aws_instance.jenkins.public_ip
}
output "sonarqube_ip" {
  value = aws_instance.sonarqube.public_ip
}
output "nexus_ip" {
  value = aws_instance.nexus.public_ip
}
output "server_ip" {
  value = aws_instance.server.public_ip
}
