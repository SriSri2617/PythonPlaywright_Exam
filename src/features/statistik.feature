Feature: View reading statistics
  As a reader,
  I want to view statistics about the reading list
  so that I can understand the contents of the catalogue.
  
  Scenario: View Statistik
    Given the user opens Statistik
    Then the total number of books should be displayed
    And the total number of favourite books should be displayed
    
    
    
  Scenario:  Statistik view after adding a book    
    Given the current total book count is displayed
    When the user adds a new book with title "Test Automation Book" and author "John Smith"
    Then the total book count should increase by one
    
  
  Scenario: Statistik view after marking a favorite
     Given the current favourite book count is displayed
     When the user marks a book as favourite
     Then the favourite book count should increase by one
    