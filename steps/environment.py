from pages.create_account import create_account
from browser import Browser
from pages.sign_in_page import sign_in_page

def before_all(context):
    context.browser = Browser()
    context.create_account = create_account()
    context.sign_in_page = sign_in_page()

def after_all(context):
    context.browser.close()