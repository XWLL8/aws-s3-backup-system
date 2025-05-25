# aws-s3-backup-system
# 🚀 AWS S3 Automated Backup System

A serverless backup solution using AWS Lambda, S3, and CloudWatch Events to automate file backups with cost optimization and encryption.

![AWS Architecture Diagram](images/architecture.png) *(Optional: add your own diagram)*

## 🔧 Features
- **Automatic Backups**: Copies files from source S3 bucket to backup bucket via Lambda.
- **Cost Optimization**: Lifecycle policies transition files to S3 Glacier after 30 days (~68% savings).
- **Security**: KMS encryption for data at rest.
- **Monitoring**: 100% success rate with CloudWatch metrics (0 errors).

## 🛠️ Technologies
- **AWS Services**: Lambda (Python 3.12), S3, CloudWatch, IAM, KMS
- **Infrastructure**: Serverless, event-driven
- **Compliance**: Aligns with Saudi NCA/SAMA CSF standards

## 📸 Proof of Implementation
| Lambda Function | CloudWatch Metrics |
|----------------|-------------------|
| ![Lambda Config](images/lambda.png) | ![Metrics](images/metrics.png) |

| S3 Encryption | Lifecycle Policy |
|--------------|-----------------|
| ![KMS](images/kms.png) | ![Lifecycle](images/lifecycle.png) |

## 🚀 Deployment Steps
1. **Clone this repo**:
   ```bash
   git clone https://github.com/yourusername/aws-s3-backup-system.git
