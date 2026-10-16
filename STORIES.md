<markdown>
---
**User Story 1 : Browse the Katalog**
---        
    As a reader,
    I want to browse the catalogue of books
    so that I can discover books to read.

**Acceptance Criteria** 
    
    1.1 Katalog is selected when the website loads.
    1.2 The catalogue displays available books.
    1.3 Hovering over a book displays the favourite icon.

**Scenario**

    1. Open the "Läslistan" website
    2. Homepage should be displayed with title "Välkomman"
    3. "Katalog" button is selected by default
    4. List of books should be displayed
    5. Favorite icon is visible when use hovers over a book

**Expected Result:**

    - The website loads successfully.
    - Katalog is selected by default.
    - Books are displayed in the catalogue.
    - A heart icon appears when hovering over a book.

---
**User Story 2 : Manage favourite books(mina böcker)**
---
    As a reader,
    I want to add and remove the books to my favourites
    so that I can easily find them later.

**Acceptance Criteria** 

    2.1 A user can mark a book as favourite.
    2.2 A favourite book appears in Mina Böcker.
    2.3 A user can remove a favourite marking.
    2.4 Removed favourite books no longer appear in Mina Böcker.

**Scenario 2.1 : Add a favorite book**

    1. Katalog page is visible
    2. Click on the favorite icon
    3. Book should marked as favorite 
    4. Book should be displayed in "Mina Böcker"

**Expected Result:**

    - The selected book is marked as a favourite.
    - The book appears in Mina Böcker.
    - The favourite book counter increases by one (if displayed).

**Scenario 2.2 : Remove a book from favorite**

    1. Book is marked as favorite
    2. Click on the favorite icon
    3. The favorite icon removed from the book
    4. Book is removed from "Mina böcker" page

**Expected Result:**

    - The favourite marking is removed from the selected book.
    - The book no longer appears in Mina Böcker.
    - The favourite book counter decreases by one (if displayed).

___
**User Story 3: Add a new book**
---
    As a reader,
    I want to add a new book to the catalogue
    so that it becomes available to all users.

**Acceptance Criteria** 

    3.1 The user can enter a title.
    3.2 The user can enter an author.
    3.3 The user can add the book.
    3.4 The added book appears in the catalogue.

**Scenario**

    1. Clcik on " Lägg till bok" page
    2. Enter the tile
    3. Enter the Förfättare name
    4. Click "Lägg till ny bok"
    5. Book should be added and displayed in the "Katalog" page

**Expected Result:**

    - The book is added successfully.
    - The new book appears in the catalogue.
    - The total book count increases by one.
___
**User Story 4: View reading statistics**
---
    As a reader,
    I want to view statistics about the reading list
    so that I can understand the contents of the catalogue.

**Acceptance Criteria** 

    4.1 Statistik displays the total number of books.
    4.2 Statistik displays the total number of favourite books.
    4.3 Adding a book updates the total book count.
    4.4 Marking a book as favourite updates the favourite book count.

**Scenario 4.1 : View Statistik**

    1. Click on "Statistik"
    2. Total number of books should be listed 
    3. Total No.of. favorite books should be displayed

**Expected Result:**

    - The Statistics page displays the total number of books.
    - The Statistics page displays the total number of favourite books.

**Scenario 4.2 : Statistik view after adding a book**
    
    1. Click on "Statistik"
    2. Total number of books should be listed 
    3. Add a new book
    4. Book count in the "Statistik" page increased.

**Expected Result:**

    The total book count increases by one after a new book is added.


**Scenario 4.3 : Statistik view after marking a favorite**

    1. Click on "Statistik"
    2. Total number of books should be listed 
    3. Mark a book favorite
    4. Favorite book count on "Statistik" page increased.

**Expected Result:**

    The favourite book count increases by one after a book is marked as favourite.

___
**User Story 5: Navigate between pages**
---
    As a reader,
    I want to navigate between Katalog, Mina Böcker, Lägg Till Bok and Statistik
    so that I can access all features of the application.

**Acceptance Criteria**

    5.1 User can open Katalog.
    5.2 User can open Mina Böcker.
    5.3 User can open Lägg Till Bok.
    5.4 User can open Statistik.
    5.5 The correct page contents are displayed after navigation.

**Scenario :**

    1. Click on "Mina böcker"
    2. Mina böcker page is visible
    3. Click on "Lägg till bok"
    4. Lägg till bok page is visible
    5. Click on "Statistik"
    4. Statistik page is visible
    6. Click on "Katalog"
    7. Katalog pahe is visible

**Expected Result:**

    - The selected page is displayed correctly.
    - The corresponding page content is visible after navigation.
___
