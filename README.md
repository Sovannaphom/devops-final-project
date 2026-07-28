# DevOps Training - Final Projects

This repository contains the complete Ansible automation projects for **Project One** and **Project Two**.

---

## Directory Structure

```text
devops-final-project/
├── project-one/             # DevOps Tooling Infrastructure (Jenkins, SonarQube, Nexus, Nginx, Portainer, glab, OhMyZsh)
│   ├── ansible.cfg
│   ├── inventory/
│   │   ├── hosts.ini
│   │   └── group_vars/all.yml
│   ├── roles/               # common, ohmyzsh, docker, portainer, glab, jenkins, sonarqube, nexus, nginx_certbot
│   ├── setup.yml            # Provisioning Playbook
│   ├── destroy.yml          # Teardown / Reset Playbook
│   └── README.md
└── project-two/             # HA Kubernetes Cluster (Kubespray, Traefik, Headlamp, ArgoCD)
    ├── ansible.cfg
    ├── inventory/
    │   └── k8s-cluster/
    │       ├── hosts.yaml
    │       └── group_vars/
    ├── roles/               # kubespray_prep, traefik, headlamp, argocd
    ├── deploy.yml           # Deployment Playbook
    ├── destroy.yml          # Reset Playbook
    └── README.md
```

---

## Quick Start Summary

### Project One Setup
```bash
cd project-one
ansible-playbook -i inventory/hosts.ini setup.yml
```

### Project Two Setup
```bash
cd project-two
ansible-playbook -i inventory/k8s-cluster/hosts.yaml deploy.yml
```
