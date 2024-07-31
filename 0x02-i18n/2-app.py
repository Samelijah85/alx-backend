#!/usr/bin/env python3
"""
Get locale from request
"""

import babel
from flask import Flask, render_template, request
from flask_babel import Babel

app = Flask(__name__)
babel = Babel(app)


class Config:
    """
    Config class.
    Contains configuration for the Babel plugin.
    """
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app.config.from_object(Config)


@babel.localeselector
def get_locale():
    """
    Determine the best match of the incoming request's locale
    from the LANGUAGES configuration variable.

    This is done by looking at the best match of the
    `accept_languages` attribute of the request object
    against the LANGUAGES configuration variable.

    Returns:
        str: The best match of the incoming request's locale
             from the LANGUAGES configuration variable.
    """
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/', methods=['GET'], strict_slashes=False)
def index():
    """Returns the 0-index.html template."""
    return render_template('2-index.html')


if __name__ == '__main__':
    app.run(debug=True)
