from flask import Blueprint, jsonify, request
from sqlalchemy import text
from sqlalchemy.exc import SQLAlchemyError
from connect_db import engine

employees_bp = Blueprint("employees", __name__)

@employees_bp.route("/employees", methods=['GET'])
def get_employees():
    try:
        # Use the context manager with the imported engine
        with engine.connect() as connection:
            query = text("SELECT * FROM employees;")
            result = connection.execute(query)

            # Format the results into a list of dictionaries
            employees = [row._asdict() for row in result]
            return jsonify(employees)

    except SQLAlchemyError as e:
        return jsonify({"error": f"Database error: {e}"}), 500
