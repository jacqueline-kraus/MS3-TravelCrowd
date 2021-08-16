# [MS3-TravelCrowd]()

<Description>

<Showcase>
--- 

WHATS LEFT:
- changing bg image automatically
- Add favicon -> [Realfavicongenerator](https://realfavicongenerator.net/): for generating the favicon
- update Period --> build script to get period automatically from start date + amount of days
- padding in form
- add: @login required
- Check reuirements for username/password, it only says "match the reuirements, but not which requirements.
- Placeholder for when there are no deals in my profile yet (newly registered user)

future feature:
- categories,
- email newsletter


MORE NOTES:
Documentation used:
https://flask.palletsprojects.com/en/2.0.x/quickstart/#a-minimal-application

Notes: change debug true to false before submitting!

Problem:
Had to import ssl and add as parameter ssl_cert_reqs=ssl.CERT_NONE to mongo, to connect to MongoDB



---
Credit for images:

Images: https://unsplash.com/
Photo by Priscilla Du Preez on Unsplash 
Photo by Rumman Amin on Unsplash 

Photo by Artyom Manchenkov on Unsplash 
Photo by Štefan Štefančík on Unsplash 
Photo by frank mckenna on Unsplash 

more tools used:
For diagram(database): https://lucid.app/

https://www.befunky.com/create/ for image resize


--- 

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
- User can see one deal with all details
- User can subscribe to the newsletter

### Registered user
- Registered User can login to the platform with his/her username and password
- User can see all deals with details, that are on the paltform
- User can see his/her profile with all deals he/she created
- User can create a new deal
    - User can read a deal
    - User can update his/her created deal
    - User can delete his/her created deal
- User can subscribe to the newsletter


## User stories
### As a business owner:
- I offer a community platform to exchange spectacular travel deals.
- 
### As a user:
- I want to see travel deals, that other people found and publish.
- I want to create and publish my own travel deals.
- I want to edit/update my own published travel deals.
- I want to delete my own travel deals.
- I want to be up to date with latest travel deals by receiving an email newsletter.



## Structure of the website

## Wireframes
Wireframes can be found here: [WIREFRAMES]()

## Surface
### Fonts

### Colors

### Images

# Features

## Existing Features


## Features left to implement:



# Technologies used:
- [Python](): 
- [Flask]():
- [HTML](https://en.wikipedia.org/wiki/Hypertext_Markup_Language): for structuring the website
- [CSS](https://en.wikipedia.org/wiki/Cascading_Style_Sheets): to style the HTML code
- [JavaScript](https://en.wikipedia.org/wiki/JavaScript): for interactivity on the website
- [JQuery](https://jquery.com/): as a JavaScript library
- [Materializecss](): 
- [Popper.js](https://getbootstrap.com/docs/4.6/getting-started/introduction/): required by bootstrap for some functionality to work
- [Fontawesome](https://fontawesome.com/): as an icon library
- [Google Fonts](https://fonts.google.com/): as a font resource
- [Balsamiq](https://balsamiq.com/): for creating wireframes

- [Am I responsive?](http://ami.responsivedesign.is/): for checking responsiveness on different screen sizes and using the screenshot taken from there as a mockup for my projects readme.
- [Comparium](https://front.comparium.app/livetesting): For live testing on different browsers


- [Mongo DB Atlas]():
- [Github](https://github.com/): for hosting the projects repository
- [Heroku]():
- [Visual Studio Code](https://code.visualstudio.com/): as a IDE (Integrated Development Environment) for developing the project
- [Git](https://en.wikipedia.org/wiki/Git): for version control



# Code Validation
- [JShint](https://jshint.com/) to validate JavaScript code
- [W3 CSS Validator](https://jigsaw.w3.org/css-validator/) to validate CSS code
- [W3 HTML Validator](https://validator.w3.org/) to validate HTML code

# Testing

## Functionality testing
For testing responsiveness, styling and interactivity I used for the project [Chrome Developer Tools](https://developers.google.com/web/tools/chrome-devtools).


--- 

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

Testing if fetch method is supported by all browsers with [https://caniuse.com/](https://caniuse.com/)
![Can I use?](readme-files/readme-images/Caniuse_fetch_screenshot.png)

## Performance testing with [Lighthouse](https://developers.google.com/web/tools/lighthouse)

Overall Scores:

![Lighthouse scores](readme-files/readme-images/lighthouse_scores.png)

Accessibility score (needs improvment):

![lighthouse accessibility score](readme-files/readme-images/lighthouse_accessibility_score.png)

---- 

## User stories testing
### As a business owner:
- I offer a community platform to exchange spectacular travel deals.
    > xxx.

### As a user:
- I want to see travel deals, that other people found and publish.
    > xxx.
- I want to create and publish my own travel deals.
    > xxx.
- I want to edit/update my own published travel deals.
    > xxx.
- I want to delete my own travel deals.
    > xxx.
- I want to be up to date with latest travel deals by receiving an email newsletter.
    > xxx.


## Bugs and problems 

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


## Problem solving helpers
- [w3schools.com](https://www.w3schools.com/)
- [MDN Web Docs](https://developer.mozilla.org/en-US/docs/Learn)
- [stackoverflow](https://stackoverflow.com/)
- [Materializecss documentation]()
- [Jinja documentation]()
- [Python documentation]()

## Code
- [Materializecss](): for grid, form and styling of the website
- [Google Fonts](https://fonts.google.com/): for the fonts used
- [Fontawesome](https://fontawesome.com/): for the icons
- Code Insitute Task Manager Mini Project(): for the authentication

## Acknowledgments
