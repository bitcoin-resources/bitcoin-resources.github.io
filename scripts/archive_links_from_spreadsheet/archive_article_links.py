from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from time import sleep

# Open 'atricle_links.txt' file, archive every link that was
# grabbed from the spreadsheet that still hadn't been archived
# Semi-Automatic: needs human supervision during process because of captchas
# Saves archived URLs into 'archived_links.txt'
with open('article_links.txt', 'r') as links:
    for link in links:
        try:
            browser = webdriver.Chrome(executable_path=ChromeDriverManager().install())
            browser.get('https://archive.is/?run=1&url=' + link)
            sleep(15)
            with open('archived_links.txt', 'a') as archive:
                archive.write(browser.current_url + '\n')
            sleep(10)
            browser.quit()
        except:
            pass
    archive.close()
links.close()
