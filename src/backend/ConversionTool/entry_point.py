from backend.ConversionTool.core import FileHTMLConversion
from backend.settings.base import BACKEND_DIR
from flask_restful import Resource
import os
from flask import request, jsonify

UPLOAD_FOLDER = os.path.join(BACKEND_DIR, "uploads")
ALLOWED_EXTENSIONS = {"docx"}


class HelloThere(Resource):
    def get(self):
        return {
            "message": "Hello! Thanks for visiting. Please upload your "
            "Microsoft Word file to /upload. Thanks!"
        }


class UploadFile(Resource):
    def put(self):
        print(request.__dict__)
        file = request.files.get("file")
        # file = request.get("file")
        bytes_stream = file.read()
        html_payload = FileHTMLConversion(bytes_stream)
        return jsonify(
            {
                "data": str(html_payload),
            }
        )
