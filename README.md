# DevOps System Monitoring Deployment

## Project Overview

This project establishes a full, automated deployment pipeline for a system monitoring solution. The solution consists of two distinct services packaged as Docker containers (one Bash-based, one Python-based) and is deployed onto a remote Linux target (AWS EC2) using **Docker**, **Docker Compose**, and **Ansible**.

The core objective is to demonstrate proficiency in:

- **Containerization:** Packaging applications and their dependencies.
- **Orchestration:** Managing multiple containers as a unified service.
- **Automation:** Using Ansible for infrastructure setup and application deployment.

---

## Project Components

| File Name                 | Description                                                                                                                     |
| :------------------------ | :------------------------------------------------------------------------------------------------------------------------------ |
| `bash_monitor.sh`         | Bash script that reports OS details, CPU, RAM, and Disk usage via native Linux commands (`top`, `free`, `df`).                  |
| `python_monitor.py`       | Python script that reports OS details, CPU, RAM, and Disk usage using the `psutil` library.                                     |
| `Dockerfile.bash`         | Builds the image for the Bash service, using **Ubuntu** as the base image.                                                      |
| `Dockerfile.python`       | Builds the image for the Python service, using a **Python 3** slim base image.                                                  |
| `docker-compose.yml`      | Defines both `bash-service` and `python-service`, handles image building, and orchestrates simultaneous deployment.             |
| `deployment_playbook.yml` | Ansible playbook that automates the installation of Docker/Docker Compose and deploys the project files onto the remote target. |
| `inventory.ini`           | Defines the connection details for the remote AWS EC2 server.                                                                   |

---

## Deployment Instructions

The deployment targets a remote **Ubuntu** server.

### Prerequisites

Ensure the following are installed and configured on your local machine:

1.  **Git** and **Docker**.
2.  **Ansible:** Installed via your package manager
3.  **AWS EC2 Instance:** A running Ubuntu instance with SSH access enabled (Port 22).

### 1. Configure SSH Access

1.  **Key File:** Place your AWS private key (`.pem` file) within the project structure (e.g., inside a `keys/` directory).
2.  **Permissions:** Set restrictive permissions on the private key:
    ```bash
    chmod 400 ansible-key.pem
    ```
3.  **Security Note:** Ensure the key file is added to your **`.gitignore`** to prevent accidental public exposure.

### 2. Update Inventory (`inventory.ini`)

Modify the `inventory.ini` file to match your AWS instance details:

```ini
[dev_servers]
aws_monitor ansible_host=PUBLIC_IP_ADDRESS ansible_user=ubuntu ansible_ssh_private_key_file=ansible-key.pem
```

### 3. Execute Ansible Deployment

Run the main playbook from the root of the project directory. This script handles dependency installation, file transfer, and service start-up on the remote server.

```bash
ansible-playbook -i inventory.ini deployment_playbook.yml
```

### 4. Verification

After the Ansible playbook completes successfully, verify the deployment directly on the remote AWS EC2 instance.

1. **Check Running Docker Containers**.

   - SSH into the EC2 instance.
   - Run `docker ps` to confirm both containers are running.

   ```bash
   ssh -i ansible-key.pem ubuntu@PUBLIC_IP_ADDRESS
   docker ps
   ```

2. **View Logs**

   ```bash
   sudo docker-compose -f /opt/system-monitor/docker-compose.yml logs --follow
   ```

3. **Clean Up**
   ```bash
   cd /opt/system-monitor/
   sudo docker-compose down
   ```
