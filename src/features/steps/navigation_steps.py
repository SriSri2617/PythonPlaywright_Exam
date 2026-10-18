import re
from behave import *
from src.features.pages.katalog import CatalogPage
from src.features.pages.add_book import AddBookPage
from src.features.pages.mina_bocker import MinaBocker
from src.features.pages.statistik import Statistic


def initialize_pages(context):
    context.addbook = AddBookPage(context.page)
    context.catalog = CatalogPage(context.page)
    context.mina = MinaBocker(context.page)
    context.statistic = Statistic(context.page)


@given('the user is on the website')
def step_catalog_page(context):
    context.page.goto(context.base_url,
                      wait_until="domcontentloaded", timeout=30000)
    initialize_pages(context)
    context.catalog.view_catalog_page()


@when('the user clicks Mina Böcker')
def step_mina_bocker_page(context):
    context.mina.mina_bocker_btn()


@then('the my books page should be displayed')
def step_my_books_page_display(context):
    context.mina.verify_favorites_page_visible()


@when('the user clicks Lägg Till Bok')
def step_add_book_page(context):
    context.addbook.add_book()


@then('the Add Book page should be displayed')
def step_add_book_page_display(context):
    context.addbook.add_book_page()


@when('the user clicks Statistik')
def step_statistic_page(context):
    context.statistic.statistic_page()


@then('the Statistics page should be displayed')
def step_statistic_page_display(context):
    context.statistic.stats_page_display()


@when('the user clicks Katalog')
def step_catalog_page(context):
    context.catalog.click_catalog_btn()


@then('the Catalogue page should be displayed')
def step_catalog_page_display(context):
    context.catalog.view_catalog_page()
