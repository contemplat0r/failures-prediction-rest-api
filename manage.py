import os
import unittest
import socket

#from flask import g
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager
#from flask_script import Server, Manager


import redis
from rq import Connection, Worker

from app.main import create_app, db
from app import blueprint
from app.main.model import failures


#queue = rq.Queue('prediction-tasks', connection=Redis.from_url('redis://'))
#from uwsgi import app
#manager = Manager(app)
#if __name__ == '__main__':
#    manager.run()

listen_port = 8000

print("hostname", socket.gethostname())
print("fqdn", socket.getfqdn())


app = create_app('dev')

app.register_blueprint(blueprint)

app.app_context().push()

manager = Manager(app)

migrate = Migrate(app, db)

manager.add_command('db', MigrateCommand)

@manager.command
def run():
    #app.run(debug=True, host='0.0.0.0', port=listen_port)
    app.run(debug=False, host='0.0.0.0', port=listen_port)

@manager.command
def runworker():
    #redis_url = app.config['REDIS_URL']
    redis_url = app.config['REDIS_URL']
    #redis_connection = redis.from_url('redis://172.18.0.2:6379')
    redis_connection = redis.from_url('redis://redis:6379/0')
    with Connection(redis_connection):
        #worker = Worker(app.config['QUEUES'])
        worker = Worker(['prediction-tasks'])
        worker.work()

@manager.command
def test():
    """Runs the unit tests."""
    tests = unittest.TestLoader().discover('app/test', pattern='test*.py')
    result = unittest.TextTestRunner(verbosity=2).run(tests)
    if result.wasSuccessful():
        return 0
    return 1

if __name__ == '__main__':
    manager.run()
