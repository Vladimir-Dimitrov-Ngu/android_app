import base64
import os
import shutil

from frontend.config import UPLOAD_DIRECTORY


def save_file(name, content):
    """Decode and store a file uploaded with Plotly Dash."""
    data = content.encode("utf8").split(b";base64,")[1]
    with open(os.path.join(UPLOAD_DIRECTORY, name), "wb") as fp:
        fp.write(base64.decodebytes(data))


def uploaded_files():
    """List the files in the upload directory."""
    files = []
    for filename in os.listdir(UPLOAD_DIRECTORY):
        path = os.path.join(UPLOAD_DIRECTORY, filename)
        if os.path.isfile(path):
            files.append(filename)
    return files


def find_latest_file(directory):
    files = [os.path.join(directory, file) for file in os.listdir(directory)]
    files.sort(key=lambda x: os.path.getmtime(x), reverse=True)
    if files:
        return files[0]
    else:
        return None


def create_dir(UPLOAD_DIRECTORY):
    if os.path.exists(UPLOAD_DIRECTORY):
        shutil.rmtree(UPLOAD_DIRECTORY)
    if not os.path.exists(UPLOAD_DIRECTORY):
        os.makedirs(UPLOAD_DIRECTORY)
