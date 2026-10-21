from behave import given, when, then
from playwright.sync_api import expect
from urllib3.util import timeout

from src.features.pages.add_book import AddBookPage
from src.features.pages.katalog import CatalogPage


@given('the user is on the Lägg Till Bok page')
def step_given_add_book(context):
    context.page.goto(context.base_url,
                      wait_until="load") 
    context.add_book_page = AddBookPage(context.page)
    context.add_book_page.add_book()


@when('the user enters a "{title}"')
def step_enter_title(context, title):
    context.add_book_page.enter_title(title)


@when('the user enters author name "{author}"')
def step_enter_author(context, author):
    context.add_book_page.enter_author(author)


@when('clicks Lägg till ny bok')
def step_click_add_book(context):
    context.add_book_page.click_add_book()


@then('Lägg till ny bok is disabled')
def step_verify_add_book_btn_disabled(context):
    context.add_book_page.add_btn_disabled()


@when('user click katalog')
def step_catalog_page(context):
    context.catalog = CatalogPage(context.page)
    context.catalog.click_catalog_btn()


@then('the added book "{title}" should appear in the catalogue')
def step_verify_book_added_catalog(context, title):
    expect(
        context.page.locator(".book")
        .filter(has_text=title)
    ).to_be_visible()
