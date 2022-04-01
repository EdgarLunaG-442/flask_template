try:
    from api import create_app

    settings_module = 'config.default'
    application = create_app(settings_module)
    
except ImportError as e:
    print(e.msg)
