from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

SEARCH_URL = "https://www.facebook.com/search/videos/?q={}"
LOGIN_URL = "https://www.facebook.com/"
DRIVER_DIR = "/Users/swsong/test/chromedriver"

def facebook_scrap(keyword):
    driver = webdriver.Chrome(DRIVER_DIR)
    driver.implicitly_wait(10)
    try:
        driver.get(LOGIN_URL)
        e = driver.find_element_by_id('email')
        e.clear()
        e.send_keys("01022169441")
        e = driver.find_element_by_id('pass')
        e.clear()
        e.send_keys("u89320239")
        e.send_keys(Keys.ENTER)
        print("login")
        alert = driver.switch_to_alert()
        alert.accept()
        driver.get(SEARCH_URL.format(keyword))

        links = []
        for link in driver.find_elements_by_css_selector('div._14as > a'):
            links.append(link.get_attribute('href'))
            break

        print('content_length : ', len(links))

        for link in links:
            driver.implicitly_wait(10)
            driver.get(link)
            author = driver.find_element_by_class_name('_371y').text
            likes = driver.find_element_by_class_name('_1g5v').text
            com_share = driver.find_elements_by_class_name('_36_q')
            com = com_share[0].text
            share = com_share[1].text
            print('(글 정보) -> ', author, likes, com, share)

            time.sleep(1.5)
            comment_btn = driver.find_element_by_class_name('_2xui')
            comment_btn.click()
            time.sleep(1.5)
            try:
                view_more = driver.find_element_by_class_name('UFIPagerLink')
                view_more.click()
            except:
                pass

            classes = driver.find_elements_by_class_name('UFICommentActorAndBodySpacing')
            for clas in classes:
                user = clas.find_element_by_css_selector('div.UFICommentActorAndBodySpacing > span > a').text
                reply = clas.find_element_by_class_name('UFICommentBody').text
                print("({}): {}".format(user, reply))
            
    except Exception as e:
        print(e)
    finally:
        driver.quit()

if __name__ == "__main__":
    keyword = input('keyword : ')
    facebook_scrap(str(keyword))