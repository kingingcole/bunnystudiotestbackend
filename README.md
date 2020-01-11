# bunnystudiotestbackend
Backend repo for Bunny Studio assessment
App is deployed on Heroku and can be found at https://bunny-todo-backend.herokuapp.com/api/users/.

To run on local server, you must have Python installed into the computer. Clone the repo and `cd` into it. You can chose to run it in a virtual environment with Veirtualenv or Venv. With virtual environment running, install the dependencies by running `pip install -r requirements.txt`.
After installations, run `py manage.py runserver` to start the server at localhost:8000.

Endpoints:
- `/users/` - lists out users on the database. Also receives POST data to create new user.
- `/tasks/` - lists out tasks on the database. Also receives POST data to create new task.
- `/users/<username>/` - detail view of a particular user
- `/tasks/<I'd>/` - detail view of a particular task.
