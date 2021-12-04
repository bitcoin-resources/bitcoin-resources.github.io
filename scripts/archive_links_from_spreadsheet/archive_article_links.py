from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

# Open 'article_links.txt' file, archive every link that was
# grabbed from the spreadsheet that still hadn't been archived
# Semi-Automatic: needs human supervision during process because of captchas
# Saves archived URLs into 'archived_links.txt'
# When archiving 'a lot of websites' you'll need to change IP-Address/VPN
# regularly, because captcha and archive.is will limit your bandwidth
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
            archive.close()
        except:
            pass
links.close()
