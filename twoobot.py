from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep, strftime
from random import randint
import pandas as pd

chromedriver_path = 'C:/Users/Ivan/Downloads/chromedriver_win32/chromedriver.exe' # Change this to your own chromedriver path!
webdriver = webdriver.Chrome(executable_path=chromedriver_path)
sleep(2)
webdriver.get('https://www.twoo.com/?login=1#login')
sleep(6)

coockies = webdriver.find_element_by_css_selector('#default > div.optanon-alert-box-wrapper > div.optanon-alert-box-bg > div.optanon-alert-box-button-container > div.optanon-alert-box-button.optanon-button-allow > div > button')
coockies.click()
sleep(3)

email = webdriver.find_element_by_css_selector(
    '#wrapper > div.tw3-homepage--abstract.tw3-homepage--abstract--desktop > div.homepageContainer__content__form.homepageContainer__content__form--intro.loginContainer.jsLoginContainer > div.tw3-pane.tw3-pane--right > div > form > div > div:nth-child(1) > div.tw3-form__row__input > input')
email.send_keys('manson.jeremy22@gmail.com')
password = webdriver.find_element_by_css_selector(
    '#wrapper > div.tw3-homepage--abstract.tw3-homepage--abstract--desktop > div.homepageContainer__content__form.homepageContainer__content__form--intro.loginContainer.jsLoginContainer > div.tw3-pane.tw3-pane--right > div > form > div > div:nth-child(2) > div.tw3-form__row__input > input')
password.send_keys('ivan123451997')
#sleep(3)

button_login = webdriver.find_element_by_css_selector('#wrapper > div.tw3-homepage--abstract.tw3-homepage--abstract--desktop > div.homepageContainer__content__form.homepageContainer__content__form--intro.loginContainer.jsLoginContainer > div.tw3-pane.tw3-pane--right > div > form > div > div:nth-child(3) > input')
button_login.click()
sleep(3)

#button_skip_shit = webdriver.find_element_by_css_selector(
#   '#smartOnboarding > a > span')
#button_skip_shit.click()
#sleep(2)

i = 0
while i < 50:
    sleep(1)
    i += 1
    try:
        if i >= 49:
            raise Exception
        else:
            like_button = webdriver.find_element_by_css_selector(
                '#gameColLeft > div > div.jsPhotoCoverContainer.photoCoverHolder > div.jsPhotoCoverContainerActions.photoCoverHolder__actions > div > a.tw3--button.tw3--button--circle.tw3--button--like.jsActionVoteYes > i > i')
            like_button.click()
    except Exception:
        try:
            close_pop_button = webdriver.find_element_by_xpath(
                '/html/body/div[15]/div[2]/div/div/div[1]/a/i/i')
            close_pop_button.click()
            sleep(2)
            chat_button = webdriver.find_element_by_xpath('/html/body/div[5]/div[2]/div/ul[1]/li[4]/a/i')
            chat_button.click()
            sleep(1)
            more_button = webdriver.find_element_by_css_selector('body > div.tw3-wrapper > div.tw3-content > div > div > div.jsMessageHeightHelper.messagesHeightHelper > div > div.jsMessageInboxTypes.inboxContainer__menu.jsShowOnboardingInbox > div > a.tw3-tab.tw3-pointerMenuToggle.jsMoreInboxesMenuToggle')
            more_button.click()
            sleep(1)
            unread_button = webdriver.find_element_by_xpath('/html/body/div[8]/div[2]/div/div/div[3]/div/div[2]/div/ul/li[1]/ul/li[1]/a')
            unread_button.click()
            sleep(1)
            while True:
                message = webdriver.find_elements_by_class_name('unread')
                if len(message) == 0:
                    print('There are no messages!')
                    break
                message[0].click()
                sleep(1)
                msg_box = webdriver.find_element_by_class_name('tw3-textarea')
                msg_box.send_keys('Hey')
                sleep(0.2)
                send_button = webdriver.find_element_by_xpath('//*[@id="jsSendMessageFormSend"]/div[2]/a[8]')
                send_button.click()
                sleep(0.5)
        except Exception:
            print('Bullshit happend')
            break
