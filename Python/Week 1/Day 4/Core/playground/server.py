from flask import Flask, render_template  # added render_template!
app = Flask(__name__)                     
    
@app.route('/<int:x>/<color>')
def index(x, color):
    return render_template("index.html", x=x, color=color)

if __name__=="__main__":
    app.run(debug=True)                   

