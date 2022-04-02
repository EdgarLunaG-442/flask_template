try:
    from api import create_app
    from flask import Flask

    settings_module = 'config.default'
    application = create_app(settings_module)
    if __name__ == "__main__":
        application.run(debug=True)
except ImportError as e:
    print(e.msg)
