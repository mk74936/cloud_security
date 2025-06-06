# 🌐 Cloud Security Automation and Compliance Dashboard

This project implements a fully automated security and compliance framework for Microsoft Azure, using Infrastructure as Code (Terraform), Azure Policy, CI/CD (GitHub Actions), Event-driven remediation, and monitoring dashboards.

---

## 🚀 Features

- **Infrastructure as Code** with Terraform
- **Policy as Code** using Azure Policy
- **Event-driven remediation** using Azure Functions
- **CI/CD pipeline** using GitHub Actions
- **Real-time compliance monitoring** with Azure Monitor + Workbooks

---

## 📁 Project Structure

```
cloud-security-dashboard/
│
├── terraform/                  # Infrastructure modules (RG, Storage, Monitoring)
├── policies/                   # Azure Policy definitions and initiative
├── functions/                  # Azure Function for auto-remediation
├── pipelines/github-actions/   # GitHub Actions workflow
├── dashboards/                 # KQL queries and workbook for compliance dashboard
└── README.md
```

---

## 🧰 Prerequisites

- Azure CLI
- Terraform
- Python 3.10+
- Azure Subscription
- Azure Functions Core Tools
- GitHub Account

---

## ⚙️ Deployment Steps

### 1. Authenticate with Azure

```bash
az login
az account set --subscription "<your-subscription-id>"
```

### 2. Deploy Infrastructure

```bash
cd terraform
terraform init
terraform apply -auto-approve
```

### 3. Deploy Azure Policies

```bash
az policy definition create --name "audit-tag-env" --rules @policies/tagging-policy.json ...
az policy definition create --name "deny-public-ip" --rules @policies/deny-public-ip.json ...
az policy assignment create --name "assign-env" ...
```

### 4. Deploy Remediation Function

```bash
cd functions/remediation-tagging
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
func azure functionapp publish <your-function-app-name>
```

### 5. Enable GitHub Actions Pipeline

Push to `main` branch to trigger Terraform CI/CD via GitHub Actions.

---

## 📊 Dashboard Setup

- Go to Azure Monitor > Workbooks
- Paste content from `dashboards/workbook.json`
- Customize KQL from `dashboards/queries/`
- Save and pin

---

## 🧹 Cleanup

```bash
az group delete --name demo-security-rg --yes --no-wait
```

---

## 📌 License

This project is for demo and educational purposes.