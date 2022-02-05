from app import create_app
from flask_script import Manager

app = create_app('development')
manager = Manager(app)

if __name__ == '__main__':
    # app.run()
    # manager.run()
    print(1)
    app.run(port=5000, debug=True)