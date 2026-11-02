import os
from flask import Blueprint, jsonify, send_from_directory

browseBp = Blueprint('brwoseBp', __name__)

NEEDED_DIR = [
    '/var',
    '/etc',
]


@browseBp.route('/dir')
def dir():
    items = []

    try:
        for path in NEEDED_DIR:

            for item in os.listdir(path):
                itemFullPath = os.path.join(path, item)

                isDir = os.path.isdir(itemFullPath)
                itemType = "dir" if isDir else "file"

                items.append({
                    "name": item,
                    "type": itemType,
                    "path": itemFullPath,
                })

    except PermissionError:
        return jsonify({"error": "Akses ditolak (Permission Denied)"}), 403

    return jsonify({
        "total_items": len(items),
        "items": items
    })
