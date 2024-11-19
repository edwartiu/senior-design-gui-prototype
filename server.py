"""
This file will help launch the server to handle communication for Sight Guide. A device will be able to
upload images to the device and the server will process the information and return results to the ESP32. 
"""

from flask import Flask, request, jsonify, flash, redirect, url_for
from openai_client import OpenAIClient
import os

openai_client = OpenAIClient()

UPLOAD_FOLDER = "images"

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


@app.route('/general-visual-aid', methods=['POST'])
def general_visual_aid():
    if request.method == "POST":
        if "file" in request.files:
            file = request.files['file']
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], "general-visual-aid", file.filename))
            return jsonify({"message": openai_client.upload_image("images/general-visual-aid/test.png")})

    return jsonify({"message": "image upload failed"})


@app.route("/document-reading", methods=["POST"])
def document_reading():
    if request.method == "POST":
        if "file" in request.files:
            file = request.files['file']
            file.save(os.path.joing(app.config['UPLOAD_FOLDER'], "document-reading", file.filename))


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)