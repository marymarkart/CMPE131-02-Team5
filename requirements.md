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

1. Add to cart
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

2. Search item
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

3. User Profiles
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

4. Buy items
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

5. Items Page
- **Pre-Condition:** Items exist and are in stock in the database.
  
- **Trigger:** User clicks the "View all" button.
  
- **Primary Sequence:** 

  1. "View all" is selected
  2. Returns the catalog for all items in the database in a grid pattern
  
- **Primary Postconditions:** A page displaying a limited amount of the database at a time is returned
  
- **Alternate Sequence:** 
  
  1. Nothing is in the database
  2. Displays a message saying nothing is currently listed

6. Post Items to Store
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
