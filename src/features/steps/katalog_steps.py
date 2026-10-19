from behave import given, when, then
from src.features.pages.katalog import CatalogPage


@given('the user opens the "Läslistan"')
def step_catalog_page(context):
    context.page.goto(context.base_url,
                      wait_until="domcontentloaded")
    context.catalogpage = CatalogPage(context.page)
    context.catalogpage.verify_reading_list_heading()


@then('home displayed with heading "Välkomman"')
def step_verify_heading_visible(context):
    context.catalogpage.verify_heading_visible()


@then('Katalog should be selected by default')
def step_catalog_selected_by_default(context):
    context.catalogpage.verify_catalog_selected_by_default()


@then('a list of books should be displayed')
def step_verify_book_list(context):
    context.catalogpage.verify_book_list()


@when('the user hovers over a book')
def step_verify_favorit_icon(context):
    context.catalogpage.mouse_hover()


@then('a favourite icon should be displayed')
def step_favorit_icon_display(context):
    context.catalogpage.favorit_icon_display()
