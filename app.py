import connexion
from flask_cors import CORS
import uvicorn

app = connexion.App(__name__, specification_dir="./")

app.add_api("swagger.yml")

CORS(app.app)


if __name__ == "__main__":
    uvicorn.run(
        "app:app",
        host="127.0.0.1",
        port=5001,
        reload=True  # Enable auto-reloading with uvicorn
    )
