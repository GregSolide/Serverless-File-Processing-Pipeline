from flask import Flask,render_template,request,url_for
import csv

app = Flask(__name__)

@app.route("/",methods= ["GET","POST"])
def hello_world():
    return render_template("Home.html")
@app.route("/file_proccessed",methods=["POST"])
def get_filed():
    if request.method == "POST":
        document = request.files["file"]
        document.save("Frontend/uploads/"+document.filename)
        with open ("Frontend/uploads/"+document.filename,"r") as f:
                    data = csv.reader(f)
                    
    return render_template("test.html")

if __name__ == "__main__":
    app.run(debug=True)
