Feature: Navigate between pages
  As a reader,
  I want to navigate between Katalog, Mina Böcker, Lägg Till Bok and Statistik
  so that I can access all features of the application.
  
  Scenario: 
    Given the user is on the website
    When the user clicks Mina Böcker
    Then the my books page should be displayed

    When the user clicks Lägg Till Bok
    Then the Add Book page should be displayed

    When the user clicks Statistik
    Then the Statistics page should be displayed

    When the user clicks Katalog
    Then the Catalogue page should be displayed
    