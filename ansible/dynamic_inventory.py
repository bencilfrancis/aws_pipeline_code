#!/usr/bin/env python3
import json

with open("inventory.json") as f:
    data = json.load(f)

inventory = {
    "all": {
        "children": ["jenkins", "nexus", "sonarqube", "server"]
    },
    "jenkins": {
        "hosts": [data["jenkins_ip"]],
        "vars": {
            "ansible_user": "ubuntu",
            "ansible_ssh_private_key_file": "../../terraform-key.pem"
        }
    },
    "sonarqube": {
        "hosts": [data["sonarqube_ip"]],
        "vars": {
            "ansible_user": "ubuntu",
            "ansible_ssh_private_key_file": "../../terraform-key.pem"
        }
    },
    "nexus": {
        "hosts": [data["nexus_ip"]],
        "vars": {
            "ansible_user": "ubuntu",
            "ansible_ssh_private_key_file": "../../terraform-key.pem"
        }
    },
    "server": {
        "hosts": [data["server_ip"]],
        "vars": {
            "ansible_user": "ubuntu",
            "ansible_ssh_private_key_file": "../../terraform-key.pem"
        }
    },
    "_meta": {}    
}
print(json.dumps(inventory, indent=2))