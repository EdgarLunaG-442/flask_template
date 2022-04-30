from api import create_app
from flask import Flask

settings_module = 'config.default'


def gunicorn():
    application = create_app(settings_module)
    return application


try:
    if __name__ == "__main__":
        application = create_app(settings_module)
        application.run(debug=True, host="0.0.0.0")

except ImportError as e:
    print(e.msg)
