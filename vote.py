
from selenium import webdriver
from selenium.common.exceptions import TimeoutException, WebDriverException
import time
import proxyscrape
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

proxy_count = 0
proxies = 0


def get_ips():
    global proxy_count, proxies
    collector = proxyscrape.create_collector('my-collector', 'http')
    proxies = collector.get_proxies({'country': 'united states'})
    proxy_count = len(proxies)
    print(f"Getting {proxy_count} proxies")
    '''
    for i in proxies:
        print(f"{i.host}:{i.port}")
        time.sleep(2)
    '''
    return proxies


votes = 0

option = webdriver.ChromeOptions()
option.add_argument('--disable-blink-features=AutomationControlled')
# option.add_argument("window-size=850,800")
option.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36")


while True:
    if votes >= proxy_count:
        proxies = get_ips()

    temp_proxy = proxies[votes]
    temp_proxy = temp_proxy
    option.add_argument(f'--proxy-server={temp_proxy}')
    print(f'Voting with IP: {temp_proxy}')
    driver = webdriver.Chrome(options=option)

    try:
        driver.get("https://www.nj.com/highschoolsports/2021/06/the-top-nj-boys-lacrosse-freshmen-in-2021-our-picks-your-votes.html")#put here the adress of your page
    except TimeoutException:
        driver.execute_script("window.stop();")

    try:
        driver.get("https://www.nj.com/highschoolsports/2021/06/the-top-nj-boys-lacrosse-freshmen-in-2021-our-picks-your-votes.html")  # put here the adress of your page
    except WebDriverException:
        driver.execute_script("window.stop();")
        driver.get("https://www.nj.com/highschoolsports/2021/06/the-top-nj-boys-lacrosse-freshmen-in-2021-our-picks-your-votes.html")#put here the adress of your page

    # elem = driver.find_elements_by_xpath("//div[@class='css-answer pds-answer']")
    driver.execute_script("window.scrollTo(0, 20000)")
    time.sleep(3)
    elem = driver.find_element_by_xpath("//span[text()='Dylan Knapp, Somerville']")
    driver.execute_script("arguments[0].click();", elem)
    driver.execute_script("window.scrollTo(0, 24000)")



    vote = driver.find_element_by_xpath("//*[@class='css-vote-button pds-vote-button']")
    vote.click()
    # driver.execute_script("arguments[0].click();", WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//*[@class='css-vote-button pds-vote-button']"))))
    time.sleep(8)
    driver.execute_script("window.scrollTo(0, 17000)")

    driver.execute_script("window.scrollTo(0, 17500)")

    driver.execute_script("window.scrollTo(0, 18000)")

    votes = votes + 1

    print(f"Voted for Dylan Knapp [{votes}] times.")

    driver.quit()

