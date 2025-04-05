from flask import Flask, render_template, send_file
import os

app = Flask(__name__)

@app.route("/")
def generate():
    # Appel de la fonction de génération de l'image (qui doit être définie ailleurs)
    from generate import generate_image
    generate_image()  # Génère l'image et la sauve dans le dossier static
    return "Image générée avec succès!"
def index():
    return render_template("index.html")  # Assurez-vous que index.html est dans le dossier templates


@app.route("/image")
def image():
    # Envoie l'image générée située dans le dossier static
    return send_file("static/molecule.png", mimetype="image/png")

@app.route("/display")
def display():
    # Affiche le template HTML qui inclut l'image générée
    return render_template("display.html")  # Assurez-vous que display.html est dans le dossier templates

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
