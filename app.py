from flask import Flask

app = Flask(__name__)

@app.route('/')
def add():
    return "Hello Mirjaxon ."

if __name__=="__main__":
    app.run(debug=True,port=3000)