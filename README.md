# Taskr - A Task Manager

Taskr is a simple task manager made for a Software Engineering course at San Jose State University



## Installation

To install and run Taskr, simply clone the GitHub repository onto a local machine, then run the run.py file using the following command when in the root folder.

```bash
python run.py
```

Afterwards, you should see :

```bash
*Serving Flask app "app" (lazy loading)
*Environment: production
 WARNING: This is a development server. Do not use it in a production deployment.
 Use a production WSGI server instead.
*Debug mode: on
*Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
*Restarting with stat
*Debugger is active!
```

You can now access Taskr on your web browser by typing http://127.0.0.1:5000/ in the address bar!





## Usage

After following the installation steps, you will find yourself on the login page. If this is your first time on the site, you will need to click on the register link at the bottom. This will then prompt you to crate a username and password which will let you access the site and it's features!



### Register User

As mentioned above, the first step to using Taskr is to create a new user using the register link at the bottom of the login page. This will let you access the site. 



### Login/Logout

Once a user is registered, they can enter their credentials into the login page and gain access to the Taskr homepage! The homepage should greet you with a Hi User message!

Once the user is ready to leave the site, they can logout by simply pressing the logout button at the right of the Navbar at the top of the page. 



### Add List

To add a list, the user can simply click the "Lists" button on the navbar at the top of the screen. The user will then be prompted to enter the name of the new list and click "Add List" and the list will be created. The list that is created will link to the task list page associated with it.



### Add Task

To add a task, the user can click the dropdown menu on the navbar which will take them to the task page. Here they can type in the task, press "add task" and the task will be displayed on the screen.



### Navbar

The navbar is visible and usable throughout the site, and can help the user navigate to different pages and logout of their account. The navbar can be seen in the top portion of the screen and has a home button, a lists button, a dropdown menu with some placeholders, and a logout button.



### Inbox

The inbox lists the tasks that were added from the task page. It has a refresh button that refreshes the page. If a task is added in another tab from the add task function, a refresh will update the inbox.



### Priority Markers

When creating a task, the user has the ability to check the "Priority" box which will add two asterisks around the task, signifying it's priority. 



### Color Formatting for Task

When creating a task, the user has the ability to choose whether they want their task to be listed in red, green, blue or any combination of the colors! It is as simple as checking the box or boxes next to the colors they want.