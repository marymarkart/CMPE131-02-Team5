## Functional Requirements

1. Login 
2. Logout
3. Create new account
4. Delete account
5. Add to cart
6. Find items
7. Splash page
8. User profiles
9. Buy items
10. Add pictures for items
11. See all items
12. Add item to store


## Non-functional Requirements

1. UI iteractive interface
2. Expected to work on Chrome
3. Currency conversion support
4. Choice of order for listing items (Alphabetical, price, etc.)

## Use Cases

1. Add to cart
- **Pre-condition:** Item exists and is in stock on the cite.

- **Trigger:** User clicks on the "add to cart" button. 

- **Primary Sequence:**
  
  1. User clicks on an item of interest
  2. Clicks the "add to cart" button
  3. Item gets added to the user's shopping cart

- **Primary Postconditions:** Displays a popup window that asks if the user wishes to continue shopping or go to checkout

- **Alternate Sequence:** 
  
  1. User clicks "add to cart"
  2. Popup displays text saying the item selected is not in stock.
  3. Does not add anything to cart
  4. Returns to item page

2. Find item
- **Pre-Condition:** Items exist in the store and are properly tagged.
  
- **Trigger:** User clicks the search button.
  
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

3. Add item to store
- **Pre-Condition:** User has a profile
  
- **Trigger:** Clicks the "post new item" button.
  
- **Primary Sequence:** 

  1. User fills out: name, price, description, and tags for the item (required fields)
  2. Presses the "Post" button
  
- **Primary Postconditions:** Item gets posted on the cite and listed under the poster's profile
  
- **Alternate Sequence:** 

  1. User does not fill out all required fields when trying to post the item
  2. Popup indicates that the user still has fields to fill out
  3. Returns to the post new item screen
  
4. Buy items
- **Pre-Condition:** User has a profile and items exist in shopping cart.
  
- **Trigger:** User clicks on "Checkout" and proceeds to click "Buy".
  
- **Primary Sequence:** 
  
  1. User goes to the review shopping cart list page
  2. User buys all items in the shopping cart
  3. Goes to a screen confirming your purchase

- **Primary Postconditions:** All items in the shopping cart are purchased and deducted from the shop.
  
- **Alternate Sequence:**
  
  1. User clicks "cancel"
  2. Returns to the previous page

- **Alternate Sequence:**

  1. Card gets declined
  2. Asks user to entire a valid credit card (in this case a card that has a cash amount greater than or equal to the amount of cash needed)


=======
5. User Profiles
- **Pre-Condition:** User profile exists
  
- **Trigger:** User clicks on "Account and Lists"
  
- **Primary Sequence:** 
  
  1. User selects "Manage your profiles"
  2. User selects which profile they would like to view

- **Primary Postconditions:** User is redirected to a new page in which user details are shown
  
- **Alternate Sequence:** 

  1. User selects which profile to edit
  2. User is redirected to new page where user details can be edited
  3. User is redirected back to profile viewer
  
6. See all items
- **Pre-Condition:** Items exist and are in stock in the database.
  
- **Trigger:** User clicks the "View all" button.
  
- **Primary Sequence:** 

  1. "View all" is selected
  2. Returns the catalog for all items in the database in a grid pattern
  
- **Primary Postconditions:** A page displaying a limited amount of the database at a time is returned
  
- **Alternate Sequence:** 
  
  1. Nothing is in the database

=======
  2. Displays a message saying nothing is currently listed
