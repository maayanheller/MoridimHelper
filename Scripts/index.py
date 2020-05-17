import secrets
from selenium import webdriver
from time import sleep

# Use the webdriver inside the computer
browser = webdriver.Chrome('../../../bin/chromedriver.exe')


class MoridimHelper:
    def __init__(self, username, pw, series_or_movie_link, number_of_ul):
        # Goes to a given link
        browser.get(series_or_movie_link)
        # Gets the html of the link
        html = browser.page_source
        # Sleep for 2 seconds so the site can load itself
        sleep(2)
        # Click on the close button of the popup
        browser.find_element_by_xpath('//*[@id="importantMessage"]/div/div/span').click()

MoridimHelper(secrets.username, secrets.pw, 'https://moridim01.tv/Series/%D7%91%D7%99%D7%AA-%D7%94%D7%A0%D7%99%D7%99%D7%A8_705.html', 4)