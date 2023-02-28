#!/usr/bin/env python3
"""
instantiate the Babel object in your app.
Store it in a module-level variable named babel.

In order to configure available languages in our app, you will create a
Config class that has a LANGUAGES class attribute equal to ["en", "fr"].

Use Config to set Babel’s default locale ("en") and timezone ("UTC").

Use that class as config for your Flask app..
"""
from flask import Flask, render_template
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


babel.init_app(app, locale_selector=get_locale)


if __name__ == "__main__":
    app.run(host='127.0.0.1', port='5000')
