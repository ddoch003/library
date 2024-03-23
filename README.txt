Libraria 20

Project overview:
This project is created as Django Advanced final project. It gathers a small part of the greatest 20th century literature classics.
Every book instance contains information about the book itself, it's author, year published and the genres it can be associated with.
Authors are also created as model instances and every author instance contains info about the author like the author's lifespan, nationality, gender, bio and the book in the shelf associated with the particular author.
Once a user is registered the user can add a book instance to favorites.
There is a search functionality that allows the users to search for books and authors.
The user can also access the blog page. Here the user can create blog posts and leave comments under every post.

User Management:
The superuser has got unlimited permissions to create, modify and delete other users.
The superuser can create, modify and delete book and author instances over both Django admin portal and application itself.
This functionality is unavailable for regular users not only by restricting the visual representation of these functionality and the links they lead to in the template, but also by adding UserPassesTestMixin in the views that checks if the user is a superadmin.
If not the page displays "403 Forbidden". The user model is defined by overriding the AbstractBaseUser Django model and also by inheriting from PermissionsMixin.

The regular user uses the email field as username and in addition to that the registration form prompts the user to enter their birth date in format "YYYY-MM-DD". 
The birtdate checks if the user is at least 12 years old by the date of registration. The user has the possibility to update the profile details once signed in (first name, last name, profile picture). 
The application welcomes the user either by username which is taken by splitting the email address to username and domain name or by first name if it exists.

*** As a profile is not created for superuser this functionality is not visible and accessible by the superuser.

The user can access their account info by clicking on the circle on the top right side of the screen which either shows the profile picture of the user if one is present or a default image. 
A simple JavaScript was written to show and hide the profile panel on click. 
Beside the profile details the user can also change the password and logout. 
The most important restriction added is to prevent a user to update another user's profile by hitting the url that will lead to the profile edit page of another user. 
This was blocked by adding UserPassesTestMixin which checks if the pk of the logged in user is the same like the one that the user tries to override. 
If not 403 Forbidden is displayed. 

A staff user is explicitely granted with staff permissions by an admin manually. In addition the staff user can be manually added to the blog staff group and this user can delete blog posts and comments if they violate the terms of use.

When the password is changed the user is redirected to the home page again and there appears a confirmation message from django.contrib.
There is also a feature that allows the user to reset the password in case the user does not remember it.
I am very proud of myself that I managed to configure this functionality to work properly. :)

Home page:
Once the user is signed in the home page changes the background and welcomes the user either by username or first name if one. 
The home page contains a navbar with the most important links of the app. The genre link extends on hover and shows all book genres (a django model). 
This is achieved by a simple JavaScript. 
Each genre leads to a page that contains all books associated with a particular genre.
The home page also picks up 3 random book instances every time when loaded. Below them there is a link to access the whole library.
*** If there are no books added yet - no books are displayed. If there are less than three books in the DB - all existing books are shown.

Book:
As mentioned in the beginning the book model contains the information about the book instances. 
The book form validates if a book with such title already exists both with creating an instance or updating it.
The save method was overriden in order to lower and then capitalize each word in the title.
Each book gotta be published between 1900 and 1999 and there is a validator applied with simple django.core.validators. 
Multiple genres can be associated with a particular book. 
As already mentioned a book instance can be edited only by a superadmin - access restricted for regular users. 
The book instance can also be deleted by a superadmin and before the post request the admin is redirected to a DeleteView that asks if the user is aware of the fact that this book will be deleted. 
There is also a link for the author's detail page accessible by clicking on the author's name.
Books list is accessible withour login. However in order a user to reach the book details the user needs to create a registration and to login.
A Book instance can be added to the user's favorite books and removed from the list as well - How? - Black magic! 
Just joking. As there is a ManyToMany field favorite_books in the Profile model that establishes the connection between user profiles and book instances there is a form in the book-details.html template that checks if the signed user has added the book to their fav books and displays Add to Favorites/Remove from Favorites button. Then the view AddToFavoriteView and the overriden post method takes care of adding or removing the book to/from the user's fav books.

Author:
An author instance is also created, updated and deleted only by a superuser. 
The access to these functionalities is also restricted with the same method already described. 
Author's details page shows the authors name, life span, gender, nationality, short bio and below the info card - the books associated with this author. 
When the author is deleted all book instances associated with this author remain in the library with an unknown author (on_delete=models.SET_NULL).

Blog:
The blog page allows users to add blog posts. A login is requiered in order to access the blog page.
Each user can edit and delete thier own blogposts.
As already mentioned the admins and the staff users can act as blog content reviewers and delete posts and comments.
Editing and deleting other people's posts is restricted not only by visibility applied in the template but also by UserPassesTestMixin restriction which checks if the signed user is the author of the post and prevents hacking by hitting the url.
A user can add a comment to a blogpost. Unfortunately the possibility to edit or delete a comment is not available through the app. The admnins and the staff users can delete inappropriate comments over the Django admin portal.
