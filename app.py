from livereload import Server
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def hello_world():
    page_title = 'Home'  # Set the default title
    return render_template ("index.html", page_title=page_title)

if __name__ == "__main__": 
    app.run(debug=True, host="0.0.0.0") 

