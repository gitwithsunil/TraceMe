from flask import Flask
from app.routes import main  # ✅ Correctly import Blueprint

app = Flask(__name__)
app.register_blueprint(main)  # ✅ Register the Blueprint

if __name__ == "__main__":
    app.run(debug=False)
