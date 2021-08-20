# [MS3-TravelCrowd](http://travelcrowd.herokuapp.com/home)

TravelCrowd is a community platform to share the most amazing travel deals! "Sharing is caring" also (or especially?) counts for travelling! With hundreds of tour operators, an infinite amount of possibilities and for every possible price it is sometimes very hard to find the right trip. Frequent travellers and travel deal hunters know, that travelling does not have to be expensive and that everybody is able to see the world!
This platform is supposed to help out: A user simply has to register and can view travel deals that other members published. A user can also create, update and delete own deals.

![screenshot_showcase](readme-files/readme-images/showcase.png)


# Table of contents
- [UX](#ux)
    - [Website owner business goals](#website-owner-business-goals)
    - [User goals](#user-goals)
    - [User stories](#user-stories)
    - [Structure of the website](#structure-of-the-website)
    - [Wireframes](#wireframes)
    - [Surface](#surface)
- [Features](#features)
    - [Existing features](#existing-features)
    - [Features left to implement](#features-left-to-implement)
- [Technologies used](#technologies-used)
- [Code Validation](#code-validation)
- [Testing](#testing)
    - [Funcionality Testing](#functionality-testing)
    - [Compatibility Testing](#compatibility-testing)
    - [User stories testing](#user-stories-testing)
    - [Bugs and problems](#bugs-and-problems)
- [Deployment](#deployment)
- [Credits](#credits)


#  UX 

## Website owner business goals
- As the website owner, the goal is to provide a community platform to exchange travel deals.

## User goals
### Unregistered user
- User can register to the platform with a username and password

### Registered user
- Registered User can login to the platform with his/her username and password
- User can see all deals with details, that are published
- User can see his/her profile with all deals he/she created
- User can create a new deal
- User can read a deal
- User can update his/her created deal
- User can delete his/her created deal
- Can search for the name of a country or city to find matching deals


## User stories
### As a business owner:
- I offer a community platform to exchange spectacular travel deals.

### As a user:
- I want to see travel deals, that other people found and publish.
- I want to create and publish my own travel deals for the community.
- I want to update my own published travel deals.
- I want to delete my own travel deals.
- I want to search quickly for a deal about the country or city I am interested in.

## Structure of the website
TravelCrowd is a responsive website, therefore optimized for all devices and screen sizes (desktop, mobile and tablet). It is user friendly designed as it has an intuitive interface and is very descriptive. On the homepage a user can register and log in. When logged in, the user can see more features, like deals that were created by other users or creating a own deal. Furthermore the user has an own profile, in which there are only the deals this certain user created. At last the user has the option to log out.

## Wireframes
Wireframes can be found here: [WIREFRAMES](readme-files/wireframes/travelcrowd.pdf)

## Surface
### Fonts
The main font used is "Amatic SC" (by [Google Fonts](https://fonts.google.com/)) with a sans-serif backup. It is used mainly for all headlines (h1-h6), for the navigation and the items list in the deal. The secondary font is Open Sans, which is used to give some variety. It is mainly used in the footer and in paragraphs.

### Colors
- Fonts: Either black or white.
- Buttons: #00695c (Materializecss: teal darken-3) and #d81b60 (Materializecss pink darken-1).
- Footer: background-color of #00695c (Materializecss: teal darken-3) and font-color of white).
- white text has a text-shadow of rgba(0, 0, 0, 0.5).
- For some other parts of the page I used different shades of #009688 (Materializecss teal), to keep the colors consistent.

### Images
- Background image from [Unsplash](https://unsplash.com/).
- Icons from [Fontawesome](https://fontawesome.com/)

# Database Schema
I used one database (travel_crowd) with two collections (deals, users) in [MongoDB Atlas](https://www.mongodb.com/):
![Database Schema](readme-files/readme-images/travelcrowd_db_schema.png)


# Features

## Existing Features

### Navigation bar (header)
If the user is not logged in yet, the navigation bar shows:
Logo, Home, Login, Register
![screenshot_nav_logged_out](readme-files/readme-images/nav_logged_out.png)
If the user not logged in, the navigation bar shows:
Logo, Home, Deals, Profile, Logout
![screenshot_nav_logged_in](readme-files/readme-images/nav_logged_in.png)

### Home
For a user who is not logged in the homepage shows the registration form and two text boxes. The first text box should animate the user to sign up and the second explains what TravelCrowd is about.
![screenshot_home_logged_out](readme-files/readme-images/home_logged_out.png)

When a user registers, the home page is still visible, but only the text box that explains what TravelCrowd is, is shown.
![screenshot_home_logged_in](readme-files/readme-images/home_logged_in.png)

### Registration
User can register with an username and password (with an minimum length of 5 and maximum length of 15, pattern: ^[a-zA-Z0-9]{5,15}$). The registration form can be found on the homepage and in an extra navigation item in the header. If the user has already an account, there is a button in the registration form that can be used to go directly to the login page.
![screenshot_registration_form](readme-files/readme-images/registration_form.png)
![screenshot_registration](readme-files/readme-images/registration.png)

### Login
User can login with the username and password used in the registration process. The login form can be found in a dedicated navigation item in the header. If the user does not yet have an account, there is a button in the login form that leads the user directly to the registration form.
![screenshot_login_form](readme-files/readme-images/login_form.png)

### View Deals
When the user is logged in he/she can see all deals created by everyone in the community.
![screenshot_deals_collapsible](readme-files/readme-images/deals_collapsible.png)
![screenshot_deal_information_](readme-files/readme-images/deal_information.png)

### Search
In the search box, the user can search for country or city names to filter deals. A message appears, if there is no match.
![screenshot_search](readme-files/readme-images/deals_search.png)


### Profile
On the profile page, the user can see all deals he/she created. When there are no deals created yet, a message appears.
![screenshot_profile](readme-files/readme-images/profile.png)

### Create Deal
By clicking on the "Create Deal" button, either on the Profile page or on the Deals page, the user can create a deal. To do so, the user has to fill out a form. The form has required and non required items.
![screenshot_create_deal](readme-files/readme-images/create_deal.png)
![screenshot_create_deal](readme-files/readme-images/create_deal_2.png)
#### Those are the form elements:
- Deal name: required, maximum 30 characters.
- Destination country: required, uses an autocomplete form (from Materializecss) to show all possible countries (with flags), when start typing.
![screenshot_dropdown_countryflags](readme-files/readme-images/dropdown_countryflags.png)
- Destination city: required.
- Price: required, has to be a number.
- Description: not required.
- Departure airport: not required, uses a 3 characters IATA code and a pattern of [A-Za-z]{3}.
- Start date: required, select with a datepicker, start date can not be after the end date.
- End date: required, select with a datepicker, end date can not be before the start date.
![screenshot_datepicker_error_message](readme-files/readme-images/datepicker_error_message.png)
- Booking link: required, has to be an URL.

### Update Deal
When clicking on the "edit" button, the user is able to update the deal. All input fields are pre filled with the previous value. The user has a choice of a "cancel" and a "update" button.
![screenshot_edit_deal](readme-files/readme-images/edit_deal.png)
![screenshot_edit_deal](readme-files/readme-images/edit_deal_2.png)

### Delete Deal
The user can also delete a deal he/she created by clicking on the "delete" button. This will open first a modal, that asks for confirmation for deletion.
![screenshot_delete_modal](readme-files/readme-images/delete_modal.png)

### Logout
User can log out of the account on the logout navigation item in the header.

### Flash messages
- When the user tries to view anything, that can be only viewed when logged in. A user could for instance type the username in the url, but this should not be possible due to security reasons.
![screenshot_flash_not_allowed](readme-files/readme-images/flash_not_allowed.png)
- When the user registered successfully.
![screenshot_flash_registration](readme-files/readme-images/flash_registration.png)
- When the username is already taken (in registration process)
![screenshot_flash_username_already_exists](readme-files/readme-images/flash_username_already_exists.png)
- When the user logged out successfully.
![screenshot_flash_logged_out](readme-files/readme-images/flash_logged_out.png)
- When the username/password is wrong while trying to login.
![screenshot_flash_incorrect_usernam_pw](readme-files/readme-images/flash_incorrect_usernam_pw.png)
- When the user published (created) a deal successfully.
![screenshot_flash_deal_published](readme-files/readme-images/flash_deal_published.png)
- When the user updated a deal successfully.
![screenshot_flash_deal_updated](readme-files/readme-images/flash_deal_updated.png)
- When the user tries to update or delete a deal that was not created by him/her.
![screenshot_flash_not_allowed](readme-files/readme-images/flash_deal_updated.png)
- When the user deleted a deal created by him/her.
![screenshot_flash_deal_deleted](readme-files/readme-images/flash_deal_deleted.png)

### Modal
When the user wants to delete a deal, a modal will be shown, that asks for confirmation before finally deleting the deal.
![screenshot_delete_modal](readme-files/readme-images/delete_modal.png)

### Partials
In this project partials were used to write reusable code that can be easily included in other templates.


## Features left to implement:
- Categories: Add categories for the user to choose from and to search for (for instance "Family vacation", "Beach", "Mountains", etc.)
- Email Newsletter: A user can subscribe to the newsletter and receives updated per email when another member publishes as deal.
- Changing the background-image automatically: Having automatically changning background-images, that change on reload of the page. This is a source of inspiration and brings the user in a better travelling mood. Idea is similiar to [Bing](https://www.bing.com/).
- Liked-deals list: Option to save deals of others that a user likes and wants to review later without searching again for it.
- IATA code list: Autocomplete option for IATA code in the departure airport input field.


# Technologies used:

### Languages:
- [Python](https://www.python.org/): for backed logic
- [JavaScript](https://en.wikipedia.org/wiki/JavaScript): for interactivity on the website

- [HTML](https://en.wikipedia.org/wiki/Hypertext_Markup_Language): for structuring the website

### For styling:
- [CSS](https://en.wikipedia.org/wiki/Cascading_Style_Sheets): to write custom style for the HTML code
- [Materializecss](https://materializecss.com/): for responsiveness, styling and some functionality (collapsible, modal, datepicker, form etc.)
- [Fontawesome](https://fontawesome.com/): as an icon library
- [Google Fonts](https://fonts.google.com/): as a font resource
- [Material ](https://material.io/resources/color/#!/?view.left=1&view.right=1&primary.color=2e7d32&secondary.color=d32f2f)

### Frameworks and libraries:
- [Flask](https://en.wikipedia.org/wiki/Flask_(web_framework)): as a framework for Python
- [JQuery](https://jquery.com/): as a JavaScript library

### Planning
- [Balsamiq](https://balsamiq.com/): for creating wireframes
- [Lucidchart](https://www.lucidchart.com/): for drafting the database

### Testing
- [Am I responsive?](http://ami.responsivedesign.is/): for checking responsiveness on different screen sizes and using the screenshot taken from there as a showcase image for my projects readme.
- [Comparium](https://front.comparium.app/livetesting): For live testing on different browsers

### Miscellaneous:
- [Mongo DB Atlas](): for storing data in a database
- [Github](https://github.com/): for hosting the projects repository
- [Heroku](): for deploying the website
- [Visual Studio Code](https://code.visualstudio.com/): as a IDE (Integrated Development Environment) for developing the project
- [Git](https://en.wikipedia.org/wiki/Git): for version control

### Code validation
- [PEP8 checker](http://pep8online.com/): to validate Python code
- [JShint](https://jshint.com/) to validate JavaScript code
- [W3 CSS Validator](https://jigsaw.w3.org/css-validator/) to validate CSS code
- [W3 HTML Validator](https://validator.w3.org/) to validate HTML code


# Testing

## Functionality testing
For testing responsiveness, styling and interactivity I used for the project [Chrome Developer Tools](https://developers.google.com/web/tools/chrome-devtools).


--- 
# NEED TO DO TMR MORNING - Internet too slow
## Compatibility testing
The website was tested through virtual devices with Chrome Developer Tools.

Browsers tested: Google Chrome and Safari.

[Live testing with Comparium](https://front.comparium.app/livetesting)
- Windows 10 Chrome 89.0


- Windows 10 Firefox 85.0
- Windows 10 Edge 86.0
- Windows 10 Opera 74.0
- Linux Firefox 81.0
- Linux Chrome 87.0
- Linux Opera 72.0

Tested locally: 
- MacOs Catalina Google Chrome Version 90.0.4430.212 (Official Build) (x86_64)
- MacOs Catalina Safari Version 13.1.1 (15609.2.9.1.2)

The website was tested on following hardware devices:
- Macbook Air with MacOs Catalina (13-inch, 2017)
- Macbook Pro with MacOs Catalina (Retina, 15-inch, Mid 2015)
- Huawei P30 Pro with Android 10
- Google Pixel 4a (5G) with Android 11
- Microsoft Surface 7 Pro with Windows 10


## Performance testing with [Lighthouse](https://developers.google.com/web/tools/lighthouse)

Performance:
![lighthouse_performance](readme-files/readme-images/lighthouse_performance.png)

Accessibility score:
![lighthouse_accessibility](readme-files/readme-images/lighthouse_accessibility.png)

Best Practice & SEO:
![lighthouse_bestpractice_seo](readme-files/readme-images/lighthouse_bestpractice_seo.png)


## User stories testing
### As a business owner:
- I offer a community platform to exchange spectacular travel deals.
    > User can create and publish own deals and view deals of others.

### As a user:
- I want to see travel deals, that other people found and publish.
    > The user can view all travel deals created by others.
- I want to create and publish my own travel deals.
    > The user can create and publish own deals.
- I want to update my own published travel deals.
    > The user can update the travel deals created by him/her.
- I want to delete my own travel deals.
    > The user can delete the travel deals created by him/her.
- I want to search quickly for a deal about the country or city I am interested in.
    > The user can use the search to search for a country or city he/she is interested in.

## Bugs and problems
- check if works on heroku without ssl workaround (Had to import ssl and add as parameter ssl_cert_reqs=ssl.CERT_NONE to mongo, to connect to MongoDB)

- for countries in UK, the flags are not shown, - flags: scotland, northern ireland, england, wales: Delete countries and keep UK?
--> used GB as countrycode for all countries within the UK
- finding a bg image that fits to the topic and to the overall design/fonts

# Database
## [Mongo DB Atlas]()


# Deployment
## [Heroku]()
1. 

## [Local deployment](https://docs.github.com/en/github/creating-cloning-and-archiving-repositories/cloning-a-repository)
1. Go to repository
2. Click on the button "code"
3. Select the "HTTPS" option.
4. Copy the URL presented
5. Open your Terminal
6. Create a directory for storing this repository
7. Type "git clone" and paste the URL in that you previously copied
8. Press enter to create local clone repository

# Credits

## Content
- Content is written by me.

## Images
- Photo by <a href="https://unsplash.com/@sebaspenalambarri?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">Sebastian Pena Lambarri</a> on <a href="https://unsplash.com/s/photos/travel-sea?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">Unsplash</a>


## Problem solving helpers
- [w3schools.com](https://www.w3schools.com/)
- [MDN Web Docs](https://developer.mozilla.org/en-US/docs/Learn)
- [stackoverflow](https://stackoverflow.com/)
- [Materializecss documentation]()
- [Jinja documentation]()
- [Python documentation]()
- [Flask Documentation](https://flask.palletsprojects.com/en/2.0.x/)
- [Flask Login-required-decorator](https://flask.palletsprojects.com/en/2.0.x/patterns/viewdecorators/#login-required-decorator)
- [Shellhacks](https://www.shellhacks.com/jinja2-check-if-variable-empty-exists-defined-true/)
https://flask.palletsprojects.com/en/2.0.x/patterns/favicon/

## Code
- [Materializecss](https://materializecss.com/): for grid, form and styling of the website
- [Google Fonts](https://fonts.google.com/): for the fonts used
- [Fontawesome](https://fontawesome.com/): for the icons
- [Code Insitute Task Manager Mini Project](https://github.com/Code-Institute-Solutions/TaskManager): for the authentication
- [Stackoverflow](https://stackoverflow.com/questions/36556566/materialize-datepicker-prevent-end-date-before-start-date): how to prevent that end date is before start date, when using datepickers.

## Acknowledgments
- A big thank you to my mentor [Tim Nelson](https://github.com/TravelTimN), who not only gave me great tips and recommendations, but also motivated me extremely! Danke!!

- I also want to thank the Code Institutes Slack Community for reviewing my code and helping with small issues as well as motivation.


---------

Requirements questions:
- Design and implement manual test procedures to assess functionality, usability,
responsiveness and data management within the Full Stack web application

- Include functions with compound statements such as if conditions and/or loops in your
Python code

-Write code that meets minimum standards for readability (comments, indentation,
consistent and meaningful naming conventions).

-Name files consistently and descriptively, without spaces or capitalisation to allow for
cross-platform compatibility. 

-Design a data model that fits the purpose of the project 


WHATS LEFT to do:
- Add favicon -> [Realfavicongenerator](https://realfavicongenerator.net/): for generating the favicon

Last time help:
- lines to long (PEP8)

- background? text not readable everywhere
- any design idea for flashes?
- change order of collapsible

Last Notes:
- change debug true to false before submitting!
- check if works on heroku without ssl workaround (Had to import ssl and add as parameter ssl_cert_reqs=ssl.CERT_NONE to mongo, to connect to MongoDB)

/Applications/Python <YOUR PYTHON VERSION>/Install Certificates.command" open the 'Install Certificates.command' file.