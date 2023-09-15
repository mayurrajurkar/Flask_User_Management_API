Flask User Management API

This is a Flask-based RESTful API for managing user resources in a MongoDB database. It allows you to perform CRUD (Create, Read, Update, Delete) operations on user data.

git repository -   https://github.com/mayurrajurkar/Flask_User_Management_API.git

pip install -r requirements.txt

python app.py

The API will be available at http://localhost:5000. 


Docker  image -    docker push mayurrajurkar/flask-corider:tagname



API Endpoints
GET /users - Returns a list of all users.
GET /users/<id> - Returns the user with the specified ID.
POST /users - Creates a new user with the specified data.
PUT /users/<id> - Updates the user with the specified ID with the new data.
DELETE /users/<id> - Deletes the user with the specified ID.
