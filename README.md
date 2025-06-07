# Facial Login System using AWS

This project is a secure and contactless facial recognition-based login system, built using **Flask**, **OpenCV**, and **AWS Rekognition**. It enables users to register and log in using facial data, providing a modern alternative to traditional username-password authentication.

---

## 🔧 Features

- ✅ User Registration with Facial Image
- ✅ Secure Login via Face Recognition
- ✅ AWS S3 for Image Storage
- ✅ AWS Rekognition for Face Matching
- ✅ Flask Backend with HTML Frontend
- ✅ IAM Roles & Policies for Secure Access

---

## 🛠️ Technologies Used

- **Python** (Flask, OpenCV, Boto3)
- **HTML/CSS**
- **AWS S3** – Image Storage
- **AWS Rekognition** – Face Comparison
- **AWS IAM** – Permission Management

---

## 🖥️ Project Structure
- facial-login-system/
- │
- ├── app.py # Main Flask application
- ├── templates/
- │ └── index.html # Frontend UI
- ├── static/
- │ └── style.css # CSS Styling
- ├── captured_images/ # Temporary image captures
- └── utils/
- └── aws_helpers.py # S3 and Rekognition integration


---

## 🚀 How It Works

### 🔐 Registration
1. User captures face via webcam.
2. Image is uploaded to AWS S3 with a unique username.
3. Admin can view & approve users (optional).

### 🔓 Login
1. User captures a new face image.
2. Image is uploaded temporarily to S3.
3. AWS Rekognition compares it with registered faces.
4. If a match is found (above 90% confidence), user is authenticated.

---

## 🧪 Testing

All components were manually tested:
- Face match success/failure scenarios
- S3 upload & retrieval
- Rekognition thresholds
- UI functionality

---

## 📸 Screenshots

Screenshots of user registration, image upload, Rekognition result, and login dashboard are provided in the `screenshots/` folder.

---

## 📦 Setup Instructions

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/facial-login-system-using-aws.git
🛡️ Future Enhancements
Add OTP/email verification

Integrate multi-user roles (admin/user)

Use DynamoDB for storing metadata

Deploy on AWS Lambda (serverless)

🤝 Acknowledgments
AWS Boto3 SDK

Flask Community

OpenCV Library

