# AI secure vault pro

An end-to-end serverless cloud application built on AWS that uses AI to automatically categorize and secure uploaded images.

## How it Works
1. **Frontend**: Hosted on **S3** & **CloudFront** (CDN) for global performance.
2. **Storage**: Images are uploaded directly to **S3** using **Presigned URLs**.
3. **AI Pipeline**: S3 triggers a **Lambda** function that calls **AWS Rekognition** to detect objects.
4. **Database**: Metadata and AI tags are stored in **DynamoDB**.

## 🛠 Tech used
- **Languages**: HTML5, CSS3, JavaScript, Python (Boto3)
- **AWS Services**: S3, Lambda, API Gateway, DynamoDB, Rekognition,CloudFront

## Security
This project follows the **AWS Well-Architected Framework** by:
- Using **Least Privilege** IAM roles.
- Implementing **Presigned URLs** to avoid exposing long-term credentials.
- Utilizing **Origin Access Control (OAC)** for S3 bucket security.

## Author
**Sajith Jayashan Rathnayaka**
*Undergraduate Student*
