#!/usr/bin/env python3
import json

with open("inventory.json") as f:
    data = json.load(f)

inventory = {
    "all": {
        "children": ["jenkins", "nexus", "sonarqube"]
    },
    "jenkins": {
        "hosts": [data["jenkins_ip"]["value"]],
        "vars": {
            "ansible_user": "ubuntu",
            "ansible_ssh_private_key_file": "../../terraform-key.pem"
        }
    },
    "sonarqube": {
        "hosts": [data["sonarqube_ip"]["value"]],
        "vars": {
            "ansible_user": "ubuntu",
            "ansible_ssh_private_key_file": "../../terraform-key.pem"
        }
    },
    "nexus": {
        "hosts": [data["nexus_ip"]["value"]],
        "vars": {
            "ansible_user": "ubuntu",
            "ansible_ssh_private_key_file": "../../terraform-key.pem"
        }
    },
    "server": {
        "hosts": [data["server_ip"]["value"]],
        "vars": {
            "ansible_user": "ubuntu",
            "ansible_ssh_private_key_file": "../../terraform-key.pem"
        }
    },
    "_meta": {
        "hostvars": {
            ip: {
                "ansible_user": "ubuntu",
                "ansible_ssh_private_key_file": "../../terraform-key.pem"
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