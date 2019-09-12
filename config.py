class Config:
    SECRET_KEY = 'monkey'


class DevConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///development_db.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class ProdConfig(Config):
    pass
