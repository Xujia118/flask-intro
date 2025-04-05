from flask import jsonify, request
from sqlalchemy import text
from sqlalchemy.exc import SQLAlchemyError
from connect_db import engine


def get_all_employees():
    try:
        # Use the context manager with the imported engine
        with engine.connect() as connection:
            query = text(
                "SELECT CONCAT(firstName, ' ', lastName) AS `employees_in_usa`\
                    FROM employees e \
                    JOIN offices o ON e.officeCode = o.officeCode \
                    WHERE o.country = :country;")

            result = connection.execute(
                query, {"country": 'USA'})  # We can can user input

            # Format the results into a list of dictionaries
            employees = [row._asdict() for row in result]
            return jsonify(employees)

    except SQLAlchemyError as e:
        return jsonify({"error": f"Database error: {e}"}), 500
