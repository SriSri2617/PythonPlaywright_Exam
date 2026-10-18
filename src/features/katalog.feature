Feature: Browse Katalog  
  As a reader,
  I want to browse the catalogue of books
  so that I can discover books to read.
  
  Scenario: 
    Given the user opens the "Läslistan"
    Then home displayed with heading "Välkomman"
    Then Katalog should be selected by default
    And a list of books should be displayed
    When the user hovers over a book
    Then a favourite icon should be displayed