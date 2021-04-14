from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def screen():
    return render_template('screen.html')

if __name__ == "__main__":
    app.run(debug=True)