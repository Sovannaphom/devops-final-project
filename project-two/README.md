# Project Two: High-Availability Kubernetes Cluster with Kubespray & Addons

Automated Ansible project to install an HA Kubernetes Cluster using **Kubespray** with **Traefik Ingress**, **Headlamp Kubernetes Dashboard**, and **ArgoCD**.

---

## Topology & Requirements

- **HA Cluster Topology:** 3 Nodes (`node1`, `node2`, `node3`) acting as Control Plane + ETCD + Worker nodes.
- **Ingress Controller:** **Traefik v3** (NGINX ingress controller is explicitly disabled in Kubespray configuration).
- **Kubernetes Dashboard:** **Headlamp** configured with custom domain `headlamp.k8s.lab`.
- **GitOps CD:** **ArgoCD** configured with custom domain `argocd.k8s.lab` and customized admin password (`ArgoAdminPassword123!`).

---

## Node Inventory Mapping

| Host Name | Public IP | Internal IP | Roles |
| :--- | :--- | :--- | :--- |
| **node1** | `104.197.103.74` | `10.128.0.2` | Control Plane, ETCD, Worker |
| **node2** | `34.59.145.174` | `10.128.0.3` | Control Plane, ETCD, Worker |
| **node3** | `136.111.8.19` | `10.128.0.4` | Control Plane, ETCD, Worker |

---

## How to Run

### 1. Deploy HA Kubernetes Cluster & Addons
```bash
ansible-playbook -i inventory/k8s-cluster/hosts.yaml deploy.yml
```

### 2. Teardown / Reset Cluster
```bash
ansible-playbook -i inventory/k8s-cluster/hosts.yaml destroy.yml
```

---

## Dashboard & Service Access

### Headlamp Dashboard
- **URL:** `http://headlamp.k8s.lab` (or HTTPS via Traefik)
- **Token Generation:**
  ```bash
  kubectl -n headlamp create token headlamp-admin
  ```

### ArgoCD GitOps UI
- **URL:** `http://argocd.k8s.lab`
- **Username:** `admin`
- **Password:** `ArgoAdminPassword123!`

---

## Domain Resolution Setup (Local Testing)
Add the following entries to your workstation's `/etc/hosts` file (or C:\Windows\System32\drivers\etc\hosts):
```text
104.197.103.74 headlamp.k8s.lab
104.197.103.74 argocd.k8s.lab
```
