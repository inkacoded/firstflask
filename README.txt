import flask

create app.py

import that the file name, and variable name are correct (app)

commands:
flask run

right now we will store data in a list, but usually it should be a database.



Docker:
Create a Dockerfile, and add the following:
FROM python:3.12        # Means that it will use the 3.12 python verson
EXPOSE 5000             # Exposed in this port where the flask app will run
WORKDIR /app            # Go into a folder within Docker image, so we can run it.
RUN pip install flask   # Once in the folder, run the flask app
COPY . /app             # Copy everything into the /app folder
CMD ["flask", "run", "--host", "0.0.0.0"]    # The commands that should be ran when the image runs the container


run in terminal:
docker build -t rest-apis-flask-python .               # -t is for tagging, the . here means is for where the Docker file is located.
