### Hub to store everything to do with the UAA Robotics Website


### Local Dev Installation

Moving foward it is assumed that you are developing using a linux machine inside a VM. I've determined this to be the simplest way to move forward using NodeJS.

#### Linux and MacOS Instructions

1. Install local dependencies (Python, NPM, Git, and NodeJS), depending on your linux distribution the installation procedure for these packages will be different. 

1. Open the folder you'd like to keep your repos in (open terminal in that folder) and run the following command to copy the repository onto your local machine. 

`git clone https://github.com/UAA-Robo/UAA-Robotics-Website.git`

2. Navigate to the UAA Robotics Website folder containing the project

`cd ~/parent/directories/then/UAA-Robotics-Website`

Your path will be slightly different, but you'll need to change to the appropriate
directory where you've cloned the repository.  Ask someone if you're confused
at this point.

3. Install the requirements.

Run the following command to install all the project requirements.

`pip install -r requirements.txt`

4. Check your work

You now have a local copy of the website on your computer and you can run
it by running `app.py`  or the following command to check. 

`flask run`

Note: if the webpage doesn't update with changes after refreshing the browser, you
may need to stop Flask (`control c`), put Flask to development mode by running `export FLASK_ENV=development`, and restart it.

5. If you need to access pages (like internalIndex.html) that access Atlas MongoDB, 
you will need one of the Web Dev members to add your local IP to the network access list.
After that, if you are getting an `SSL: CERTIFICATE_VERIFY_FAILED` error, you may need to update
your certificates. To do that (on mac), follow the first answer on this Stack Overflow:
https://stackoverflow.com/questions/52805115/certificate-verify-failed-unable-to-get-local-issuer-certificate

6. Contribute!

Remember to talk to someone before you start pushing code to master, but you're
ready to start writing code!

#### Things to be aware of

let me know if you have any questions.
