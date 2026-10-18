Feature: Manage favourite books (mina böcker)
  As a reader,
  I want to add books to my favourites
  so that I can easily find them later.
  
  Scenario: Add a favorite book
    Given the user is viewing the Katalog
    When the user clicks the favourite icon on a book
    Then the book should be marked as favourite
    And the book should appear in Mina Böcker
    
  Scenario: Remove a book from favorite
    Given a book is marked as favourite
    When the user clicks the favourite icon again
    Then the favourite marking should be removed
    And the book should no longer appear in Mina Böcker