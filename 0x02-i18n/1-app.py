#!/usr/bin/env python3

"""
Working with Babel configurations

Author: Bradley Dillion Gilden
Date: 06-02-2024
"""
from flask import Flask, render_template
from flask_babel import Babel
import pytz


class Config:
    """class for Babel configuration"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)


@app.route("/", strict_slashes=False)
def index():
    """returns the page index"""
    return render_template("1-index.html")


if __name__ == '__main__':
    app.run(debug=True)
