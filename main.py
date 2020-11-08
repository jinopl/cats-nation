from flask import Flask,render_template
app = Flask(__name__)

@app.route("/")

def hello():
    return "Welcome to cats-nation , GO TO localhost:5000/cats FOR  CATS "

@app.route("/cats")
def cats():
	return render_template('cats-nation.html')

if __name__ == "__main__":
    app.run()