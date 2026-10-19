from behave import given, when, then
from src.features.pages.katalog import CatalogPage
from src.features.pages.mina_bocker import MinaBocker

def step_up_catalog(context):
    context.page.goto(context.base_url, 
                      wait_until = "domcontentloaded")
    context.minabocker = MinaBocker(context.page)
    context.catalog = CatalogPage(context.page)
    context.catalog.view_catalog_page()
    

# Scenario : Add a favorite book
@given('the user is viewing the Katalog')
def step_view_katalog(context):
    step_up_catalog(context)
    


@when('the user clicks the favourite icon on a book')
@when(u'the user clicks the favourite icon again')
def step_select_favorit_book(context):
    context.catalog.click_favorite_icon()


@then('the book should be marked as favourite')
def step_verify_favorit_book_icon(context):
    context.catalog.favorit_icon_display()


@then('the book should appear in Mina Böcker')
def step_verify_mina_bocker_page(context):
    context.minabocker.mina_bocker_btn()
    context.minabocker.verify_mina_bocker_page()


# Scenario : Remove a book from favorite
@given('a book is marked as favourite')
def step_given_book_is_favorite(context):
    step_up_catalog(context)
    context.catalog.click_favorite_icon()


@then('the favourite marking should be removed')
def step_verify_favorit_icon_removed(context):
    context.catalog.verify_favorit_icon_removed()


@then('the book should no longer appear in Mina Böcker')
def step_book_removed_from_mina_bocker_page(context):
    context.minabocker.mina_bocker_btn()
    context.minabocker.verify_book_removed_mina_bocker_page()
