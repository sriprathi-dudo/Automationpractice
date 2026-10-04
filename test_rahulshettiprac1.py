
import time

from playwright.sync_api import Page, expect, Playwright

def test_UIvalidation(playwright:Playwright):
    browser = playwright.firefox.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://rahulshettyacademy.com/loginpagePractise/")
    page.get_by_label("Username:").fill("rahulshettyacademy")
    page.get_by_label("Password:").fill("Learning@830$3mK2")
    page.get_by_role("combobox").select_option("consult")
    page.locator("#terms").check()
    page.get_by_role("button", name="Sign In").click()
    #expect(page.get_by_text("Incorrect username/password.")).to_be_visible()
    iphone_locator= page.locator("app-card").filter(has_text="iphone X")
    iphone_locator.get_by_role("button",name="Add").click()
    nokia_locator= page.locator("app-card").filter(has_text="Nokia Edge")
    nokia_locator.get_by_role("button",name="Add").click()
    page.get_by_text("Checkout").click()
    expect(page.locator(".media-body")).to_have_count(2)
    page.wait_for_timeout(2000)

    count = page.locator(".media-body").count()

    for i in range(count):
        product_name = page.locator(".media-body").nth(i).locator("h4 a").text_content()
        print(f"Product {i+1}: {product_name}")

        #if product_name == "iphone X":
         #   price_text = page.locator(".media-body").nth(i).locator("storage:visible").text_content()
          #  print(f"Price of {product_name}: {price_text}")

    