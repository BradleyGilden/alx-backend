# i18n - with flask-babel

Internationalization (i18n) is the process of preparing software to support local languages and cultural settings for other markets.

## Learning Objectives

* Learn how to parametrize Flask templates to display different languages
* Learn how to infer the correct locale based on URL parameters, user settings or request headers
* Learn how to localize timestamps

## Tasks

* [0-app.py](0-app.py) - First you will setup a basic Flask app in 0-app.py. Create a single / route and an index.html template that simply outputs “Welcome to Holberton” as page title (<title>) and “Hello world” as header (<h1>)
* [templates](templates) - page templates
* [1-app.py](1-app.py) - In order to configure available languages in our app, you will create a Config class that has a LANGUAGES class attribute equal to ["en", "fr"].

  Use Config to set Babel’s default locale ("en") and timezone ("UTC").

  Use that class as config for your Flask app.
* [2-app.py](2-app.py) - Create a get_locale function with the babel.localeselector decorator. Use request.accept_languages to determine the best match with our supported languages.
* []() - 
* []() - 
* []() - 
* []() - 
