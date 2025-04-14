#-------------------------------------------------------------------------------
# Name:        nomenclature2
# Purpose:
#
# Author:      Louis-Ulysse Simonet
#
# Created:     05/04/2025
# Copyright:   (c) Louis-Ulysse Simonet 2025
# Licence:     MIT License
#-------------------------------------------------------------------------------


from flask import Flask, render_template, send_file
import os
from generate import generate_image
app = Flask(__name__)

@app.route("/")
def index():
    increment_counter()
    generate_image()  
    name = generate_image()  
    return render_template("index.html", name=name)

@app.route("/moleculename")
def moleculename():
    with open(os.path.join("static", "moleculename.txt"), "r", encoding="utf-8") as f:
        return f.read()

@app.route("/image")
def image():
    return send_file("static/molecule.png", mimetype="image/png")

@app.route("/display")
def display():
    return render_template("display.html") 

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
