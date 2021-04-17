# **Github Repository Link**

https://github.com/AdrianBrambila/CMPE131Team6



# **Group Members**

Adrian Brambila  --  AdrianBrambila

Adrian Perez -- Adrian-Perez-98

Mohibkhan Pathan -- Mohib1402

Dennis Vu -- ddot159



# Use Case Description

**Product Name:**  Taskr - A Task Manager

**Problem Statement:** Create a web browser application for managing tasks.



**Use Case Name:**   Login

**Date:** 4/15/21

## Summary

User must be able to login into the software with a username and unique password. Sign up/Login should be handled with checks to make sure the input is correct.

## Actors

actor 1 = User


## Preconditions

* Username
* Password

## Triggers

Submit trigger will submit the input and allow user with correct username and password proceed into the web app.

## Primary Sequence

step 1 enter username
step 2 enter password
step 3 submit credentials


## Primary Postconditions

* none


## Alternate Sequences

* Step 1 Click on forgot password

* step 2 Enter email to reset password


### Alternate Trigger

- Forgot password

### Alternate Postconditions

- Must half email associated with user

## Non-functional Requirements



## Glossary









**Use Case Name:**  Add new list/Remove an old list

**Date:** 4/15/21

## Summary

User should be able to add a new list of ToDo's. There should be a option to title these lists (ex: Goals, Shopping list, Dinner options, etc.).  

## Actors

actor 1 = User


## Preconditions

* Must be signed in
* In the home menu

## Triggers

You must click on a '+' button and name the new title. In order to remove you must click on the '-' next to a list to remove it.

## Primary Sequence

step 1 click '+'
step 2 type name into box
step 3 click add


## Primary Postconditions

* none


## Alternate Sequences

* Step 1 click '-'


### Alternate Trigger

'-' to delete a list

### Alternate Postconditions



## Non-functional Requirements



## Glossary









**Use Case Name:**  Add/Remove item to list

**Date:** 4/15/21

## Summary

User should be able to add and remove items with ease. (ex: + and - buttons would be fast and effecient).

## Actors

actor 1 = User


## Preconditions

* Must be signed in

* Must be inside a list


## Triggers

You must click on a '+' button and name the new title. In order to remove you must click on the '-' next to a task to remove it.

## Primary Sequence

step 1 click '+'
step 2 type name of task into box
step 3 click add


## Primary Postconditions

* none


## Alternate Sequences

* Step 1 Step 1 click '-'


### Alternate Trigger

'-' to delete a task

### Alternate Postconditions



## Non-functional Requirements



## Glossary









**Use Case Name:**  Share Completions of list to other users

**Date:** 4/15/21

## Summary

Users Should be able to share the state of their ToDo's list with other users  

## Actors

actor 1 = User


## Preconditions

- Must have a list able to share

## Triggers

Share button that allows user to share list with another user

## Primary Sequence

step 1 click share
step 2 input user to share to


## Primary Postconditions

* none

## Alternate Sequences

### Alternate Trigger

### Alternate Postconditions



## Non-functional Requirements



## Glossary









**Use Case Name:**  Mark items depending on completion

**Date:** 4/15/21

## Summary

Users should have the option to update the status of a their lists/items depending on how complete they are (ex: complete flag, not complete flag).

## Actors

actor 1 = User


## Preconditions

* Must have list
* Must have a task added to a list already

## Triggers

Drop down list to mark the status of the task

## Primary Sequence

step 1 select drop down
step 2 choose status


## Primary Postconditions

- none

## Alternate Sequences

### Alternate Trigger

### Alternate Postconditions



## Non-functional Requirements



## Glossary









**Use Case Name:**   Priority Markers

**Date:** 4/15/21

## Summary

User should be able to to set tasks with different prioties (ex: urgent - not urgent)

## Actors

actor 1 = User


## Preconditions

* Must have a list
* Must have a task added to a list already

## Triggers

Option on task to change the color to flag the task

## Primary Sequence

step 1 Click on task
step 2 options to set priority


## Primary Postconditions

* none


## Alternate Sequences

### Alternate Trigger

### Alternate Postconditions



## Non-functional Requirements



## Glossary









**Use Case Name:**  Searching

**Date:** 4/17/21

## Summary

User should be able to search for a list with the help of a search bar.

## Actors

actor 1 = User


## Preconditions

* The desired list should already be there in the database

## Triggers

* Clicking on the search button after typing the name of the list would give the user the desired list.

## Primary Sequence

step 1 Type the name of list desired


## Primary Postconditions

* none


## Alternate Sequences

* none

### Alternate Trigger

### Alternate Postconditions




## Non-functional Requirements



## Glossary









**Use Case Name: ** Navbar

**Date:** 4/17/21

## Summary

Users should be able to switch between the pages with the help of a bar at the top with buttons that serve as a link to the different pages(Home, About).

## Actors

actor 1 = User


## Preconditions

