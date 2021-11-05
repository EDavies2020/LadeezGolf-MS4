# Gluten Free Kids Website


![Image]()

[View live project here]()

This website has been created for my full stack milestone project. 

The site created is a fictional e-commerce womens golf shop buisness, I chose this as a female golfer myself. Customers can browe products and purchase if they choose to do so. They can set up an account and follow female golf news.


# Table of Contents <a name="home"></a>

1. [Introduction](#Introduction)
2. [User Experience (UX)](#UX)
3. [Design](#Design)
4. [Wireframes](#Wirefames)
5. [Features](#Features)
6. [Technologies Used](#Technologies)
7. [Testing](#Testing)
8. [Deployment](#Deployment)
9. [Cloning Repository](#Cloning)
10. [Credits](#Credits)

# Introduction <a name="introduction"></a>


## Website Purpose :

* This website is for customers interested in buying womens golf products
* Customers want to be able to browse through products and make a purchase
* The simple, intuative layout of the site allows users to easily add items to their bag and make purchases


[ Back to Table of Contents](#home)


# User Experience (UX) <a name="UX"></a>


## As a Developer:

* As the developer, I want to create a website for the business owner to show their products
* As the developer, I want the website to be aesthetically pleasing by making good use of HTML, CSS and Javascript 
* As the developer, I want the website to function in the intended ways and allowing purchasing of items, setting an account and leaving comments

## As a Site Owner:

* As a site owner, I want to be able to add/edit and delete products on the site
* As a site owner, I want to be able to upload/edit news stories, and be able to delete news posts and approve comments

## As a Site User:

* As a user, I want to easily browse through all products for sale
* As a user, I want to view a specific category of products
* As a user, I want to search for a product using key words
* As a user, I want to view details of each product and see a clear image of the product
* As a user, I want to be able to choose the size of the product I want
* As a user, I want to be able to add product/s to my shopping bag
* As a user, I want to be able to purchase items in my shopping bag
* As a user, I want to create and sign in to my account
* As a user, I want to read news relating to ladies golf
* As a signed in user, I want to be able to save and update my delivery details
* As a signed in user, I want to be able to comment golf news


[ Back to Table of Contents](#home)


# Wireframes <a name="Wireframes"></a>


* Homepage 
* Products Page 
* New page


[ Back to Table of Contents](#home)


# Design <a name="Design"></a>


## Colours:

* I used Black, white and grey to keep the site simple and clear to all
* I used rgb(184, 33, 91) which is a dark pink/red as a nod to the site being aimed at women
* I used Recursive font as it is clear to read and modern 

## Images:

* All non-recipe images were chosen because they were relevant to womens golf 
* Non-product Images were sourced from [unspalsh](https://unsplash.com/) and [pixabay](https://pixabay.com/)
* Product images were sourced from [American Golf](https://www.americangolf.co.uk) and [Golf Online](https://www.golfonline.co.uk)
* News images & stoies came from google searches for womens golf news
 

## Favicon: 
* I used [Jimdo](https://www.jimdo.com/) to create my company logo and then used [favicon.io](https://favicon.io/) to convert my logo into a favicon


[ Back to Table of Contents](#home)


# Features <a name="Features"></a>


## Navbar/Footer

* The navbar is fixed on all pages and came from Bootstrap 
* The navbar features the company logo to the left 
* The navbar switches to a sidebar on smaller screens 
* Certain links are only visible for registered users
* The navbar and footer share the same colour scheme
* The footer has links to social media.<br><b>Note:</b> these links are for the pages main sites as this is a fabricated company


## Homepage

* There is a fixed image on the homepage with a 'Shop Now' Button which takes the user to all products
* There is a search bar for searching all products
* There are buttons for searching by category/price and viewing News articles
* There is a My account button which for non registered directs the user to sign up and for registered users directs to their order history and account details which can be updated
* There is a bag icon which takes the user to their shopping bag


## Products Page/s

* Easily accesible by selecting the 'Products' or another option from the navbar
* All Products page shows the user all items available
* Each product is displayed in a card showing an image of the product, the product name, and the price and its category type
* The product image being clicked will reveal more product details


## Product Details Pages

* There are Individual pages for each product to show more details
* This includes the product name, product image, price of product, product size selection (where relevant) and product description
* The user has the option of selecting the quantity they would like to purchase
* The user then has the option to add this quantity of the item to their bag or return to shopping


## Shopping Bag

* Accessed by selecting the bag icon from the navbar
* The user can view items aded to their bag and the total of the goods added
* The user has the option of updating the quantity, or removing the item from their bag
* Two buttons at the bottom of the page allow the user to either 'Keep shopping' or move forward to the 'Checkout' page
* A message displays to show how much more the user needs to spend to qualify for free delivery


## Checkout

* The order summary includes a breakdown of the order including delivery price if applicable 
* The checkout form will pull through the users profile information if they are logged in, if they are registered
* The Form requires the users name, email address, shippping details and payment details to complete the purchase
* The user can either 'Adjust cart' if they need to make changes to their order before purchasing or 'Pay now' to complete the order


## Checkout Success

* A 'timer' will appear to let the user know the transaction is processing
* They will then be taken to a page to let them know their purchase has been successful
* This page contains the order information, including unique order number, delivery details and billing information
* There is a back to shop button at the end of this information


## Log in / register functionality

* A user who is not logged in will have the option to 'Login' or 'Register' from the Profile icon on the navbar
* Django allauth was used for account management
* If user selects to 'Register' they are taken to a registration page which asks for their email address, and prompts to create a username and password
* The user will recieve a email to verify their account
* If the user selects to login they will be asked to enter their username and password


## Account

* A logged in user can access their account page from the profuile icon in the navbar
* The Account page shows the users default information and the users order history
* The default information can be updated by the user
* The order history shows a bteakdown of all orders with basic information showing
* In The order history column the user can click the order number which takes the user to the order confirmation for that order


## Toasts
* Bootstrap toasts were used to assure the user of their actions throughout their journey - Letting them know when an item was added/removed from their bag, if their order was succesfull, if they are logged in or logged out.
* Toasts were also used to show users what had been added to their bag and how much to get free delivery in a 'mini' shopping bag format


## Golf News
* Admin can update the news feed with new gold related stories
* Logged in users can comment on news posts
* Admin have the option of adding, editing and deleting news posts
* Logged in users have the option to add comments to news posts


## Admin / Superuser
* When a user is logged in as Admin/Superuser they will have different functionality to a regular user
* When they select the Profile icon from the navbar they will have the options to Add a News post, Add a Product
* If they select to add a product, they will be taken to a page to fill out a form and add a product
* If they select to add a news post, they will be taken to a page to fill out a form and add a news post 


[ Back to Table of Contents](#home)


# Technologies <a name="Technologies"></a>


1. Languages used: HTML5, CSS3, JQuery, Javascript,  Python and Jinja and Django framework was used to build the application

2. [GitHub](https://github.com/) 
    * My project code is stored in GitHub

3. [Git](https://gitpod.io/workspaces/) 
    * Git was used for version control, code created in GitPod was committed and pushed to GitHub

4. [unspalsh](https://unsplash.com/), [pixabay](https://pixabay.com/)
    * Used for images throughout the site

5. [Jimdo](https://www.jimdo.com/),
    * Used to create my company logos

6. [favicon.io](https://favicon.io/), 
    * Used to create my favicon
    
7. [FontAwesome](https://fontawesome.com/) 
    * Font Awesome icons were used throughout the site

8. [Bootstrap](https://getbootstrap.com/)
    * Used for product cards, forms, navbar, side nav, footer 

9. [Heroku](https://heroku.com/)
    * Used to deploy this repository

10. [Stripe](https://stripe.com/en-gb) 
    * Used for payments



[ Back to Table of Contents](#home)


# Testing <a name="Testing"></a>


Testing can be found here: [TESTING.md](TESTING.md)


[ Back to Table of Contents](#home)


# Deployment <a name="Deployment"></a>




[ Back to Table of Contents](#home)


# Cloning <a name="Cloning"></a>




* When it shows as done your files will be cloned to your desktop


[ Back to Table of Contents](#home)


# Credits <a name="Credits"></a>


## Code

* [Blog Tutrial](https://djangocentral.com/building-a-blog-application-with-django/)
    * News app was created using this tutorial

* Code Institute
    * Django Module, Boutique Ado Mini Project

* Slack Community
    * Thread found on adding 404.html


## Media

* All images were sourced from the following sites: [unspalsh](https://unsplash.com/), [pixabay](https://pixabay.com/), [American Golf](https://www.americangolf.co.uk) and [Golf Online](https://www.golfonline.co.uk)
* News images & stoies came from google searches for womens golf news

## Acknowledgements

A big thank you to the following: 

* Tutor support for helping me with issues I had during the course/project
* My wonderfully supportive family for being understanding when I am glued to my laptop for hours on end
* The Slack community for sharing problems you come across and helpful fixes offered
* The encouragement from other students Ive connected with during my time on the course, it is a great support network 




[ Back to Table of Contents](#home)