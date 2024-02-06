#!/usr/bin/env python3

"""
Set up simple route

Author: Bradley Dillion Gilden
Date: 06-02-2024
"""
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def index():
    """returns the page index"""
    return render_template("0-index.html")


if __name__ == '__main__':
    app.run(debug=True)
