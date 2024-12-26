from flask import Flask, jsonify
from flask_cors import CORS
from controllers.books_controller import books_bp
from controllers.employees_controller import employees_bp

app = Flask(__name__)
CORS(app)

# Register controllers
app.register_blueprint(books_bp)
app.register_blueprint(employees_bp)

@app.route("/health")
def check_health():
    return jsonify({"status": "success", "message": "Health OK!"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001, debug=True)