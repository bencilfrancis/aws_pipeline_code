#!/usr/bin/env python3
import json

with open("inventory.json") as f:
    data = json.load(f)

inventory = {
    "jenkins": {
        "hosts": [data["jenkins_ip"]["value"]]
    },
    "sonarqube": {
        "hosts": [data["sonarqube_ip"]["value"]]
    },
    "nexus": {
        "hosts": [data["nexus_ip"]["value"]]
    },
    "server": {
        "hosts": [data["server_ip"]["value"]]
    },
    "_meta": {
        "hostvars": {
            ip: {
                "ansible_user": "ubuntu",
                "ansible_ssh_private_key_file": "../terraform-key.pem"
            }

            for ip in [
                data["jenkins_ip"]["value"],
                data["sonarqube_ip"]["value"],
                data["nexus_ip"]["value"],
                data["server_ip"]["value"]
            ]
        }
    }    
}
print(json.dumps(inventory, indent=2))