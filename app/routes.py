from flask import render_template, flash, redirect, url_for, request, session
from flask_login import current_user, login_user
from flask_login import logout_user
from flask_login import login_required
from datetime import timedelta

from app import db

from app import myapp_obj
from app.forms import LoginForm, TaskForm, ListForm, EditForm

from app.models import User, Task, List

# different URL the app will implement
# @myapp_obj.route("/")
# # called view function
# def hello():
#     user = {'name' : 'Miguel (made with Dictionary)'}
#     posts = [
#         {
#             'author' : 'Linh',
#             'body' : 'Beautiful day in San Jose!'
#         },
#         {
#             'author': 'Emma',
#             'body' : 'I got my vaccine today!'
#         }
#     ]
#
#     return render_template('hello.html', user_template=user, posts=posts)
@myapp_obj.route("/base")
def base():
    return render_template('base.html')
@myapp_obj.route("/", methods=['GET', 'POST'])
def login():

    if current_user.is_authenticated:
        return redirect('/home')

    form = LoginForm()
    if form.validate_on_submit():
        # User.query.filter_by() returns a list from the User table
        # first() returns first element of the list
        # the form.username.data is getting the info the user submitted in the form
        user = User.query.filter_by(username=form.username.data).first()
        # if no user found or password for user incorrect
        # user.check_password() is a method in the User class
        if user is None or not user.password == form.password.data:
            flash('Invalid username or password')
            return redirect('/')
        # let flask_login library know what user logged int
        # it also means that their password was correct
        login_user(user, remember = form.remember_me.data)

        # return to page before user got asked to login
        # for example, if user tried to access a wedpage called profile, but since they
        # weren't logged in they would get redirected to login page. After they log in
        # the user will be redirected to their previous request, which would be the profile
        # page in this case.

        return redirect('/home')

    return render_template('login.html', title='Sign In', form=form)


@myapp_obj.route("/catemain")
def catemain():
    asset = []
    for l in List.query.filter_by(user = current_user):
        asset.append(l.category)
    return render_template('catemain.html', bset = set(asset))


@myapp_obj.route("/cate/<string:name>")
def cate(name):
    return render_template('category.html', cates = List.query.filter_by(category = name, user = current_user), na = name)


@myapp_obj.route("/home", methods=['GET', 'POST'])
def home():
    return render_template('home.html', title='Home')

@myapp_obj.route("/req")
# user needs to be logged in to see this page
# needs to be user route!
@login_required
# called view function
def req():
    return '''<html><body>
    User needs to be logged in
    </body>
    </html>'''

@myapp_obj.route("/register", methods=['GET', 'POST'])
def register():
    form = LoginForm()
    if form.validate_on_submit():

        user = User.query.filter_by(username=form.username.data).first()

        if user is None:
            new_user = User(username = form.username.data, password = form.password.data)
            db.session.add(new_user)
            db.session.commit()
            flash('Congratulations! You have been successfully registered as a user')
            return redirect('/')


        # return to page before user got asked to login
        # for example, if user tried to access a wedpage called profile, but since they
        # weren't logged in they would get redirected to login page. After they log in
        # the user will be redirected to their previous request, which would be the profile
        # page in this case.
        # next_page = request.args.get('next')
        # if not next_page or url_parse(next_page).netloc != '':
        #     next_page = url_for('index')
        #
        # return redirect(next_page)
        else:
            flash('username already taken, please try another username!')
    return render_template('register.html', title = 'Sign Up', form=form)

@myapp_obj.route("/inbox", methods=['GET', 'POST'])
def inbox():
    
    form = TaskForm()
    List.query.all()
    todo = List.query.filter_by(name = form.item.data).first()
    
    if form.validate_on_submit():
        
        if todo is None:
            flash('does not exist')
            return redirect('/inbox') 
            
        else:
            todo = todo
            return render_template('filter.html', title='Filter', form = form, todo = todo)
    return render_template('inbox.html', title='Inbox',  lists = List.query.filter_by(user=current_user), form = form, todo = todo)

# lists = []
@myapp_obj.route("/lists", methods=['GET', 'POST'])
def list():
    form = ListForm()
    if form.validate_on_submit():
        list_name = List.query.filter_by(name=form.list.data, user = current_user).first()

        if list_name is None:
            new_list = List(name=form.list.data, category = form.category.data, priority = form.priority.data, user = current_user)
            new_cat = Task(item=form.category.data, task_name = form.list.data, user =current_user)

            db.session.add(new_list)
            db.session.commit()

        # lists = List.query.filter_by(user=current_user)
        return redirect('/lists')
    return render_template('lists.html', title = 'List', form=form, lists = List.query.filter_by(user=current_user))

@myapp_obj.route("/delete/<string:task>")
def delete(task):
    task = List.query.filter_by(name = task, user = current_user).first()
    db.session.delete(task)
    db.session.commit()
    return redirect('/lists')



@myapp_obj.route("/edit/<string:task>", methods=['GET', 'POST'])
def edit(task):
    ta = List.query.filter_by(name = task, user = current_user).first()
    form = EditForm()
    if form.validate_on_submit():

        if form.rename.data != "" and form.changeCategory.data != "":
            ta.name = form.rename.data
            ta.category = form.changeCategory.data
            db.session.add(ta)
            db.session.commit()
        elif form.rename.data != "":
            # t = List(name = form.rename.data, category = ta.category, user = current_user)
            ta.name = form.rename.data
            db.session.add(ta)
            db.session.commit()
        elif form.changeCategory.data != "":
            # t = List(name = ta.name, category = form.changeCategory.data, user = current_user)
            ta.category = form.changeCategory.data
            db.session.add(ta)
            db.session.commit()
        else:
            return redirect('/lists')

        return redirect('/lists')



    return render_template('edit_task.html', form = form)

@myapp_obj.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect('/')
