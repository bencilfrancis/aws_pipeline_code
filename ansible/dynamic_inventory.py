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
            "ansible_ssh_private_key_file": "../../terraform-key.pem",
            "ansible_ssh_common_args": "-o StrictHostKeyChecking=no -o UserKnownHostsFile=/dev/null"
        }
    },
    "sonarqube": {
        "hosts": [data["sonarqube_ip"]],
        "vars": {
            "ansible_user": "ubuntu",
            "ansible_ssh_private_key_file": "../../terraform-key.pem",
            "ansible_ssh_common_args": "-o StrictHostKeyChecking=no -o UserKnownHostsFile=/dev/null",
            "ansible_become_flags": "-n -S"
        }
    },
    "nexus": {
        "hosts": [data["nexus_ip"]],
        "vars": {
            "ansible_user": "ubuntu",
            "ansible_ssh_private_key_file": "../../terraform-key.pem",
            "ansible_ssh_common_args": "-o StrictHostKeyChecking=no -o UserKnownHostsFile=/dev/null"
        }
    },
    "server": {
        "hosts": [data["server_ip"]],
        "vars": {
            "ansible_user": "ubuntu",
            "ansible_ssh_private_key_file": "../../terraform-key.pem",
            "ansible_ssh_common_args": "-o StrictHostKeyChecking=no -o UserKnownHostsFile=/dev/null"
        }
    },
    "_meta": {}    
}
print(json.dumps(inventory, indent=2))