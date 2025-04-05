from flask import Flask, send_file
from generate import generate_image
import os

app = Flask(__name__)

@app.route("/")
def index():
    generate_image()
    return '''
    <html>
        <head><title>Nomenclature molécule</title></head>
        <body>
            <h1> Formule topologique : </h1>
            <img src="/image" alt="formule topologique d'une moléule carbonée'" />
        </body>
    </html>
    '''

@app.route("/image")
def image():
    return send_file("static/output.png", mimetype="image/png")

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)