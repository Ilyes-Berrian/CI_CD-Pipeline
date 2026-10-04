from flask import Flask


def create_app():
    app = Flask(__name__)
    print("inside create_app function")

    @app.route('/')
    def home():
        print("inside home function")
        return 'Hi from /home route!'
    @app.route('/about')
    def about():
        print("inside about function")
        return 'Hi from /about route!'
    return app


if __name__ == '__main__':
    app = create_app()

    app.run(host='0.0.0.0', port=80, debug=True)
