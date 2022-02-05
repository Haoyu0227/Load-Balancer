from flask import Flask


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_mapping(
        SECRET_KEY='dev',
    )
    app.jinja_env.auto_reload = True

    from .apis import api
    app.register_blueprint(api, url_prefix='/')


    return app