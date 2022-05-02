from app import create_app
from flask_script import Manager,Server

# Creating app instance
app = create_app('development')

# Instantiate the Manager class
manager = Manager(app)

# Use the add_command method to create a new command 'server' which will launch our application server.
manager.add_command('server',Server)

# Creating a command to run unittests
@manager.command
def test():
    """Run the unit tests."""
    import unittest
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verbosity=2).run(tests)

if __name__ == '__main__':
    manager.run()