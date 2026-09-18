from flask import Flask, render_template, request
import os
import sys

PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)

from Backend.Logic import Logic

app = Flask(__name__)
logic_module = Logic()

@app.route("/",methods= ["GET","POST"])
def hello_world():
    return render_template("Home.html")
@app.route("/file_proccessed",methods=["POST"])
def get_filed():
    if request.method == "POST":
        document = request.files["file"]
        print(document.filename)
        logic_module.upload_file(document)
        logic_module.downloading_file(document)
    return render_template("test.html")

if __name__ == "__main__":
    app.run(debug=True)
