from flask import Flask
import flask_jwt_extend
import routes

app = Flask(__name__)

app.register_blueprint(routes.books, url_prefix="/api/books/")

app.config["SECRET_KEY"] = 'your secret key' #Update your secret key for greater security (required)

app.config["JWT_SECRET_KEY"] = 'yor jwt secret key' #Update your secret key for greater security (required)

jwt = jwt.JWTManager(app)

if __name__ == '__main__':
    
    app.run(debug=True)
