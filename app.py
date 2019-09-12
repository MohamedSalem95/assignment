from manage import create_app, db, migrate, login_manager
from config import DevConfig

from users.models import User


app = create_app(DevConfig)

@login_manager.user_loader
def load_user(id):
    return User.query.get(id)


@app.shell_context_processor
def create_shell_context():
    return  dict(app=app, db=db, migrate=migrate, User=User)


if __name__ == '__main__':
    app.run()
