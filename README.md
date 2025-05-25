# aws-s3-backup-system
# 🚀 AWS S3 Automated Backup System

A serverless backup solution using AWS Lambda, S3, and CloudWatch Events to automate file backups with cost optimization and encryption.



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

### Serverless Backup Workflow
| Component | Screenshot |
|-----------|------------|
| **Lambda Function Configuration** | ![Lambda Console](https://github.com/user-attachments/assets/3d047d0c-a818-4d4b-ade0-0c393ab6eb59) |
| **CloudWatch Success Metrics** | ![100% Success Rate](https://github.com/user-attachments/assets/3ffc22cd-8552-4f63-a41c-fd794611d8fc) |

### Security & Cost Optimization
| Feature | Proof |
|---------|-------|
| **KMS Encryption Enabled** | ![S3 Encryption Settings](https://github.com/user-attachments/assets/f4a3e007-8024-4f0f-9f50-4a8047b2460e) |
| **Glacier Lifecycle Policy** | ![30-Day Transition Rule](https://github.com/user-attachments/assets/fa53f3c1-2149-447b-bdd1-51b41ef1132d) |


## 🚀 Deployment Steps
1. **Clone this repo**:
   ```bash
   git clone https://github.com/yourusername/aws-s3-backup-system.git
