# AI secure vault pro
<img width="1293" height="649" alt="image" src="https://github.com/user-attachments/assets/331fe475-3775-43de-a4a6-0d529a89941d" />

An end-to-end serverless cloud application built on AWS that uses AI to automatically categorize and secure uploaded images.

## How it Works
1. **Frontend**: Hosted on **S3** & **CloudFront** (CDN) for global performance.
2. **Storage**: Images are uploaded directly to **S3** using **Presigned URLs**.
3. **AI Pipeline**: S3 triggers a **Lambda** function that calls **AWS Rekognition** to detect objects.
4. **Database**: Metadata and AI tags are stored in **DynamoDB**.

## 🛠 Tech used
- **Languages**: HTML5, CSS3, JavaScript, Python (Boto3)
- **AWS Services**: S3, Lambda, API Gateway, DynamoDB, Rekognition,CloudFront

**Lambda Function Overview**
<img width="816" height="341" alt="image" src="https://github.com/user-attachments/assets/c93ab54e-c35f-431e-8254-7c2849cca760" />

**DynamoDB database table**

<img width="560" height="284" alt="image" src="https://github.com/user-attachments/assets/c3efceea-bb4c-4718-9f26-de52f3fda8cc" />

**API Gateway Routes**

<img width="536" height="222" alt="image" src="https://github.com/user-attachments/assets/a18a6f03-122f-49c8-a84e-71f4f6cc2b08" />

**CloudFront distribution**

<img width="762" height="203" alt="image" src="https://github.com/user-attachments/assets/6ecba862-ff5a-476d-a5e2-53af2f7aa107" />


## Security
This project follows the **AWS Well-Architected Framework** by:
- Using **Least Privilege** IAM roles.
- Implementing **Presigned URLs** to avoid exposing long-term credentials.
- Utilizing **Origin Access Control (OAC)** for S3 bucket security.

## Author
**Sajith Jayashan Rathnayaka**
*Undergraduate Student*
