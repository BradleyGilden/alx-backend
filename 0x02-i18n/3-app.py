#!/usr/bin/env python3

"""
Allow babel to find best match of available languages

Author: Bradley Dillion Gilden
Date: 06-02-2024
"""
from flask import Flask, render_template, request
from flask_babel import Babel
import pytz


class Config:
    """class for Babel configuration"""
    BABEL_DEFAULT_LOCALE = "en"
    LANGUAGES = ["en", "fr"]
    TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)


@babel.localeselector
def get_locale():
    """finds best match for configured languages"""
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route("/", strict_slashes=False)
def index():
    """returns the page index"""
    return render_template("3-index.html")


if __name__ == '__main__':
    app.run(debug=True)
