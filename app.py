from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def Home():
    page_title = 'Grobots Club'  # Set the default title
    return render_template ("index.html", page_title=page_title)


@app.route('/gallery')
def Gallery():
    page_title = 'Gallery'
    return render_template("gallery.html", page_title=page_title)

@app.route('/aboutus')
def AboutUs():
    page_title='AboutUs'
    return render_template("aboutus.html", page_title=page_title)

if __name__ == "__main__": 
    app.run(debug=True, host="0.0.0.0") 

