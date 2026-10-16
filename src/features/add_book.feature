Feature: Add a new book
  As a reader,
  I want to add a new book to the catalogue
  so that it becomes available to all users.
  
  Scenario: 
    Given the user is on the Lägg Till Bok page
    When the user enters a title
    And the user enters author name
    And clicks Lägg till ny bok
    Then Lägg till ny bok is disabled
    When user click katalog
    Then the added book should appear in the catalogue
    