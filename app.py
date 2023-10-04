from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def Home():
    page_title = 'Grobots Club'  # Set the default title
    return render_template ("index.html", page_title=page_title)


@app.route('/EmpoweringYoungMinds')
def EmpoweringYoungMinds():
    page_title = 'EmpoweringYoungMinds'
    return render_template("empoweringyoungminds.html", page_title=page_title)

if __name__ == "__main__": 
    app.run(debug=True, host="0.0.0.0") 

