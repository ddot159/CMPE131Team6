# Taskr - A Task Manager

Taskr is a simple task manager made for a Software Engineering course at San Jose State University

## Installation

To install and run Taskr, simply clone the GitHub repository onto a local machine, then run the run.py file using the following command when in the root folder.

```
python run.py
```

Afterwards, you should see :

```
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

*** IMPORTANT *** : When assigning a due date, use the format 'YYYY-MM-DD' (without the quotes) otherwise the task will not add and register. The Due Date field has to be filled out as well and cannot be empty.

### Register User

As mentioned above, the first step to using Taskr is to create a new user using the register link at the bottom of the login page. This will let you access the site.

### Login/Logout

Once a user is registered, they can enter their credentials into the login page and gain access to the Taskr homepage! The homepage should greet you with a Hi User message!

Once the user is ready to leave the site, they can logout by simply pressing the logout button at the right of the Navbar at the top of the page.

### Add Category

To add a list/Category, the user can simply click the "Tasks" button on the navbar at the top of the screen. The user will then be prompted to enter the name of the new task and also the category, when the user clicks "Add Task" and the category will be created which can be viewed by clicking on the "Categories" option of the dropdown menu on the navbar.

### Add Task

To add a task, the user can click the dropdown menu on the navbar which will take them to the task page. Here they can type in the task, press "add task" and the task will be displayed on the screen.

### Delete Task

A delete button is available to the user on the Task Page, when clicked, it results in the task getting deleted from the list. Before deleting the task, the website shows a confirmation pop-up asking the users if they want to continue and performs the deletion based on their answer.

### Assigning Dates

The user while adding a task has an option to add a deadline to it, and this deadline can be viewed using the inbox option of our web application. When assigning a due date, use the format 'YYYY-MM-DD' (without the quotes).

### Navbar

The navbar is visible and usable throughout the site, and can help the user navigate to different pages and logout of their account. The navbar can be seen in the top portion of the screen and has a home button, a lists button, a dropdown menu with some placeholders, and a logout button.

### Viewing Function

We have enabled an option "Categories" for the user to view the different categories and the tasks assigned to each category. This option is located inside the dropdown-menu of the Navbar.

### Edit Tasks/Categories

Similar to the delete button on the Tasks Page, we have also created an edits button for the user to change the task name, its category or deadline. When clicked it redirects to an Edits Page where three input fields- New Task, New Category, New Deadline are present, out of which only New Deadline field is a required field.

### Mobile Version

For enabling a mobile version, we just added the required meta tag to the all the user-accessed html files. We have also provided instructions on how to run it on your mobile server in run.py file.

### Inbox

The inbox lists the tasks that were added from the task page. It has a refresh button that refreshes the page. If a task is added in another tab from the add task function, a refresh will update the inbox. Also displays a task and its associated elements.

### Mark Completion

Marking completion of a task is what every user needs in a todo-app like Taskr. Basically, the user clicks on the Mark Completion option which is located on the Tasks Page and it turns green indicating the task has been achieved, but if the user mistakenly clicks on it, he/she has an option to unmark again by clicking on it again.

### Priority Markers

When creating a task, the user has the ability to check the "Priority" box which will add two asterisks around the task, signifying it's priority.

### Color Formatting for Task

When creating a task, the user has the ability to choose whether they want their task to be listed in red, green, blue or any combination of the colors! It is as simple as checking the box or boxes next to the colors they want.

### Delete account

If the users feel the need to delete their account because of any reason, they always have an option to do that in the dropdown menu of the navbar, using this option results in the website showing a confirmation pop-up which briefly explains the outcome of proceeding. If they wish to proceed with the action, their data/credentials get deleted from the website's database and they are no longer a valid user.

### Filtering

The precondition is to be in the inbox. A user might remember a specific task they want to pull up and it can be done using the filter search bar. The filtering field filters by the task name but will display other elements associated with it like its category or due date. It is case-sensitive so the user will have to search for the task inputted or it will return a does not exist message. Users can continuously use the filter button afterwards to search for additional tasks.

### Search Bar

If the user has a huge list of tasks they have the option to search for a specific task or tasks. Simply type in the search bar while on the list page and the results will pop up. The user can find the results separate from the long list of all tasks so that they don't mix them up.