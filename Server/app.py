from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/get')
def hello_world1():
    return 'Hello, shristi ruakkar!!'

if __name__ == "__main__":
    app.run(debug=True)