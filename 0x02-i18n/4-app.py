#!/usr/bin/env python3

"""
Forcing Locale

Author: Bradley Dillion Gilden
Date: 06-02-2024
"""
from flask import Flask, render_template, request
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


@babel.localeselector
def get_locale():
    """
    returns default locale if requested locale does not exist
    """
    locale = request.args.get('locale')
    if locale:
        return locale
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route("/", strict_slashes=False)
def index():
    """returns the page index"""
    return render_template("3-index.html")


if __name__ == '__main__':
    app.run(debug=True)
