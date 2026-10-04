
from playwright.sync_api import playwright, sync_playwright, expect, Page

def test_childframehandling(page:Page):
    page.goto("https://rahulshettyacademy.com/loginpagePractise/")

    with page.expect_popup() as child_page_info:
        page.locator("a").filter(has_text="Free Access to InterviewQues/ResumeAssistance/Material").click()
        child_page = child_page_info.value
        text= child_page.locator(".red").inner_text()
        print(text)

        ext_data = text.split("at")
        email = ext_data[1].strip().split(" ")[0]
        print(f"Email found: {email}")
        assert email == "mentor@rahulshettyacademy.com"

def test_UIautomation(page:Page):
    page.goto("https://rahulshettyacademy.com/AutomationPractice/")
    expect(page.get_by_placeholder("Hide/Show Example")).to_be_visible()
    page.get_by_role("button", name="Hide").click()
    expect(page.get_by_placeholder("Hide/Show Example")).to_be_hidden()
    page.wait_for_timeout(2000)
    #alerts handling
    page.on("dialog", lambda dialog: dialog.accept())
    page.get_by_role("button", name="Confirm").click()
    page.wait_for_timeout(5000)

    #Frames handling
    pageFrame = page.frame_locator("#courses-iframe")
    pageFrame.get_by_role("link", name="All Access plan").click()
    expect(pageFrame.locator("body")).to_contain_text("All Access plan")
    page.wait_for_timeout(5000)

    #hadling tables
    page.goto("https://rahulshettyacademy.com/seleniumPractise/#/offers")
    for index in range(page.locator("th").count()):
        if page.locator("th").nth(index).filter(has_text="Price").count() >0:
            priceColvalue = index
            print(f"price of the column is: {priceColvalue}")
            break
    rice_row = page.locator("tr").filter(has_text="Rice")
    print(f"Row value of rice is: {rice_row.locator('td').nth(priceColvalue).text_content()}")

    Potato_row = page.locator("tr").filter(has_text="Potato")
    print(f"ROw of the potato is : {Potato_row.locator("td").nth(priceColvalue).text_content()}")

    for index in range(page.locator("th").count()):
        if page.locator("th").nth(index).filter(has_text="Discount price").count() >0:
            discountNumber = index
            print(f"Discount price column number is: {discountNumber}")
    
            
    rice_row_dis = page.locator("tr").filter(has_text="Rice")
    print(f"Discount Price of rice is: {rice_row_dis.locator("td").nth(discountNumber).text_content()}")
