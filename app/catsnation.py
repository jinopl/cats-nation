from flask import Flask,render_template
import random
import os
import socket
import argparse
app = Flask(__name__)

color_codes = {
    "red": "#e74c3c",
    "green": "#16a085",
    "blue": "#2980b9",
    "blue2": "#30336b",
    "pink": "#be2edd",
    "darkblue": "#130f40"
}

SUPPORTED_COLORS = ",".join(color_codes.keys())

# Get color from Environment variable
COLOR_FROM_ENV = os.environ.get('APP_COLOR')
# Generate a random color
COLOR = random.choice(["red", "green", "blue", "blue2", "darkblue", "pink"])


@app.route("/")
def main():
    # return 'Hello'
    return render_template('index.html', name=socket.gethostname(), color=color_codes[COLOR])


@app.route("/cats")
def cats():
	return render_template('cats-nation.html')

if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument('--color', required=False)
    args = parser.parse_args()
    
    if args.color:
        print("Color from command line argument =" + args.color)
    elif COLOR_FROM_ENV:
        print("No Command line argument. Color from environment variable =" + COLOR_FROM_ENV)
        COLOR = COLOR_FROM_ENV
    else:
        print("No command line argument or environment variable. Picking a Random Color =" + COLOR)

    # Check if input color is a supported one
    if COLOR not in color_codes:
        print("Color not supported. Received '" + COLOR + "' expected one of " + SUPPORTED_COLORS)
        exit(1)

    # Run Flask Application
    app.run(host="0.0.0.0", port=8080)