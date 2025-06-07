from flask import Flask, request, jsonify, render_template, redirect, url_for
from awshelpers.s3 import upload_image_to_s3
from awshelpers.rekognition import find_matching_user
import uuid

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')  # taskflow homepage

@app.route('/register', methods=['POST'])
def register_face():
    if 'image' not in request.files:
        return jsonify({"error": "No image uploaded"}), 400

    image_file = request.files['image']
    username = request.form.get('username', 'anonymous')

    s3_url = upload_image_to_s3(image_file, filename=f"{username}.jpg")

    if s3_url:
        return jsonify({"message": "Image uploaded", "url": s3_url})
    else:
        return jsonify({"error": "Upload failed"}), 500


@app.route('/login-face', methods=['POST'])
def login_face():
    if 'image' not in request.files:
        return jsonify({'error': 'No image provided'}), 400

    image = request.files['image']
    username = request.form.get('username', 'anonymous')
    temp_filename = f"faces/temp/{username}_login.jpg"  # include folder here
    s3_url = upload_image_to_s3(image, f"{username}_login.jpg", folder="faces/temp")

    if not s3_url:
        return jsonify({'error': 'Upload failed'}), 500

    matched_user = find_matching_user(temp_filename)
    if matched_user:
        return jsonify({"redirect_url": url_for("dashboard")})
    else:
        return jsonify({"error": "Face not recognized"}), 401


@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')


if __name__ == '__main__':
    app.run(debug=True)
