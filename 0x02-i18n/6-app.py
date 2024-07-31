#!/usr/bin/env python3
"""
Basic Flask app
"""
from flask import Flask, render_template, request, g
from flask_babel import Babel

app = Flask(__name__)
babel = Babel(app)


class Config:
    """
    Config class.
    Contains configuration for the Babel plugin.
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)

users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


def get_user(login_as):
    """
    Get the user associated with a given login_as value.

    Parameters
    ----------
    login_as : str
        The value of the login_as argument to a URL. This is the
        value of the g.user variable after calling the
        before_request function.

    Returns
    -------
    user : dict
        A dictionary representing the user associated with the
        given login_as value. If no user is associated with
        the given login_as value, this will be None.
    """
    try:
        return users.get(int(login_as))
    except Exception:
        return


@app.before_request
def before_request():
    """
    Set the g.user variable in the global context of the request.

    This function is called before each request and sets the
    g.user variable based on the "login_as" argument in the query
    string. The g.user variable is used in the templates to
    display the user's name and other information.

    If the "login_as" argument is not present, the g.user variable
    is set to None.
    """
    g.user = get_user(request.args.get("login_as"))


@babel.localeselector
def get_locale():
    """
    Determine the best match of the incoming request's locale
    from the LANGUAGES configuration variable.

    This function is called by Flask-Babel to determine the
    best match of the incoming request's locale. The function
    looks at the following sources in order to determine the
    best match:

    1. The "locale" argument in the query string of the
       request URL.
    2. The "locale" attribute of the request object,
       which is inferred from the Accept-Language header of
       the request.
    3. The "locale" header of the request.
    4. If all of the above are not present, the best match
       of the LANGUAGES configuration variable.

    The best match is determined by using the
    accept_languages.best_match() method of the request
    object.

    Parameters
    ----------
    None

    Returns
    -------
    locale : str
        The best match of the incoming request's locale
        from the LANGUAGES configuration variable. If no
        match is found, the function returns None.
    """
    locale = request.args.get("locale")
    if locale:
        return locale
    user = request.args.get("login_as")
    if user:
        lang = users.get(int(user)).get('locale')
        if lang in app.config['LANGUAGES']:
            return lang
    headers = request.headers.get("locale")
    if headers:
        return headers
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/', methods=["GET"], strict_slashes=False)
def hello():
    """Returns the 0-index.html template."""
    return render_template('6-index.html')


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
