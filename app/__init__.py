from flask import Flask, render_template
from config import config


def create_app(config_name='default'):
    """Application factory pattern"""
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    
    # Register blueprints
    from app.routes.main import main
    from app.routes.competitions import competitions_bp
    
    app.register_blueprint(main)
    app.register_blueprint(competitions_bp, url_prefix='/competitions')
    
    # Error handlers
    @app.errorhandler(404)
    def page_not_found(e):
        return render_template('pages/404.html'), 404
    
    @app.errorhandler(500)
    def internal_server_error(e):
        return render_template('pages/404.html'), 500
    
    return app
