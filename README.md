[![Build Status](https://travis-ci.org/MatijaBas/rugby-shop.svg?branch=master)](https://travis-ci.org/MatijaBas/rugby-shop)

# [Rugby shop](https://rugby-shop.herokuapp.com/)

**This is my Milestone Project 4: Full Stack Frameworks with Django - Code Institute**
-----

## Table of Contents
1. [UX](#ux)
    - [Goals](#goals)
        - [Visitor Goals](#visitor-goals)
        - [Business Goals](#business-goals)
    - [User Stories](#user-stories)
    - [Design Choices](#design-choices)
    - [Wireframes](#wireframes)

2. [Features](#features)
    - [Existing Features](#existing-features)
        - [Header](#header)
        - [Navbar](#navbar)
        - [Footer](#footer)
        - [Home Page](#home-page)
        - [Products Page](#products-page)
            - [Product Details Page](#product-details-page)
        - [Reviews Page](#reviews-page)
        - [About Page](#about-page)
        - [Contact Page](#contact-page)
        - [Delivery Page](#delivery-page)
        - [Return Policy Page](#return-policy-page)
        - [Terms&Condition Page](#terms-condition-page)
        - [Register Page](#register-page)
        - [Login Page](#login-page)
        - [Profile Page](#profile-page)
        - [Checkout](#checkout)
            - [Cart Page](#cart-page)
            - [PaymentPage](#paymentt-page)
    - [Features for Future Releases](#features-for-future-releases)

3. [Information Architecture](#information-architecture)
    - [Database choice](#database-choice)
    - [Data Models](#data-models)
        - [User](#user)
        - [Products App Model](#products-app-model)
        - [Cart App Models](#cart-app-models)
        - [Accounts App Models](#accounts-app-models)
        - [Checkout app models](#checkout-app-models)

4. [Technologies Used](#technologies-used)
    - [Tools](#tools)
    - [Databases](#databases)
    - [Libraries](#libraries)
    - [Languages](#languages)

5. [Testing](#testing)
    - [Code Validation](#code-validation) 
    - [Manual Testing](#manual-testing)

6. [Deployment](#deployment)
    - [How to run this project locally](#how-to-run-this-project-locally)
    - [Heroku Deployment](#heroku-deployment)

7. [Credits](#credits)
    - [Content](#content)
    - [Images](#images)
    - [Code](#code)
    - [Acknowledgements](#acknowledgements)
    
8. [Contact](#contact)

***

<br/>

# Overview
[Rugby shop](https://rugby-shop.herokuapp.com/) was built and deployed by Matija Basanovic as his final project for 
the [Code Institute Full Stack Web Development Diploma](https://codeinstitute.net/). The project has been developed using [Django](https://www.djangoproject.com/), with the goal of 
fulfilling the requirements of the final, Full-Stack Milestone Project of the Code Institute Full-Stack Software Developer Course.
This page is made after a lot of thinking and negotiation with the man name Seamus who owns the shops.
The purpose of the Rugby shop online page is to help bussines owner Seamus to sell some of his products on line during lockdown in Ireland coused by global pandemic call COVID-19. Because all his 50 shops are closed now, this is the only way for Seamus to sell some products and try to save a company and try bussines to continue.

All images displayed in project are stored in an [AWS S3](https://aws.amazon.com/s3/) bucket, as are static files like CSS, icons and user-uploaded pictures.

The project is hosted at [Heroku](https://www.heroku.com/). A [Postgresql](https://www.postgresql.org/) database, also hosted at Heroku, is used to store image data and user data

# UX

## Goals

### Visitor Goals

The visitors that are targeted by Rugby Shop are:
- Professionals who are looking for good product for their team
- Amateurs that want to play a rugby in their favorite jersey
- People that want to get perfect birthay present
- People that are just bored becouse of COVID-19 and looking to spend some money

User goals are:
- Find a product that's gonna satisfied their needs 
- Buy from a trustworthy online shop.
- Show total price and number of items in cart.
- Be able to navigate the shop easily, find what I need and make a safe and secure purchase.


The online Rugby Shop is a great way to meet these needs because:
- The website has been designed to provide a clear view of product visitors are looking for.
- In navbar , visitors can find Home, Login and Register, Shop button with all products where they can search for specific product, Reviews and Cart
- Buyers can leave review if they are logged in

### Business Goals

The Goals of The Rugby Shop business are:
- Provide a professional online shop that helps the user to feel safe that they are buying from a trustworthy source. 
- Build brand awareness by including all the colors, fonts and logo associated with The Rugby Shop.
- Build Rugby Shop newsletter subscriptions.
- Fast and efficient delivery.
- Make sales of products easy for buyers to increase sales conversion.
- The presentation and layout of the site may not cause consternation, loss, or a desire to resign from shopping.

## User Stories

A Visitor to The Rugby Shop website  expects/wants/needs:

1. As a creative, mindful person I would rather buy products from local shop to support small local business owners with a personal touch, instead of buying products from big companies.

2. As new visitor I want ability to search through small amounts of information to find what I need, and then be able to easily click to get more detailed information.
As new customer I dont want to be confused by the layout or process of payment, and be able to easy find what i am looking for.

4. In order to avoid unawareness of purchase, I want product information must be sufficiently clear to understand.

5. A text search function so that I can quickly narrow down my search when looking for something specific.I need To be able to see a summary of my order on every page of the checkout process. When I am logged in I can access my account details and update them if I need to. 
I expect to be able to find information on my past orders. 
I expect to be able to easily get in contact with the shop owner via a contact form.

## Design Choices

The Rugby Shop website has a stylistic design with discrete and warm colors, inspiring images and simple buttons.

### Fonts
- The primary font [Merriweather](https://fonts.google.com/specimen/Merriweather?query=me) provides an artistic feeling, but are at the same time easy to read, which I think suits the purpose of the page and it´s audience.

My discrete & warm color design choices goes well together with the background image, and are listed here:

Color for the navbar | Color for the footer | Color for the New Collection carousel | Color for landing page | Color for about us text
--- | --- | --- | --- | ---
#ec7211 | #ec7211 | #4c2b22 | #f8f9fa | #1a251a

## Wireframes

Please click here to see all the [Wireframes](https://github.com/MatijaBas/rugby-shop/tree/master/wireframes) created.

# Features
 
## Existing Features

### Elements on every page

#### Navbar:

<div align="center">
    <img src="https://rugby-shop.s3-eu-west-1.amazonaws.com/static/img/navbar1.jpg" alt="Rugby Shop Navbar" aria-label="RugbyShop" />
</div>

- The navbar is top and fix , features on every page. RugbyShop logo on the far left which links to the home page of the site.

- Next to the logo is Home, Register and Login or Home, Profile and LogOut If user is loged in.

- In the middle of Navbar is name of the webpage so user know all the time where he is.

- On the right side of the navbar visitors can find links to Shop, reviews and cart

  -  The shopping cart counter works even for a user who is not logged in. This is because all the information about which products the user has added 
      to their cart is stored in their session data. This makes it possible for a new user to add things to their cart before being asked to log in or register. 
      This way user can add items to cart without registering, however when user will go to cart and will try to do checkout he/she will be directed to login/register page.
    
    - When user logs in a cart will remain with items picked as anonymous user.


<div align="center">
    <img src="https://rugby-shop.s3-eu-west-1.amazonaws.com/static/img/navbar-mobile.jpg" alt="Rugby Shop Navbar on mobile devices" aria-label="RugbyShop" />
</div>

- In mobile view logo is on left and the navigation bar changes to drop downtoggle with categories to choose from underneath logo.

***

<br/>

### Home Page

<br/>

<div align="center">
    <img src="https://rugby-shop.s3-eu-west-1.amazonaws.com/static/img/homepage.jpg" alt="Rugby Shop Homepage" aria-label="RugbyShop" />
</div>

<br/>

- The home page is welcoming users and ofering them a button to browse products, and underneath that is carousel with new collections

<br/>

#### About Us

<div align="center">
    <img src="https://rugby-shop.s3-eu-west-1.amazonaws.com/static/img/about_us1.jpg" alt="Rugby Shop About Us" aria-label="RugbyShop" />
</div>

- Text about how did shop start and little bit of history about Rugby Shop

<br/>

<div align="center">
    <img src="https://rugby-shop.s3-eu-west-1.amazonaws.com/static/img/about_us2.jpg" alt="Rugby Shop About Us" aria-label="RugbyShop" />
</div>

- Few pictures from first days, when shop was open, 
- Subscribe me form for users who are interested in exclusive offers

<br/>

