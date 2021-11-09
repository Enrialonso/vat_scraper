from datetime import datetime as dt

from playwright.sync_api import Playwright, sync_playwright


def crawler(playwright: Playwright) -> None:
    path_file = dt.now().strftime("output_%Y_%m_%d_%H_%M.csv")

    browser = playwright.chromium.launch(headless=True)
    context = browser.new_context()
    page = context.new_page()
    with open('vat.txt', "r") as file:
        for line in file.readlines():
            line = line.replace('\n', '')
            flag = True
            while flag:
                try:
                    page.goto("https://www.vatsearch.co.za/vat-search")
                    page.wait_for_load_state("load")
                    page.click("[placeholder=\"10 Digit VAT Number\"]")
                    page.fill("[placeholder=\"10 Digit VAT Number\"]", line)
                    page.click("text=Perform Search", timeout=1000)
                    flag = False
                except Exception as error:
                    print(f"Reload web!!!")

            page.wait_for_load_state("load")
            with open(path_file, "a") as csv:
                try:
                    table_ok = page.query_selector("//*[@id='scrollToSearchResults']")
                    rows = table_ok.query_selector_all("//tbody")
                    for row in rows:
                        td = row.query_selector_all("td")
                        print(td[0].inner_text())
                        csv.write(f"{line};{td[0].inner_text()};\n")
                except Exception as error:
                    print("NO RESPONSE")
                    line = line.replace('\n', '')
                    csv.write(f"{line};NOT-FOUND;\n")

    context.close()
    browser.close()


def main():
    print("START CRAWLER")
    with sync_playwright() as playwright:
        crawler(playwright)


if __name__ == "__main__":
    main()
