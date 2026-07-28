# Project One: Multi-Node DevOps Tooling Infrastructure

Automation playbooks and roles for setting up a 3-node DevOps infrastructure with Jenkins, SonarQube, Nexus, Nginx reverse proxy + SSL/certbot, glab, OhMyZsh, and Portainer.

---

## Infrastructure Overview & Mapping

| Node Name | Public IP | Internal IP | Services Installed | Domain Name |
| :--- | :--- | :--- | :--- | :--- |
| **machine01-jenkin** | `104.197.103.74` | `10.128.0.2` | Jenkins (Docker), glab, Docker, Ansible, Nginx (Reverse Proxy + Certbot), Portainer, OhMyZsh | `jenkins.devops.lab` |
| **machine02-sonarqube** | `34.59.145.174` | `10.128.0.3` | SonarQube + PostgreSQL (Docker Compose), Portainer, OhMyZsh | `sonarqube.devops.lab` |
| **machine03-nexus** | `136.111.8.19` | `10.128.0.4` | Nexus 3 (Docker Compose with `docker-blob`, `helm-blob`, hosted repos), Portainer, OhMyZsh | `nexus.devops.lab` |

---

## Features

1. **Jenkins Container Capabilities:** Built with a custom `Dockerfile` containing Docker CLI, Docker Compose, `glab` CLI, and `ansible` binary inside the container, with `/var/run/docker.sock` mounted.
2. **SonarQube Stack:** Deployed via Docker Compose with dedicated PostgreSQL 15 database and sysctl parameters pre-configured (`vm.max_map_count=524288`).
3. **Nexus Blobstores & Repositories:** Auto-provisioned using Python API scripts for:
   - Docker Blob Store (`docker-blob`) & Docker Hosted Repo (`docker-hosted`)
   - Helm Blob Store (`helm-blob`) & Helm Hosted Repo (`helm-hosted`)
4. **Nginx Reverse Proxy & HTTPS:** Installed on Machine01 with Nginx virtual hosts reverse proxying requests to all three services, pre-configured with Let's Encrypt Certbot and fallback self-signed certificates.
5. **Portainer & OhMyZsh:** Deployed across all 3 machines for container management and shell experience.

---

## How to Run

### 1. Provision Infrastructure
```bash
ansible-playbook -i inventory/hosts.ini setup.yml
```

### 2. Reset (Destroy) Infrastructure
```bash
ansible-playbook -i inventory/hosts.ini destroy.yml
```

---

## Domain Resolution Setup (Local Testing)
Add the following entries to your workstation's `/etc/hosts` file (or C:\Windows\System32\drivers\etc\hosts):
```text
104.197.103.74 jenkins.devops.lab
104.197.103.74 sonarqube.devops.lab
104.197.103.74 nexus.devops.lab
```
