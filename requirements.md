## Functional Requirements

1. Login
2. Logout
3. Create new account
4. Delete account
5. Add to cart
6. Search Items
7. Splash page
8. User profiles
9. Buy items
10. Add pictures for items
11. Items Page
12. Post Items to Store

## Non-functional Requirements

1. UI iteractive interface
2. Expected to work on Chrome
3. Currency conversion support
4. Choice of order for listing items (Alphabetical, price, etc.)

## Use Cases

1. Login 
- **Pre-condition:** User needs to have an existing account in the database

- **Trigger:** User clicks on the Login Button on the navbar

- **Primary Sequence:**
  1. User clicks on Login on the navbar
  2. User enters email and password to login their account

- **Primary Postconditions:** User is logged into their account has access to the logged in features

- **Alternate Sequence:** 
  1. User tries to login
  2. Website tells user they dont have an account or entered wrong

2. Logout
- **Pre-condition:** User needs to be logged into an account

- **Trigger:** User clicks on logout on the navbar

- **Primary Sequence:**
  1. User clicks on logout on the top right button of the navbar

- **Primary Postconditions:** User is logged out of their account and dont have access to their profile or cart

- **Alternate Sequence:** 
  1. User clicks on the logout button on the navbar
  2. User is logged out of their account and does not have access to profile or cart


3. Create new account
- **Pre-condition:** User does not need preconditions

- **Trigger:** User clicks on the SignUp button on the navbar

- **Primary Sequence:**
  1. User clicks on the SignUp button
  2. User needs to enter username
  3. User needs to enter email address
  4. User needs to enter a password
  5. User needs to re-enter a password

- **Primary Postconditions:** Users information is sored into the database and is redirected to the login page where they can enter their account 

- **Alternate Sequence:** 
  1. User clicks on SignUp
  2. User leaves the account name empty
  3. The website tells the user to enter a field

- **Alternate Sequence:** 
  1. User clicks on SignUp
  2. User tries to use a username already taken by another user
  3. The website tells the user to enter a different username because it's been taken

4. Delete account
- **Pre-condition:** The user has an account

- **Trigger:** User clicks on Delete Account button in Account

- **Primary Sequence:**
  1. User clicks on the Account Button on the navbar
  2. User clicks on the Delete Account Button on the bottom of the account information

- **Primary Postconditions:** The users posts are found in the database and all deleted. Finally the users information is deleted from the database

5. Add to cart
- **Pre-condition:** Item exists and is on the items page.

- **Trigger:** User clicks on the items post and clicks on the "add to cart" button. 

- **Primary Sequence:**
  1. User clicks on an item of interest
  2. Clicks the "add to cart" button
  3. Item gets added to the user's shopping cart

- **Primary Postconditions:** The item is added to the current users cart and can be accessed ont hr cart button in the navbar.

- **Alternate Sequence:** 
  1. User clicks "add to cart"
  2. Popup displays text saying the item selected is not in stock.
  3. Does not add anything to cart
  4. Returns to item page

6. Search item
- **Pre-Condition:** Item post exists in the store.
  
- **Trigger:** User enters the items name in the search bar and clicks the search button.
  
- **Primary Sequence:**
  1. User types into the search bar
  2. The search button is clicked
  
- **Primary Postconditions:** Returns the page of the item the user searched for
  
- **Alternate Sequence:**
  1. User clicks off of the search bar
  2. Search bar returns to it's previous orientation, minimized

- **Alternate Sequence:**
  1. Searches the database for item but returns nothing
  2. Displays a screen saying the item the user searched for doesn't exist

7. Splash Page 
- **Pre-condition:** User does not need an account to view splashpage

- **Trigger:** Clicks on any button on the navbar to view the different pages

- **Primary Sequence:**
  1. User clicks on the website home page to view home
  2. User clicks on the About button to view the About page
  3. User clicks on the Items button to view the item posts

- **Primary Postconditions:** User is navigated to the splash page of the button clicked

- **Alternate Sequence:** 
  1. User clicks on Reebay button to be greeted to the website

- **Alternate Sequence:** 
  1. User clicks on About button to get information about the Reebay Website

- **Alternate Sequence:**
  1. User clicks on Items button to view all items posted by other users
  
8. User Profiles
- **Pre-Condition:** User is logged in
  
- **Trigger:** User clicks on "Account on the navbar
  
- **Primary Sequence:**
  1. User Account button
  2. User uploads an image to change profile
  3. User selects Update to update account information

- **Primary Postconditions:** Users profile is updated with new profile image and is saved to the database
  
- **Alternate Sequence:**
  1. User clicks on the Items button for the Items page
  2. User clicks on sellers profile picture or profile name
  3. User is redirected to sellers profile to view all their posts

9. Buy items
- **Pre-Condition:** User has a profile and items exist in shopping cart.
  
- **Trigger:** User clicks on "Checkout" and clicks on "Buy Now.
  
- **Primary Sequence:** 
  1. User goes to the Cart button on navbar
  2. User clicks on checkout to see total cost
  3. User clicks on Buy Now and is taken to the stripe page to buy the item

- **Primary Postconditions:** The item is bought and is taken to the thank you for your purchase page.
  
- **Alternate Sequence:**
  1. User clicks on "remove item" from cart
  2. Removes the item from the cart

- **Alternate Sequence:**
  1. Card gets declined from stripe
  2. Asks user to entire a valid credit card

10. Add Pictures for Items 
- **Pre-condition:** User needs to have an account and be logged in

- **Trigger:** User clicks on the sell button and is able to upload an image

- **Primary Sequence:**
  1. User is logged into their account
  2. User clicks on the sell button
  3. User uploads an image to the post
  4. User posts the item clicking the post button

- **Primary Postconditions:** The users item is posted with the picture and information on a card for the Items page.

- **Alternate Sequence:** 
  1. User forgets to upload an image
  2. The post is still uploaded and uses the default image
  3. The user goes to their post on the Items page and clicks on update
  4. The user uplaods an image to the post and clicks on update to update the post.
  
11. Items Page
- **Pre-Condition:** Items exist and are in stock in the database.
  
- **Trigger:** User clicks the "View all" button.
  
- **Primary Sequence:** 

  1. "View all" is selected
  2. Returns the catalog for all items in the database in a grid pattern
  
- **Primary Postconditions:** A page displaying a limited amount of the database at a time is returned
  
- **Alternate Sequence:** 
  
  1. Nothing is in the database

  2. Displays a message saying nothing is currently listed

12. Post Items to Store
- **Pre-Condition:** User has a profile and is logged in
  
- **Trigger:** Clicks the "post new item" button.
  
- **Primary Sequence:** 
  1. User fills out: name of item, description of item, price of item and an image for the item (all required except image)
  2. Presses the "Post" button
  
- **Primary Postconditions:** Item gets posted on the cite and listed under the poster's profile. If the post did not have an image, use the default item image instead.
  
- **Alternate Sequence:** 
  1. User does not fill out all required fields when trying to post the item
  2. Popup indicates that the user still has fields to fill out
  3. Returns to the post new item screen
  4. User can update the post at any time to add more discription or an item image.
