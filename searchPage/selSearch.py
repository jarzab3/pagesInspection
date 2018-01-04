from selenium import webdriver

chromeOptions = webdriver.ChromeOptions()
prefs = {"profile.managed_default_content_settings.images":2}
chromeOptions.add_experimental_option("prefs",prefs)

browser = webdriver.Chrome(chrome_options=chromeOptions)

# browser = webdriver.Chrome() #replace with .Firefox(), or with the browser of your choice

url = ""

browser.get(url)  # navigate to page behind login

a = browser.find_element_by_class_name("pink-btn")

a.click()

for i in range(1, 200, 1):

    url = url + i

    browser.get(url) #navigate to page behind login
    innerHTML = browser.execute_script("return document.body.innerHTML") #returns the inner HTML

    content = browser.find_elements_by_css_selector('div.username')

    for u in content:
        s = u.text

        if s.find("") == -1:
            pass
        else:
            print("Found on page " + str(i))

        print(u.text)

    # print(content)

# print(innerHTML)
