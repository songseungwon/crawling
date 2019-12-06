import time
from selenium import webdriver

URL = "https://twitter.com/search?q={}&src=typd"
DRIVER_DIR = "/Users/swsong/test/chromedriver"

def twitter(keyword):
    driver = webdriver.Chrome(DRIVER_DIR)
    driver.implicitly_wait(10)
    driver.get(URL.format(str(keyword)))
    try:
        no_page = 0
        while no_page < 10:
            driver.execute_script('window.scrollTo(0, document.body.scrollHeight)')
            no_page += 1
            time.sleep(1.5)

        content = driver.find_elements_by_css_selector('div.content')
        print("content_length: ", len(content))
        for i in content:
            cont = i.find_element_by_css_selector('p.tweet-text')
            timestamp = i.find_element_by_css_selector('a.tweet-timestamp')
            print(str(cont.text).strip(), timestamp.get_attribute("title"))
            print('**********************************')
    except Exception as e:
        print(e)
    finally:
        driver.close()
if __name__ == "__main__":
    keyword = input('keyword : ')
    twitter(keyword)