* The buttons for the desired pages should be available on every webpage.

## Triggers

* Clicking on the button for a particular webpage would result in the browser redirecting to that webpage.

## Primary Sequence

step 1 click on the button for a particular webpage on the navbar


## Primary Postconditions

* none


## Alternate Sequences

* none

### Alternate Trigger

### Alternate Postconditions



## Non-functional Requirements



## Glossary









**Use Case Name:** Formatting and color options

**Date:**  4/15/2021

## Summary

Allow users the ability to add color and formatting like bold, underline and italics to make certain tasks more visible or highlight importance

## Actors

actor 1 = User




## Preconditions

* Already logged in

* Already made a new task





## Triggers

When certain portions of text are highlighted, a formatting menu appears with options.

## Primary Sequence

step 1) Highlight text
step 2) Select formatting wanted


## Primary Postconditions

* Selected Item must be formatted in the way indicated by the user











**Use Case Name:**  Usable Mobile Version

**Date:** 4/15/2021



## Summary

Allow user to have access to a usable mobile version, not losing main functionality of the app when accessed on a mobile device.

## Actors

actor 1= User



## Preconditions

* n/a




## Triggers

When site is accessed on a mobile device, should launch a useable version

## Primary Sequence

step 1) Open site on mobile device


## Primary Postconditions

* Site should be readable and usable on a mobile version









**Use Case Name:** Inbox

**Date:** 4/17/21

## Summary

Users should have a place to find their tasks and to do lists.

## Actors

actor 1 = User


## Preconditions

* user is logged in


## Triggers

The user presses or clicks the inbox icon

## Primary Sequence

step 1 Use the search bar or scroll through inbox to find a list or task
step 2 Select the item the user wants to view
step 3 Select the back arrow to exit the inbox


## Primary Postconditions

* inbox refreshes after the user exits




## Alternate Sequences

Only if you have alt seq

* Step 1 If the user used the search bar to find an item hit enter and then select item




### Alternate Trigger

*none

### Alternate Postconditions

* user manually refreshes the inbox

## Non-functional Requirements



## Glossary







**Use Case Name:** Calendar

**Date:** 4/17/21



## Summary

The calendar function allows user to set up reminders on upcoming dates


## Actors

actor 1 = user


## Preconditions

* user is logged in




## Triggers

User presses calendar link or icon on the page


## Primary Sequence

step 1 On the actual calender select a date MM/DD/YYYY 
step 2 Select a time or range of time for the item
step 3 Save to make changes



## Primary Postconditions

* postcondition

* postcondition

* etc



## Alternate Sequences


* n/a



### Alternate Trigger

### Alternate Postconditions



## Non-functional Requirements



## Glossary









**Use Case Name: **Filtering inbox

**Date:**



## Summary

Used to find specific items in the inbox



## Actors

actor 1 = user



## Preconditions

* user logged in

* inside of inbox

* filters are assigned to items



## Triggers

user selects the filtering tool in the inbox


## Primary Sequence

step 1 select the desired options marked as flagged/starred/archive/unread
step 2 click done



## Primary Postconditions

* n/a 

* 



## Alternate Sequences



* users can select multiple options




### Alternate Trigger

### Alternate Postconditions



## Non-functional Requirements



## Glossary









**Use Case Name:** Notifications

**Date:**



## Summary

write summary here



## Actors

actor 1
actor 2
….


## Preconditions

* precond 1

* precond 2

* ….



## Triggers

Explain trigger here



## Primary Sequence

step 1 action
step 2 action
etc


## Primary Postconditions

* postcondition

* postcondition

* etc



## Alternate Sequences

only if you have an alt seq

* step 1 alt seq.

* step 2 alt seq.

* etc



### Alternate Trigger



### Alternate Postconditions



## Non-functional Requirements



## Glossary









**Use Case Name:** Viewing Function

**Date:**



## Summary

write summary here



## Actors

actor 1
actor 2
….


## Preconditions

* precond 1

* precond 2

* ….



## Triggers

Explain trigger here



## Primary Sequence

step 1 action
step 2 action
etc


## Primary Postconditions

* postcondition

* postcondition

* etc



## Alternate Sequences

Only if you have alt seq

* Step 1 alt. seq.

* step 2 alt. seq.

* etc



### Alternate Trigger

### Alternate Postconditions



## Non-functional Requirements



## Glossary







**Use Case Name:** Logout Button

**Date:**



## Summary

write summary here



## Actors

actor 1
actor 2
….


## Preconditions

* precond 1

* precond 2

* ….



## Triggers

Explain trigger here



## Primary Sequence

step 1 action
step 2 action
etc


## Primary Postconditions

* postcondition

* postcondition

* etc



## Alternate Sequences

Only if you have alt seq

* Step 1 alt. seq.

* step 2 alt. seq.

* etc



### Alternate Trigger

### Alternate Postconditions



## Non-functional Requirements



## Glossary
