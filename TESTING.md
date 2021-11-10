# Testing

# Table of Contents <a name="home"></a>
1. [Super User Details](#superuser)
2. [Validation Services](#validation)
3. [Errors/Warnings HTML](#html)
4. [Errors/Warnings CSS](#css)
5. [Errors/Warnings JS Hint](#js)
6. [Errors/Warnings PEP8](#pep8)
7. [Testing User Experience (UX)](#ux)
8. [Manual Testing](#manual)



# Super User Details <a name="superuser"></a>


Here are the superuser details for Ladeez Golf:

* username: emmad
* email: emmad@ladeezgolf.com
* password: CImilestone4



# Validation <a name="validation"></a>


* [W3C Markup Validation Service](https://validator.w3.org/) - Used to validate html

* [W3C CSS Validation Service](https://jigsaw.w3.org/css-validator/) - Used to validate CSS

* [JS Hint](https://jshint.com/) - Used to validate JavaScript

* [PEP8 Online Service](http://pep8online.com/) - Used to validate CSS


[Back to Testing](TESTING.md)



# Errors/Warnings HTML <a name="html"></a>


* Stray </a> tags found - Resolved by removing stray tags


[Back to Testing](TESTING.md)



# Errors/Warnings CSS <a name="css"></a>


* number missing unit - Resolved by adding px to number
* pm not recognised - Resolved by changing typo to px
* solis not recognised - Resolved by changing typo to solid


[Back to Testing](TESTING.md)



# Errors/Warnings JS Hint <a name="js"></a>


* 2 missing semi colons added - Resolved by adding missing semi colons


# Errors/Warnings PEP8 <a name="pep8"></a>


PEP8 showed a number of errors with length, white space and indentation. 

These have all been resolved by amending the length, removing white space amd correctly indenting code.

I had an issue after resolving PEP8 issues which meant that making lines shorter broke my webpage. 

I contacted tutor support and Sean helped me resolve the issue, this did mean some of my code isnt pep8 compliant in terms of length which I understand from Sean is okay according to python rules:

![Image](media/tutormessage.jpg)


[Back to Testing](TESTING.md)



# Testing User Experience (UX) <a name="ux"></a>


## As a Developer:

* As the developer, I want to create a website for the business owner to show their products 
    - All products are displayed clearly
* As the developer, I want the website to be aesthetically pleasing by making good use of HTML, CSS and Javascript 
    - The website has a consistant use of colours and styles with interative elements in appropriate places
* As the developer, I want the website to function in the intended ways and allowing purchasing of items, setting an account and leaving comments
    - The site has been manually tested and items can be purchased, you can create, amend and delet an account and users can leave comments on news stories

## As a Site Owner:

* As a site owner, I want to be able to add/edit and delete products on the site
    - The site has been manually tested and products can be added, edited and deleted correctly
* As a site owner, I want to be able to upload/edit news stories, and be able to delete news posts and approve comments
    - The site has been manually tested and New stories can be uploaded, amended and deleted. Comments can also be added and deleted.

## As a Site User:

* As a user, I want to easily browse through all products for sale
    - Products are easy to browse
* As a user, I want to view a specific category of products
    - Products can be viewed by category and sorted
* As a user, I want to search for a product using key words
    - There is a search bar at the top which will search for keywords in the website
* As a user, I want to view details of each product and see a clear image of the product
    - Each product has its own card which shows full details and a clearimage. The image can be clicked to show a larger version.
* As a user, I want to be able to choose the size of the product I want
    - There is an option to select a size
* As a user, I want to be able to add product/s to my shopping bag
    - Products can be added to the shopping bag and amended in the bag
* As a user, I want to be able to purchase items in my shopping bag
    - Users can checkout items in their shopping bag
* As a user, I want to create and sign in to my account
    - Users can create an account and sign in
* As a user, I want to read news relating to ladies golf
    - There is a news blog with stories on gold news 
* As a signed in user, I want to be able to save and update my delivery details
    - Users are able to save and update their delivery details in their account
* As a signed in user, I want to be able to comment golf news
    - Users can leave their comments on News stories


[Back to Testing](TESTING.md)

# Manual Testing <a name="manual"></a>


* Clicking logo takes user back to homepage
* Search bar tested using words in single/multiple items titles and descriptions and ensure it is returned to the user
* User icon tested to ensure that it reveals the correct dropdown for a user is logged in / logged out / logged in as superuser
    * If user is not logged in the dropdown reveals 'Register' and 'Login'

    
If user is logged in the dropdown has two options 'Logout' and 'Profile'
If user is logged in as superuser dropdown has options to 'Add a product', 'Add a blog post', 'Profile' and 'Logout'
All dropdown items were tested to ensure the user is brought to the correct page
Test cart icon to ensure it leads to the users Shopping Cart page
Test navigation links
'All Products' link leads to the Products page, displaying all products in all categories
'Shop by Room' dropdown gives users four options, allowing them to filter products by their room (category). Each option from dropdown leads the user to a page that only shows products in that room
'News' link leads the user to the news/blog page of the site
Navbar responsiveness was tested across small, medium, large and extra large screen sizes using Google Chrome dev tools



[ Back to Table of Contents](#home)