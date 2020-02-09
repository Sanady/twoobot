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

button_skip_shit = webdriver.find_element_by_css_selector(
    '#smartOnboarding > a > span')
button_skip_shit.click()
sleep(2)

i = 0
while i < 50:
    sleep(1)
    i += 1
    try:
        like_button = webdriver.find_element_by_css_selector('#gameColLeft > div > div.jsPhotoCoverContainer.photoCoverHolder > div.jsPhotoCoverContainerActions.photoCoverHolder__actions > div > a.tw3--button.tw3--button--circle.tw3--button--like.jsUploaderTrigger.jsActionVoteYes > i > i')
        like_button.click()
    except Exception:
        try:
            close_pop_button = webdriver.find_element_by_css_selector('#gameColLeft > div > div.jsPhotoCoverContainer.photoCoverHolder > div.jsPhotoCoverContainerActions.photoCoverHolder__actions > div > a.tw3--button.tw3--button--circle.tw3--button--like.jsUploaderTrigger.jsActionVoteYes > i > i')
            close_pop_button.click()
        except Exception:
            print('Bullshit happend')