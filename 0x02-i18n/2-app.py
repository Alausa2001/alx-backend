#!/usr/bin/env python3
"""
Create a get_locale function with the babel.localeselector decorator.

Use request.accept_languages to determine the best match
with our supported languages..
"""
from flask import Flask, render_template, request
from flask_babel import Babel

app = Flask(__name__)
babel = Babel(app)


class Config():
    """
    config class
    to keep track of languages available
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app.config.from_object(Config)


@babel.localeselector
def get_locale():
    """
     Get locale from request
    """
    return request.accept_languages.bestmatch(app.config['LANGUAGES'])


@app.route('/', methods=['GET'], strict_slashes=False)
def home():
    """
    renders template/index.html
    """
    return render_template('2-index.html')


if __name__ == "__main__":
    app.run(host='0.0.0.0', port='5000')
