from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

options = webdriver.EdgeOptions()
options.add_argument('--headless')
driver = webdriver.Edge(options=options)
streamer = ''

url='https://www.twitch.tv/popout/'+streamer+'/chat?popout='
driver.get(url)

element = 'span'
attribute = 'data-a-target'
message = 'chat-message-text'

bin = set()

def wait_for_elements():
    return WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR, f"{element}[{attribute}='{message}']"))
    )

while True:
    try:
        elements = wait_for_elements()

        for div in elements:
            text_content = div.text
            if((text_content not in bin)):
                bin.add(text_content)
                with open('output.txt', 'a', encoding='utf-8') as file:
                    file.write(text_content + '\n')

    except Exception as e:
        print(e)