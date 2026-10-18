### Reading List - Test Automation Project

**Overview**

This project is part of the **Test Aautomation with Python** examination. The purpose is to test the functionality of the Läslistan web application using Python, Playwright, Behave, and pytest.

The tests cover the applicaton's frontend and backend functionality. 
- The frontend tests use Behaviour-Driven Development (BDD) with Gherkin feature files and Behave step definitions. 
- The backend tests use pytest for unit and integration testing.

**Website under test:**

    https://tap-vt26-testautomatisering.github.io/exam/

___
**Technologies**
        
        - Python
        - Playwright – browser automation
        - Behave – BDD test framework
        - Gherkin – readable feature specifications
        - pytest – unit and integration testing
        - Flake8 – Python code style checking
        - Git and GitHub – version control
        - GitHub Actions – Continuous Integration (CI)
___
**Functionality Tested**

**Frontend – Behaviour-Driven Development (BDD)**
- The frontend is tested using Behave, Gherkin, and Playwright.The feature files describe user behaviour and the expected results of interactions with the website.

**The tests cover the following views:**
- Katalog: Viewing the book catalogue and interacting with books.
- Lägg till bok: Opening the add-book view and adding a book with a title and author.
- Mina böcker: Viewing and managing favourite books.
- Statistik: Viewing statistics about books and favourites.
- Navigation: Moving between the different views.

**In this project:**

- User stories describe the functionality from the user's perspective.
- Gherkin feature files describe expected behaviour using Feature, Scenario, Given, When, and Then.
- Behave matches the Gherkin steps with Python step definitions.
- Step definitions use Playwright and Page Objects to interact with the website.
- Assertions verify whether the application behaves as expected.
    
Page Objects are used to organize page interactions and locators separately from the step definitions.

**Backend – Unit and Integration Testing**

- The backend contains the BookStore and FavoriteBooks classes.
- Unit tests check individual methods and their expected behaviour. Integration tests check how the classes work together.

**The required methods are:**
        
        BookStore        
        - addBook(author, title)
        - toggleFavorite(book_id)
        
        FavoriteBooks        
        - add(book)
        - remove(book)

**Continuous Integration**

GitHub Actions is used to automate test execution when code is pushed to the configured branch.

**Documentation**
        
        - README.md – Project overview, test coverage, and execution instructions.
        - STORIES.md – User stories describing the application's functionality.
        - ANSWERS.md – Answers to the examination's theory questions.

**Installation and Run**

    1. Clone the project from GitHub - git clone "https://github.com/SriSri2617/PythonPlaywright_Exam.git"
    2. Navigate to the project directory cd PythonPlaywright_Exam
    3. On windows Powershell create virtual env - python -m venv .venv
    4. Activate the virtual env - .venv\Scripts\Activate.ps1
    5. Install the dependencies from requrements.txt - pip install -r Requirements.txt
    6. Run the backend test with - pytest
    7. Run the BDD test with - behave