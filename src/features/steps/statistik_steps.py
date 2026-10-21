from behave import given, when, then
from src.features.pages.katalog import CatalogPage
from src.features.pages.statistik import Statistic
from src.features.pages.add_book import AddBookPage


def initialize_pages(context):
    context.statistic = Statistic(context.page)
    context.addbook = AddBookPage(context.page)
    context.catalog = CatalogPage(context.page)


# scenario : View statistik
@given('the user opens Statistik')
@given('the current total book count is displayed')
@given('the current favourite book count is displayed')
def step_statistic_page(context):
    context.page.goto(context.base_url)
    initialize_pages(context)
    context.statistic.statistic_page()

    # Book_count
    context.book_count_before = context.statistic.get_book_count_stats_page()

    # Fav_book_count
    context.fav_book_count_before = (context.statistic
                                     .get_fav_book_count_stats_page())


@then('the total number of books should be displayed')
def step_verify_book_count(context):
    context.statistic.verify_total_book_count()


@then('the total number of favourite books should be displayed')
def step_verify_fav_count(context):
    context.statistic.verify_fav_book_count()


# Scenario - Statistik view after adding a book

@when('the user adds a new book with title "{title}" and author "{author}"')
def step_add_new_book(context, title, author):
    context.addbook.add_book()
    context.addbook.enter_title(title)
    context.addbook.enter_author(author)
    context.addbook.click_add_book()


@then('the total book count should increase by one')
def step_verify_book_count_after_add_book(context):
    context.statistic.statistic_page()
    book_count_after = context.statistic.get_book_count_stats_page()

    assert book_count_after == context.book_count_before + 1


# Scenario - Statistik view after marking a favorite

@when('the user marks a book as favourite')
def step_add_fav_book(context):
    context.catalog.click_catalog_btn()
    context.catalog.click_favorite_icon()


@then('the favourite book count should increase by one')
def step_verify_fav_book_count_after_add(context):
    context.statistic.statistic_page()
    fav_count_after = context.statistic.get_fav_book_count_stats_page()

    assert fav_count_after == context.fav_book_count_before + 1
