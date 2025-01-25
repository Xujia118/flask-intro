from flask import Flask, jsonify


def check_health():
    return jsonify({"status": "success", "message": "Health OK!"})
