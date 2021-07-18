# django-crud
### setup 
run in your terminal :
1. `mkdir django-custom-user`
2. `cd django-custom-user`
3. `poetry init -n`
<!-- 4. `cd django_models` -->
4. `poetry add --dev black`
5. `poetry add django`
6. `poetry shell`

### create snacks_crud_project project:


 1. `django-admin startproject customUser .` 
          1. this command must write once
          2. (.) in the last very important, its means here 

### create snacks app
1. `python manage.py startapp accounts`
2. `python manage.py runserver`
>Note that we did not run migrate to configure our database. It's important to wait until after we've created our new custom user model before doing so.
## AbstractUser
### Custom User Model
1. update customUser/settings.py
   1. add the accounts app
      * Within INSTALLED_APPS add accounts at the bottom.
   2. use the AUTH_USER_MODEL config 
      * at the bottom of the entire file, add the AUTH_USER_MODEL config.
2. create a new CustomUser model
   1. account => models.py => import AbstractUser=> add class woth __str__ method
3. create new UserCreation and UserChangeForm
   1. `touch accounts/forms.py`
   2. import and add two calsses 
4. update the admin
   1. import and add class 
### create a new database that uses the custom user model.
1. `python manage.py makemigrations accounts`
2. `python manage.py migrate`
### Superuser
* run `python manage.py createsuperuser`
username : mohammad
email: mohammad@gmail.com
pass : mohammad123456789
### Templates/Views/URLs
1. updating settings.py to use a project-level templates directory.
    * TEMPLATES => `'DIRS': [str(BASE_DIR.joinpath('templates'))]`
2. Then set the redirect links for log in and log out, which will both go to our home template. Add these two lines at the bottom of the file.
3. Create a new project-level templates folder and within it a registration folder as that's where Django will look for the log in template. We will also put our signup.html template in there.
4. create four templates:
   1. templates/registration/login.html => add form 
   2. templates/registration/signup.html => add form 
   3. templates/base.html
   4. templates/home.html

5. Now for our urls.py files at the project and app level.
6. Create a urls.py file in the accounts app.
7. Last step is our views.py file in the accounts app which will contain our signup form.

run `python manage.py runserver`
### test part 
check this article https://learndjango.com/tutorials/django-testing-tutorial



### Github : 
 4. create EMPTY repository django-models on Github. Do NOT initialize with README, license or gitignore.
### connect Github with your local machine:
 2. `echo "# django-models" >> README.md
 2. git init
 12. git add README.md
 13. git commit -m "first commit"
 6. git branch -M main
 7. git remote add origin https://github.com/MohmmadNada/django-models.git
 8. git push -u origin main`
