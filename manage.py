from flask_script import Manager, prompt_bool

from src import app, db
from src.models import User

manager = Manager(app)


@manager.command
def init_db():
    db.create_all()
    db.session.add(User(username='Patryk', email='bob1@wp.pl'))
    db.session.add(User(username='Kacper', email='ala2@wp.pl'))
    db.session.commit()
    print('Database has been initialized')


@manager.command
def drop_db():
    msg = 'Are you sure you want to delete your database?'
    if prompt_bool(msg):
        db.drop_all()
        print('Database has been dropped.')

if __name__ == '__main__':
    manager.run()
