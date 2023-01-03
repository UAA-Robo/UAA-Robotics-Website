### Hub to store everything to do with the UAA Robotics Website


### Local Dev Installation

#### Linux and MacOS Instructions

1. Copy the repository onto your local machine.

`git clone https://github.com/UAA-Robo/UAA-Robotics-Website.git`

2. Navigate to the UAA Robotics Website folder containing the project

`cd ~/parent/directories/then/UAA-Robotics-Website`

Your path will be slightly different, but you'll need to change to the appropriate
directory where you've cloned the repository.  Ask someone if you're confused
at this point.

3. Create a virtual environment to manage your dependencies

`python3 -m venv ./venv`

This tells python to make a new virtual environment inside a folder called venv in the folder you're
currently in.

4. Turn on the virtual environment

`source venv/bin/activate`

this runs the activation script in the virtual environment.  The command
prompt should look something like this now:

`(venv) patrickpragman@pop-os:~/PycharmProjects/UAA-Robotics-Website$`

with the name of the virtual environment in perens before the username.

5. Install the requirements.

Run the following command to install all the project requirements.

`pip install -r requirements.txt`

6. Check your work

You now have a local copy of the website on your computer and you can run
it by running the `app.py` run the following command to check. 

`python3 app.py`

Note: if the webpage doesn't update with changes after refreshing the browser, you
may need to set Flask to development mode by running `export FLASK_ENV=development`

7. Contribute!

Remember to talk to someone before you start pushing code to master, but you're
ready to start writing code!

#### Things to be aware of

If you haven't worked with virtual environments before they can
be tricky.  Remember when you're done working on the project
to run the command `deactivate` in the terminal, and before
you start working on the project, always remember to activate
the project.

Deactivate can be done from any directory, but the only way
to activate a project is to run the activation script in the
folder containing the venv.  In our case that's 

`source ~/path/to/UAA-Robotics-Website/venv/bin/activate`

let me know if you have any questions.