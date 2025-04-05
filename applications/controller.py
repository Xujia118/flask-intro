from flask import jsonify, request
from sqlalchemy import text
from sqlalchemy.exc import SQLAlchemyError
from connect_db import engine

from applications.utils import format_applications_for_internal_role


def get_all_applications():
    try:
        with engine.connect() as connection:
            query = text(       
                '''
                    SELECT
                        parent.name AS parent_name,
                        child.name AS child_name
                    FROM product_relationships pr
                    JOIN products parent ON pr.parent_product_id = parent.id
                    JOIN products child ON pr.child_product_id = child.id
                    WHERE pr.is_external = 0;
                    '''
                )
            query_result = connection.execute(query)

            formatted_applications_for_internal_role = format_applications_for_internal_role(query_result)
            
            return jsonify(formatted_applications_for_internal_role)

    except SQLAlchemyError as e:
        return jsonify({"error": f"Database error: {e}"}), 500
