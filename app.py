# coding=utf8
import logging
import os

from flask import request, send_from_directory
from flask_api import FlaskAPI
from upload_processor import UploadProcessor

application = FlaskAPI(__name__)

# Logging
if not application.debug:
    file_handler = logging.FileHandler("log/logger.log")
    file_handler.setLevel(logging.DEBUG)
    application.logger.addHandler(file_handler)


@application.route("/upload", methods=["POST"])
def hello():
    file = request.files["image"]

    processor = UploadProcessor(file)
    processor.save()
    processed_path = processor.process(log_to_file=True)

    return {"pid": os.getpid(), "file": processed_path}


@application.route("/uploads/<filename>")
def uploaded_file(filename):
    return send_from_directory("uploads", filename)


if __name__ == "__main__":
    application.run()
