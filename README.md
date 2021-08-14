# [MS3-TravelCrowd]()

<Description>

<Showcase>
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

### As a user:



Documentation used:
https://flask.palletsprojects.com/en/2.0.x/quickstart/#a-minimal-application

Notes: change debug true to false before submitting!

Problem:
Had to import ssl and add as parameter ssl_cert_reqs=ssl.CERT_NONE to mongo, to connect to MongoDB

possibility to reuse the registration.html in home.html?


future feature: changing bg images.. atm too much to investigate (too time consuming)
--- 

For Logo: https://www.freelogodesign.org/

Images: https://unsplash.com/
Photo by Priscilla Du Preez on Unsplash 
Photo by Rumman Amin on Unsplash 

Photo by Artyom Manchenkov on Unsplash 
Photo by Štefan Štefančík on Unsplash 
Photo by frank mckenna on Unsplash 

For diagram(database): https://lucid.app/

https://www.befunky.com/create/ for image resize

- add credits for authentication scripts

add: @login required


Add favicon

Update Logo

Create deal form:
- update Period --> build script to get period automatically from start date + amount of days

padding in form

general styling of forms!!

change font (everywhere)

Make "created by"- session user :: show only own creted deals on profile

Testing for textareas --> eventually limit the amount of characters!

Check reuirements for username/password, it only says "match the reuirements, but not which requirements.

Make Home as starting page.

Placeholder for when there are no deals in my profile yet (newly registered user)

link to book einbauen

price & amount days: only int