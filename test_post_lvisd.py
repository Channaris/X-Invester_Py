from pickle import GLOBAL
import requests
from bs4 import BeautifulSoup
import csv
import itertools
from email.mime import image
import imp
from unittest import skip
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait,Select
from selenium.webdriver.common.action_chains import ActionChains
import io
from PIL import Image
import time
import os
from pymongo import MongoClient
import pymongo
from collections import ChainMap
from bson.objectid import ObjectId
from datetime import date
################################################################

today = date.today()

PATH = "D:\\work\\web_scraping\\program\\chromedriver.exe"
os.environ['webdriver.chrome.driver'] = PATH
wd = webdriver.Chrome(PATH)
wd.maximize_window()

# ##Start of db zone###
myclient = pymongo.MongoClient("mongodb+srv://wiewworkmotion:0826521401Wiew@cluster0.pu7bm.mongodb.net/?retryWrites=true&w=majority")
mydb = myclient["test_X-invester"]
mycol = mydb["test_X-invester_ppth_newlo2"]

def insert_data_mongo(raw_data_home):

    mydict = raw_data_home

    x = mycol.insert_one(mydict)

##########################query################################################################
def query():
  myquery = {"_id":ObjectId('63201f574a1c94218af6f5f5')}

  mydoc = mycol.find(myquery)
  global galleryUrls
  for x in mydoc:
    try:
      lat_long = []
      topic = x.get('name')
      galleryUrls = x.get('galleryUrls')
      listType = x.get('listType')
      PropertyType = x.get('propertyTypes')
      watchListPropertyTypes = x.get('watchListPropertyTypes')
      Property = x.get('property')
      details_array = x.get('cut_find_details')
      details_dict = dict(ChainMap(*details_array))
      totalBedroom = details_dict.get('จำนวนห้องนอน')
      totalToilet = x.get('totalToilet')
      startingPrice = x.get('startingPrice')
      finalPrice = x.get('finalPrice')
      minimumArea = details_dict.get('ขนาดพื้นที่ห้อง')
      maximumArea = details_dict.get('ขนาดพื้นที่ห้อง')
      # TH_Name = x.get('TH_Name')
      # EN_Name = x.get('EN_Name')
      # Address = x.get('Address')
      # Latitude = x.get('Latitude')
      # Longitude = x.get('Longitude')
      Description = x.get('description')
      State = x.get('State')
      City = x.get('City')
      SubCity = x.get('SubCity')
      cut_find_address = x.get('cut_find_address')

      post_topic.append(topic)
      imgs.append(galleryUrls)
      list_type.append(listType)
      property_type.append(PropertyType)
      property.append(Property)
      bedroom.append(totalBedroom)
      toilet.append(totalToilet)
      s_price.append(startingPrice)
      f_price.append(finalPrice)
      min_area.append(minimumArea)
      max_area.append(maximumArea)
      description.append(Description)
      watchlistPropertyTypes.append(watchListPropertyTypes)
      state.append(State)
      city.append(City)
      subcity.append(SubCity)
      address.append(cut_find_address)

    except:
      topic = x.get('name')
      galleryUrls = x.get('galleryUrls')
      listType = x.get('listType')
      PropertyType = x.get('propertyTypes')
      watchListPropertyTypes = x.get('watchListPropertyTypes')
      Property = x.get('property')
      totalBedroom = x.get('totalBedroom')
      totalToilet = x.get('totalToilet')
      startingPrice = x.get('startingPrice')
      finalPrice = x.get('finalPrice')
      minimumArea = x.get('minimumArea')
      maximumArea = x.get('maximumArea')
      Description = x.get('description')
      # TH_Name = x.get('TH_Name')
      # EN_Name = x.get('EN_Name')
      # Address = x.get('Address')
      # Latitude = x.get('Latitude')
      # Longitude = x.get('Longitude')
      State = x.get('State')
      City = x.get('City')
      SubCity = x.get('SubCity')
      cut_find_address = x.get('cut_find_address')

      post_topic.append(topic)
      imgs.append(galleryUrls)
      list_type.append(listType)
      property_type.append(PropertyType)
      property.append(Property)
      bedroom.append(totalBedroom)
      toilet.append(totalToilet)
      s_price.append(startingPrice)
      f_price.append(finalPrice)
      min_area.append(minimumArea)
      max_area.append(maximumArea)
      description.append(Description)
      watchlistPropertyTypes.append(watchListPropertyTypes)
      state.append(State)
      city.append(City)
      subcity.append(SubCity)
    # lat_long.append(Latitude)
    # lat_long.append(Longitude)
      address.append(cut_find_address)

  def pnt():
    print('pnt',post_topic)
  pnt()


    # lat_long.append(Latitude)
    # lat_long.append(Longitude)
##########################query################################################################

##End of db zone###
province_xpath = '//*[text()="{}"]'
district_xpath = '//*[text()="{}"]'
subdistrict_xpath = '//*[text()="{}"]'
province = 'กรุงเทพมหานคร'
district = 'ดุสิต'
subdistrict = 'ดุสิต'
ad_title = ['test(English)12345657891011121311415161718test(English)12345657891011121311415161718test(English)12345657891011121311415161718test(English)12345657891011121311415161718test(English)12345657891011121311415161718test(English)12345657891011121311415161718test(English)12345657891011121311415161718test(English)12345657891011121311415161718test(English)12345657891011121311415161718test(English)12345657891011121311415161718test(English)12345657891011121311415161718test(English)12345657891011121311415161718test(English)12345657891011121311415161718test(English)12345657891011121311415161718test(English)12345657891011121311415161718test(English)12345657891011121311415161718test(English)12345657891011121311415161718test(English)12345657891011121311415161718test(English)12345657891011121311415161718test(English)12345657891011121311415161718test(English)12345657891011121311415161718test(English)12345657891011121311415161718test(English)12345657891011121311415161718test(English)12345657891011121311415161718test(English)12345657891011121311415161718test(English)12345657891011121311415161718test(English)12345657891011121311415161718test(English)12345657891011121311415161718test(English)12345657891011121311415161718test(English)12345657891011121311415161718test(English)12345657891011121311415161718test(English)12345657891011121311415161718test(English)12345657891011121311415161718test(English)12345657891011121311415161718test(English)12345657891011121311415161718test(English)12345657891011121311415161718test(English)12345657891011121311415161718test(English)12345657891011121311415161718test(English)12345657891011121311415161718test(English)12345657891011121311415161718test(English)12345657891011121311415161718test(English)12345657891011121311415161718test(English)12345657891011121311415161718test(English)12345657891011121311415161718test(English)12345657891011121311415161718test(English)12345657891011121311415161718test(English)12345657891011121311415161718test(English)12345657891011121311415161718test(English)12345657891011121311415161718test(English)12345657891011121311415161718test(English)12345657891011121311415161718']
################################################################
JS_ADD_TEXT_TO_INPUT = """
    var elm = arguments[0], txt = arguments[1];
    elm.value += txt;
    elm.dispatchEvent(new Event('change'));
    """

i=0
cpost = 1
n_pic = 1
post_topic = []
list_type = []
bedroom = []
toilet = []
s_price = []
f_price = []
min_area = []
max_area = []
description = []
property_type = []
watchlistPropertyTypes =[]
property = []
imgs = []
state = []
city = []
subcity = []
address = []
####url################################
url = "https://www.livinginsider.com/"

wd.get(url)
wait = WebDriverWait(wd, 10)
####url################################
##########################click_login################################################################
def click_login():
    wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="none_login_zone"]/a[1]')))
    wd.find_element(By.XPATH, '//*[@id="none_login_zone"]/a[1]').click()
    time.sleep(2)

# click_login()

##########################click_login##########################################

###############################fill_login##########################################
def fill_login():
    wd.implicitly_wait(0.5)
    wait.until(EC.element_to_be_clickable((By.ID, "login_username"))).send_keys("mailusedfortest@gmail.com")
    wd.find_element(By.CLASS_NAME, 'btn-next-step').click()
    time.sleep(2)
    wd.find_element(By.XPATH, '//*[@id="password"]').send_keys("qwerty123456Zx")
    wd.find_element(By.CLASS_NAME, 'btn-next-step').click()
    print("Click Login_Button finish")
    time.sleep(4)

###############################fill_login##########################################

#######################click_createpost#######################################
def click_createpost():
    time.sleep(0.5)
    wd.get(url)
    time.sleep(3)

    wd.find_element(By.XPATH, '//*[@id="navbar"]/ul/li[8]/a').click()
    
########################click_createpost######################################

################################fill_data####################################
def fill_data():
    ###################################PAGE1###################################

    time.sleep(2)
################ข้อมูลทั่วไป#######################################


#########################สถานะผู้ประกาศ#######################################################
    # check if
    # wd.find_element(By.XPATH, '//*[@id="post_data"]/div[1]/div[1]/div/div[1]/label').click()  # Owner
    wd.find_element(By.XPATH, '//*[@id="post_data"]/div[1]/div[1]/div/div[2]/label').click()  # Agent
#########################สถานะผู้ประกาศ#######################################################
#########################Stock ID#######################################################
    # wd.find_element(By.ID, 'web_sku').send_keys('000')
    # wd.find_element(By.XPATH, '//*[@id="post_data"]/div[1]/div[4]/div/div[1]/label').click()  # sell

#########################Stock ID#######################################################
#########################Title#######################################################
    headtitle = wd.find_element(By.ID, 'web_title')#.send_keys(post_topic)
    wd.execute_script(JS_ADD_TEXT_TO_INPUT, headtitle, post_topic)

#########################Title#######################################################
#########################Description #######################################################
    ad_title = wd.find_element(By.ID, 'web_description')#.send_keys(description)
    wd.execute_script(JS_ADD_TEXT_TO_INPUT, ad_title, description)

#########################Description #######################################################
#########################ประเภทประกาศ#######################################################
    # check if
    wd.find_element_by_tag_name('body').send_keys(Keys.CONTROL + Keys.HOME)
    time.sleep(2)

    print(list_type)

    if 'sell' in list_type or 'ขาย' in list_type:
        wd.find_element(By.XPATH, '//*[@id="post_data"]/div[1]/div[4]/div/div[1]/label').click()  # sell
        if property_type[0] == "[ObjectId('62bd7104f0521b8890fe9a0f')]":
            condo_sell_page2()
        elif property_type[0] == "[ObjectId('62bd7104f0521b8890fe9a11')]":
            house_sell_page2()
    elif list_type == ['down'] or list_type == ['ดาวน์']:
        wd.find_element(By.XPATH, '//*[@id="post_data"]/div[1]/div[4]/div/div[2]/label').click()  # down
    elif 'rent' in list_type or 'เช่า' in list_type:
        # wd.find_element(By.XPATH, '//*[@id="post_data"]/div[1]/div[4]/div/div[1]/label').click()  # sell
        # print('click sell')
        
        wd.find_element(By.XPATH, '//*[@id="post_data"]/div[1]/div[4]/div/div[3]/label').click()  # rent
        print('click rent')
        print(property_type)
        if property_type[0] == "[ObjectId('62bd7104f0521b8890fe9a0f')]":
            condo_rent_page2()
            print('condo_rent_page2')
        elif property_type[0] == "[ObjectId('62bd7104f0521b8890fe9a11')]":
            house_rent_page2()
            print('house_rent_page2')
        else:
            print('error')
            house_sell_page2()
    elif list_type == ['long lease'] or list_type == ['เซ้ง']:
        wd.find_element(By.XPATH, '//*[@id="post_data"]/div[1]/div[4]/div/div[4]/label').click()  # long lease

#########################ประเภทประกาศ#######################################################
#########################ประเภทอสังหาริมทรัพย์#######################################################
    # check if

    # buildingList_el = wd.find_element_by_id('buildingList')
    # for buildingList_option in buildingList_el.find_elements_by_tag_name('option'):
    #     if buildingList_option.text == property_type:
    #         buildingList_option.click()  # select() in earlier versions of webdriver
    #         break
    #     else:
    #         buildingList_option.click('คอนโด') # select() in

    # house
    # land
    # shophouse
    # office
    # townhouse
    # homeoffice
    # retail
    # showroom
    # bfs
    # factory
    # wh
#########################ประเภทอสังหาริมทรัพย์#######################################################
# #########################ทำเล#######################################################
#     # check if
#     time.sleep(2)
#     wd.find_element(By.XPATH, '//*[@id="post_data"]/div[1]/div[7]/span/span[1]/span').click()
#     wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/span/span/span[1]/input')))
#     wd.find_element(By.XPATH, '/html/body/span/span/span[1]/input').send_keys("จตุจักร")
#     time.sleep(2)
#     wd.find_element(By.XPATH, '//*[@id="select2-web_zone_id-results"]/li').click()
#     time.sleep(1)

#     # area =
#     # area.click()

# #########################ทำเล#######################################################
# #########################map#######################################################
#     wd.find_element(By.XPATH, '//*[@id="post_data"]/div[3]/div[3]/div/div/button').click()
#     time.sleep(2)
###################################PAGE1###################################
###################################PAGE3###################################
    # #draft
    wd.find_element(By.ID, 'save_draft').click()
    # #draft

    # #post
    # wd.find_element(By.ID, 'save_publish').click()
    # wd.find_element(By.ID, 'btn_post').click()
    # #post

###################################PAGE3###################################
def condo_sell_page2():#ผ่าน
    print('condo_sell_page2')
    time.sleep(2)
    buildingList_el = wd.find_element_by_id('buildingList')
    for buildingList_option in buildingList_el.find_elements_by_tag_name('option'):
        if buildingList_option.text == 'คอนโด':
            time.sleep(2)
            buildingList_option.click()  # select() in earlier versions of webdriver
            break    
        # if property_type == ['คอนโด']:
        #     if buildingList_option.text == 'คอนโด':
        #         buildingList_option.click()  # select() in earlier versions of webdriver
        #         break
        # else:
        #     if buildingList_option.text == 'คอนโด':
        #         buildingList_option.click()  # select() in earlier versions of webdriver
        #         break
            # buildingList_option.click('คอนโด') # select() in

#########################   condoProject name#######################################################
    time.sleep(2)
    wd.execute_script("document.getElementById('div_web_project_id').style.display='block';")

    wd.find_element(By.XPATH, '//*[@id="div_web_project_id"]/span').click()
    time.sleep(1)
    wd.find_element(By.XPATH, '/html/body/span/span/span[1]/input').send_keys("ไม่ทราบชื่อโครงการ")
    time.sleep(2)
    wd.find_element(By.XPATH, '//*[@id="select2-web_project_id-results"]/li[1]').click()

#########################condoProject name#######################################################
#########################ทำเล#######################################################
    # check if
    time.sleep(2)
    wd.find_element(By.XPATH, '//*[@id="post_data"]/div[1]/div[7]/span/span[1]/span').click()
    wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/span/span/span[1]/input')))
    wd.find_element(By.XPATH, '/html/body/span/span/span[1]/input').send_keys("จตุจักร")
    time.sleep(2)
    wd.find_element(By.XPATH, '//*[@id="select2-web_zone_id-results"]/li').click()
    time.sleep(1)

    # area =
    # area.click()

#########################ทำเล#######################################################
#########################map#######################################################
    wd.find_element(By.ID, 'posmap').click()

#########################map#######################################################
    wd.find_element_by_tag_name('body').send_keys(Keys.CONTROL + Keys.END)
    time.sleep(1)
    wd.find_element(By.XPATH, '//*[@id="post_data"]/div[3]/div[3]/div/div/button').click()
    print('click_next')
    time.sleep(2)
###################################PAGE1###################################
###################################PAGE2###################################
###########################################Bedrooms#########################################################
    wait.until(EC.element_to_be_clickable((By.ID, "select2-web_room-container")))
    wd.find_element(By.ID, 'select2-web_room-container').click()
    bedroom_el = wd.find_element(By.ID, 'web_room')
    for bedroom_option in bedroom_el.find_elements_by_tag_name('option'):
        if property_type == ['สตูดิโอ']:
            if bedroom_option.text == 'ห้องสตูดิโอ':
                bedroom_option.click()  # select() in earlier versions of webdriver
                break
        elif bedroom == ['1'] or bedroom == ['1 ห้อง']:
            if bedroom_option.text == '1 ห้อง':
                bedroom_option.click()  # select() in earlier versions of webdriver
                break
        elif bedroom == ['2'] or bedroom == ['2 ห้อง']:
            if bedroom_option.text == '2 ห้อง':
                bedroom_option.click()  # select() in earlier versions of webdriver
                break
        elif bedroom == ['3'] or bedroom == ['3 ห้อง']:
            if bedroom_option.text == '3 ห้อง':
                bedroom_option.click()  # select() in earlier versions of webdriver
                break
        elif bedroom == ['4'] or bedroom == ['4 ห้อง']:
            if bedroom_option.text == '4 ห้อง':
                bedroom_option.click()  # select() in earlier versions of webdriver
                break
        elif bedroom == ['5'] or bedroom == ['5 ห้อง']:
            if bedroom_option.text == '5 ห้อง':
                bedroom_option.click()  # select() in earlier versions of webdriver
                break
        elif bedroom == ['6'] or bedroom == ['6 ห้อง']:
            if bedroom_option.text == '6 ห้อง':
                bedroom_option.click()  # select() in earlier versions of webdriver
                break
        elif bedroom == ['7'] or bedroom == ['7 ห้อง']:
            if bedroom_option.text == '7 ห้อง':
                bedroom_option.click()  # select() in earlier versions of webdriver
                break
        elif bedroom == ['8'] or bedroom == ['8 ห้อง']:
            if bedroom_option.text == '8 ห้อง':
                bedroom_option.click()  # select() in earlier versions of webdriver
                break
        elif bedroom == ['9'] or bedroom == ['9 ห้อง']:
            if bedroom_option.text == '9 ห้อง':
                bedroom_option.click()  # select() in earlier versions of webdriver
                break
        elif bedroom == ['10'] or bedroom == ['10 ห้อง']:
            if bedroom_option.text == '10 ห้อง':
                bedroom_option.click()  # select() in earlier versions of webdriver
                break
        elif bedroom == ['มากกว่า 10'] or bedroom == ['มากกว่า 10']:
            if bedroom_option.text == 'มากกว่า 10':
                bedroom_option.click()  # select() in earlier versions of webdriver
                break
        else:
            if bedroom_option.text == 'ห้องสตูดิโอ':
                bedroom_option.click()  # select() in earlier versions of webdriver
                break
##########################################Bedrooms#########################################################
##########################################Bathrooms#########################################################
    wd.find_element(By.ID, 'select2-web_bathroom-container').click()
    bathroom_el = wd.find_element(By.ID, 'web_bathroom')
    for bathroom_option in bathroom_el.find_elements_by_tag_name('option'):
        if toilet == ['1'] or toilet == ['1 ห้องน้ำ']:
            if bathroom_option.text == '1 ห้องน้ำ':
                bathroom_option.click()  # select() in earlier versions of webdriver
                break
        elif toilet == ['2'] or toilet == ['2 ห้องน้ำ']:
            if bathroom_option.text == '2 ห้องน้ำ':
                bathroom_option.click()  # select() in earlier versions of webdriver
                break
        elif toilet == ['3'] or toilet == ['3 ห้องน้ำ']:
            if bathroom_option.text == '3 ห้องน้ำ':
                bathroom_option.click()  # select() in earlier versions of webdriver
                break
        elif toilet == ['4'] or toilet == ['4 ห้องน้ำ']:
            if bathroom_option.text == '4 ห้องน้ำ':
                bathroom_option.click()  # select() in earlier versions of webdriver
                break
        elif toilet == ['5'] or toilet == ['5 ห้องน้ำ']:
            if bathroom_option.text == '5 ห้องน้ำ':
                bathroom_option.click()  # select() in earlier versions of webdriver
                break
        elif toilet == ['มากกว่า 5']:
            if bathroom_option.text == 'มากกว่า 5':
                bathroom_option.click()  # select() in earlier versions of webdriver
                break
        else:
            if bathroom_option.text == '1 ห้องน้ำ':
                bathroom_option.click()  # select() in earlier versions of webdriver
                break

##########################################Bathrooms#########################################################
##########################################Level#########################################################
    wd.find_element(By.ID, 'select2-web_floor-container').click()
    level_el = wd.find_element(By.ID, 'web_floor')
    for level_option in level_el.find_elements_by_tag_name('option'):
        if level_option.text == '1-4':
            level_option.click()  # select() in earlier versions of webdriver
            break

##########################################Level#########################################################
##########################################area#########################################################
    wd.find_element(By.ID, 'web_area_size').send_keys(max_area[0])

##########################################area#########################################################
##########################################Selling price#########################################################
    wd.find_element(By.ID, 'web_price').send_keys(f_price[0])

##########################################Selling price#########################################################
##########################################Special Additional#########################################################

    # wd.find_element(By.XPATH, '//*[@id="web_keeping_pet"]').click()
    # wd.find_element(By.XPATH, '//*[@id="topic_duplex"]').click()
    # wd.find_element(By.XPATH, '//*[@id="topic_penthouse"]').click()

##########################################Special Additional#########################################################
##########################################Matterport URL#########################################################
    # wd.find_element(By.ID, 'web_matterport').send_keys('1')

##########################################Matterport URL#########################################################
##########################################Youtube URL#########################################################
    # wd.find_element(By.ID, 'web_youtube').send_keys('1')

##########################################Youtube URL#########################################################
##########################################picture#########################################################
    for n_img in range(int(len(galleryUrls))):
        wd.find_element(By.ID, 'fileupload').send_keys(galleryUrls[n_img])
##########################################picture#########################################################
    wd.find_element_by_tag_name('body').send_keys(Keys.CONTROL + Keys.END)
    time.sleep(5)
    try:
        wd.find_element(By.XPATH, '//*[@id="post_data_main"]/div[8]/div/div/div/button[2]').click()
        print('click xpath')
    except:
        wd.find_element(By.CLASS_NAME, 'btn btn-step-default step-next mr-auto ml-2').click()
        print('click CLASS_NAME')
    wd.find_element(By.XPATH, '/html/body/div[2]/section[2]/div/div[3]/div/div/div/div/div/div/div/form/div[8]/div/div/div/button[2]').click()
    print('click post')
    time.sleep(3)
    wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="post_data"]/div[1]/div/div[2]/div')))
    wd.find_element(By.XPATH, '//*[@id="post_data"]/div[1]/div/div[2]/div').click()
    wd.find_element(By.XPATH,'//*[@id="post_data"]/div[3]/button').click()


###################################PAGE2###################################

def condo_rent_page2():#ผ่าน
    print('condo_rent_page2')
    time.sleep(2)
    buildingList_el = wd.find_element_by_id('buildingList')
    for buildingList_option in buildingList_el.find_elements_by_tag_name('option'):
        if buildingList_option.text == 'คอนโด':
            time.sleep(2)

            buildingList_option.click()  # select() in earlier versions of webdriver
            break  
#########################   condoProject name#######################################################
    wd.execute_script("document.getElementById('div_web_project_id').style.display='block';")

    wd.find_element(By.XPATH, '//*[@id="div_web_project_id"]/span').click()
    time.sleep(1)
    try:
        wd.find_element(By.XPATH, '/html/body/span/span/span[1]/input').send_keys(address[0])
        time.sleep(2)
        wd.find_element(By.XPATH, '//*[@id="select2-web_project_id-results"]/li[1]').click()
    except:
        wd.find_element(By.XPATH, '/html/body/span/span/span[1]/input').send_keys("ไม่ทราบชื่อโครงการ")
        time.sleep(2)
        wd.find_element(By.XPATH, '//*[@id="select2-web_project_id-results"]/li[1]').click()

#########################   condoProject name#######################################################
#########################ทำเล#######################################################
    # check if
    time.sleep(2)
    wd.find_element(By.XPATH, '//*[@id="post_data"]/div[1]/div[7]/span/span[1]/span').click()
    wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/span/span/span[1]/input')))
    wd.find_element(By.XPATH, '/html/body/span/span/span[1]/input').send_keys(city[0])
    time.sleep(2)
    wd.find_element(By.XPATH, '//*[@id="select2-web_zone_id-results"]/li').click()
    time.sleep(1)

    # area =
    # area.click()

#########################ทำเล#######################################################
#########################map#######################################################
    wd.find_element(By.ID, 'posmap').click()

#########################map#######################################################
    wd.find_element_by_tag_name('body').send_keys(Keys.CONTROL + Keys.END)
    time.sleep(1)
    wd.find_element(By.XPATH, '//*[@id="post_data"]/div[3]/div[3]/div/div/button').click()
    time.sleep(2)
###################################PAGE1###################################
###################################PAGE2###################################
###########################################Bedrooms#########################################################
    wait.until(EC.element_to_be_clickable((By.ID, "select2-web_room-container")))
    wd.find_element(By.ID, 'select2-web_room-container').click()
    bedroom_el = wd.find_element(By.ID, 'web_room')
    for bedroom_option in bedroom_el.find_elements_by_tag_name('option'):
        if property_type == ['สตูดิโอ']:
            if bedroom_option.text == 'ห้องสตูดิโอ':
                bedroom_option.click()  # select() in earlier versions of webdriver
                break
        elif bedroom == ['1'] or bedroom == ['1 ห้อง']:
            if bedroom_option.text == '1 ห้อง':
                bedroom_option.click()  # select() in earlier versions of webdriver
                break
        elif bedroom == ['2'] or bedroom == ['2 ห้อง']:
            if bedroom_option.text == '2 ห้อง':
                bedroom_option.click()  # select() in earlier versions of webdriver
                break
        elif bedroom == ['3'] or bedroom == ['3 ห้อง']:
            if bedroom_option.text == '3 ห้อง':
                bedroom_option.click()  # select() in earlier versions of webdriver
                break
        elif bedroom == ['4'] or bedroom == ['4 ห้อง']:
            if bedroom_option.text == '4 ห้อง':
                bedroom_option.click()  # select() in earlier versions of webdriver
                break
        elif bedroom == ['5'] or bedroom == ['5 ห้อง']:
            if bedroom_option.text == '5 ห้อง':
                bedroom_option.click()  # select() in earlier versions of webdriver
                break
        elif bedroom == ['6'] or bedroom == ['6 ห้อง']:
            if bedroom_option.text == '6 ห้อง':
                bedroom_option.click()  # select() in earlier versions of webdriver
                break
        elif bedroom == ['7'] or bedroom == ['7 ห้อง']:
            if bedroom_option.text == '7 ห้อง':
                bedroom_option.click()  # select() in earlier versions of webdriver
                break
        elif bedroom == ['8'] or bedroom == ['8 ห้อง']:
            if bedroom_option.text == '8 ห้อง':
                bedroom_option.click()  # select() in earlier versions of webdriver
                break
        elif bedroom == ['9'] or bedroom == ['9 ห้อง']:
            if bedroom_option.text == '9 ห้อง':
                bedroom_option.click()  # select() in earlier versions of webdriver
                break
        elif bedroom == ['10'] or bedroom == ['10 ห้อง']:
            if bedroom_option.text == '10 ห้อง':
                bedroom_option.click()  # select() in earlier versions of webdriver
                break
        elif bedroom == ['มากกว่า 10'] or bedroom == ['มากกว่า 10']:
            if bedroom_option.text == 'มากกว่า 10':
                bedroom_option.click()  # select() in earlier versions of webdriver
                break
        else:
            if bedroom_option.text == 'ห้องสตูดิโอ':
                bedroom_option.click()  # select() in earlier versions of webdriver
                break
##########################################Bedrooms#########################################################
##########################################Bathrooms#########################################################
    wd.find_element(By.ID, 'select2-web_bathroom-container').click()
    bathroom_el = wd.find_element(By.ID, 'web_bathroom')
    for bathroom_option in bathroom_el.find_elements_by_tag_name('option'):
        if toilet == ['1'] or toilet == ['1 ห้องน้ำ']:
            if bathroom_option.text == '1 ห้องน้ำ':
                bathroom_option.click()  # select() in earlier versions of webdriver
                break
        elif toilet == ['2'] or toilet == ['2 ห้องน้ำ']:
            if bathroom_option.text == '2 ห้องน้ำ':
                bathroom_option.click()  # select() in earlier versions of webdriver
                break
        elif toilet == ['3'] or toilet == ['3 ห้องน้ำ']:
            if bathroom_option.text == '3 ห้องน้ำ':
                bathroom_option.click()  # select() in earlier versions of webdriver
                break
        elif toilet == ['4'] or toilet == ['4 ห้องน้ำ']:
            if bathroom_option.text == '4 ห้องน้ำ':
                bathroom_option.click()  # select() in earlier versions of webdriver
                break
        elif toilet == ['5'] or toilet == ['5 ห้องน้ำ']:
            if bathroom_option.text == '5 ห้องน้ำ':
                bathroom_option.click()  # select() in earlier versions of webdriver
                break
        elif toilet == ['มากกว่า 5']:
            if bathroom_option.text == 'มากกว่า 5':
                bathroom_option.click()  # select() in earlier versions of webdriver
                break
        else:
            if bathroom_option.text == '1 ห้องน้ำ':
                bathroom_option.click()  # select() in earlier versions of webdriver
                break

##########################################Bathrooms#########################################################
##########################################Level#########################################################
    wd.find_element(By.ID, 'select2-web_floor-container').click()
    level_el = wd.find_element(By.ID, 'web_floor')
    for level_option in level_el.find_elements_by_tag_name('option'):
        if level_option.text == '1-4':
            level_option.click()  # select() in earlier versions of webdriver
            break
##########################################Level#########################################################
##########################################area#########################################################
    wd.find_element(By.ID, 'web_area_size').send_keys(max_area[0])

##########################################area#########################################################
###############################web_contract_startdate########################################################
    c_day = today.strftime('%Y-%m-%d')
    print(c_day)
    wd.find_element(By.XPATH, '//*[@id="web_contract_startdate"]').click()
    # wd.find_element(By.XPATH, '//*[@id="web_contract_startdate"]').send_keys(c_day)

###############################web_contract_startdate########################################################
##########################################rent price#########################################################
    wd.find_element(By.ID, 'web_price').send_keys(f_price[0])

##########################################rent price#########################################################
##########################################Special Additional#########################################################

    # wd.find_element(By.XPATH, '//*[@id="web_keeping_pet"]').click()
    # wd.find_element(By.XPATH, '//*[@id="topic_duplex"]').click()
    # wd.find_element(By.XPATH, '//*[@id="topic_penthouse"]').click()

##########################################Special Additional#########################################################
##########################################Matterport URL#########################################################
    # wd.find_element(By.ID, 'web_matterport').send_keys('1')

##########################################Matterport URL#########################################################
##########################################Youtube URL#########################################################
    # wd.find_element(By.ID, 'web_youtube').send_keys('1')

##########################################Youtube URL#########################################################
##########################################picture#########################################################
    # wd.find_element(By.ID, 'fileupload').send_keys("D:\\work\\web_scraping\\test_pic\\404_1.jpeg")
    for n_img in range(int(len(galleryUrls))):
        wd.find_element(By.ID, 'fileupload').send_keys(galleryUrls[n_img])
##########################################picture#########################################################
    wd.find_element(By.XPATH, '//*[@id="post_data_main"]/div[10]/div/div/div/button[2]').click()
    wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="post_data"]/div[1]/div/div[2]/div')))
    wd.find_element(By.XPATH, '//*[@id="post_data"]/div[1]/div/div[2]/div').click()
    wd.find_element(By.XPATH, '//*[@id="post_data"]/div[3]/button').click()

###################################PAGE2###################################


def house_sell_page2():
    print('house_sell_page2')
    time.sleep(2)
    buildingList_el = wd.find_element_by_id('buildingList')
    for buildingList_option in buildingList_el.find_elements_by_tag_name('option'):
        if buildingList_option.text == 'บ้าน':
            time.sleep(2)
            buildingList_option.click()  # select() in earlier versions of webdriver
            break


#########################ทำเล#######################################################
    # check if
    time.sleep(2)
    # wd.execute_script("document.getElementById('div_web_zone_id').style.display='block';")
    wd.find_element(By.XPATH, '//*[@id="post_data"]/div[1]/div[7]/span/span[1]/span').click()
    wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/span/span/span[1]/input')))
    wd.find_element(By.XPATH, '/html/body/span/span/span[1]/input').send_keys("จตุจักร")
    time.sleep(2)
    wd.find_element(By.XPATH, '//*[@id="select2-web_zone_id-results"]/li').click()
    time.sleep(1)

    # area =
    # area.click()

#########################ทำเล#######################################################
#########################map#######################################################
    wd.find_element(By.ID, 'posmap').click()

#########################map#######################################################
    wd.find_element_by_tag_name('body').send_keys(Keys.CONTROL + Keys.END)
    wd.find_element(By.XPATH, '//*[@id="post_data"]/div[3]/div[3]/div/div/button').click()
    time.sleep(2)
###################################PAGE1###################################
###################################PAGE2###################################
###########################################Bedrooms#########################################################
    wait.until(EC.element_to_be_clickable((By.ID, "select2-web_room-container")))
    wd.find_element(By.ID, 'select2-web_room-container').click()
    bedroom_el = wd.find_element(By.ID, 'web_room')
    for bedroom_option in bedroom_el.find_elements_by_tag_name('option'):
        if bedroom == ['1'] or bedroom == ['1 ห้อง']:
            if bedroom_option.text == '1 ห้อง':
                bedroom_option.click()  # select() in earlier versions of webdriver
                break
        elif bedroom == ['2'] or bedroom == ['2 ห้อง']:
            if bedroom_option.text == '2 ห้อง':
                bedroom_option.click()  # select() in earlier versions of webdriver
                break
        elif bedroom == ['3'] or bedroom == ['3 ห้อง']:
            if bedroom_option.text == '3 ห้อง':
                bedroom_option.click()  # select() in earlier versions of webdriver
                break
        elif bedroom == ['4'] or bedroom == ['4 ห้อง']:
            if bedroom_option.text == '4 ห้อง':
                bedroom_option.click()  # select() in earlier versions of webdriver
                break
        elif bedroom == ['5'] or bedroom == ['5 ห้อง']:
            if bedroom_option.text == '5 ห้อง':
                bedroom_option.click()  # select() in earlier versions of webdriver
                break
        elif bedroom == ['6'] or bedroom == ['6 ห้อง']:
            if bedroom_option.text == '6 ห้อง':
                bedroom_option.click()  # select() in earlier versions of webdriver
                break
        elif bedroom == ['7'] or bedroom == ['7 ห้อง']:
            if bedroom_option.text == '7 ห้อง':
                bedroom_option.click()  # select() in earlier versions of webdriver
                break
        elif bedroom == ['8'] or bedroom == ['8 ห้อง']:
            if bedroom_option.text == '8 ห้อง':
                bedroom_option.click()  # select() in earlier versions of webdriver
                break
        elif bedroom == ['9'] or bedroom == ['9 ห้อง']:
            if bedroom_option.text == '9 ห้อง':
                bedroom_option.click()  # select() in earlier versions of webdriver
                break
        elif bedroom == ['10'] or bedroom == ['10 ห้อง']:
            if bedroom_option.text == '10 ห้อง':
                bedroom_option.click()  # select() in earlier versions of webdriver
                break
        elif bedroom == ['มากกว่า 10'] or bedroom == ['มากกว่า 10']:
            if bedroom_option.text == 'มากกว่า 10':
                bedroom_option.click()  # select() in earlier versions of webdriver
                break
##########################################Bedrooms#########################################################
##########################################Bathrooms#########################################################
    wd.find_element(By.ID, 'select2-web_bathroom-container').click()
    bathroom_el = wd.find_element(By.ID, 'web_bathroom')
    for bathroom_option in bathroom_el.find_elements_by_tag_name('option'):
        if toilet == ['1'] or toilet == ['1 ห้องน้ำ']:
            if bathroom_option.text == '1 ห้องน้ำ':
                bathroom_option.click()  # select() in earlier versions of webdriver
                break
        elif toilet == ['2'] or toilet == ['2 ห้องน้ำ']:
            if bathroom_option.text == '2 ห้องน้ำ':
                bathroom_option.click()  # select() in earlier versions of webdriver
                break
        elif toilet == ['3'] or toilet == ['3 ห้องน้ำ']:
            if bathroom_option.text == '3 ห้องน้ำ':
                bathroom_option.click()  # select() in earlier versions of webdriver
                break
        elif toilet == ['4'] or toilet == ['4 ห้องน้ำ']:
            if bathroom_option.text == '4 ห้องน้ำ':
                bathroom_option.click()  # select() in earlier versions of webdriver
                break
        elif toilet == ['5'] or toilet == ['5 ห้องน้ำ']:
            if bathroom_option.text == '5 ห้องน้ำ':
                bathroom_option.click()  # select() in earlier versions of webdriver
                break
        elif toilet == ['มากกว่า 5']:
            if bathroom_option.text == 'มากกว่า 5':
                bathroom_option.click()  # select() in earlier versions of webdriver
                break
        else:
            if bathroom_option.text == '1 ห้องน้ำ':
                bathroom_option.click()  # select() in earlier versions of webdriver
                break

##########################################Bathrooms#########################################################
##########################################Level#########################################################
    wd.find_element(By.ID, 'select2-web_floor-container').click()
    level_el = wd.find_element(By.ID, 'web_floor')
    for level_option in level_el.find_elements_by_tag_name('option'):
        if level_option.text == '1':
            level_option.click()  # select() in earlier versions of webdriver
            break

##########################################Level#########################################################
##########################################area#########################################################
    wd.find_element(By.ID, 'web_area_size').send_keys(max_area[0])

##########################################area#########################################################
##########################################Selling price#########################################################
    wd.find_element(By.ID, 'web_price').send_keys(f_price[0])

##########################################Selling price#########################################################
##########################################Special Additional#########################################################

    # wd.find_element(By.XPATH, '//*[@id="web_keeping_pet"]').click()
    # wd.find_element(By.XPATH, '//*[@id="topic_duplex"]').click()
    # wd.find_element(By.XPATH, '//*[@id="topic_penthouse"]').click()

##########################################Special Additional#########################################################
##########################################Matterport URL#########################################################
    # wd.find_element(By.ID, 'web_matterport').send_keys('1')

##########################################Matterport URL#########################################################
##########################################Youtube URL#########################################################
    # wd.find_element(By.ID, 'web_youtube').send_keys('1')

##########################################Youtube URL#########################################################
##########################################picture#########################################################
    for n_img in range(int(len(galleryUrls))):
        wd.find_element(By.ID, 'fileupload').send_keys(galleryUrls[n_img])
##########################################picture#########################################################
    wd.find_element(By.XPATH, '//*[@id="post_data_main"]/div[8]/div/div/div/button[2]').click()
    wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="post_data"]/div[1]/div/div[2]/div')))
    wd.find_element(By.XPATH, '//*[@id="post_data"]/div[1]/div/div[2]/div').click()
    wd.find_element(By.XPATH,'//*[@id="post_data"]/div[3]/button').click()

    # wd.find_element(By.CLASS_NAME, 'web_post_accept').click()
    # wd.find_element(By.XPATH, '//*[@id="post_data"]/div[3]/button').click()

###################################PAGE2###################################


def house_rent_page2():
    buildingList_el = wd.find_element_by_id('buildingList')
    for buildingList_option in buildingList_el.find_elements_by_tag_name('option'):
        if buildingList_option.text == 'บ้าน':
            time.sleep(2)
            buildingList_option.click()  # select() in earlier versions of webdriver
            break

#########################ทำเล#######################################################
    # check if
    time.sleep(2)
    # wd.execute_script("document.getElementById('div_web_project_id').style.display='block';")
    wd.find_element(By.XPATH, '//*[@id="post_data"]/div[1]/div[7]/span/span[1]/span').click()
    wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/span/span/span[1]/input')))
    wd.find_element(By.XPATH, '/html/body/span/span/span[1]/input').send_keys("จตุจักร")
    time.sleep(2)
    wd.find_element(By.XPATH, '//*[@id="select2-web_zone_id-results"]/li').click()
    time.sleep(1)

    # area =
    # area.click()

#########################ทำเล#######################################################
#########################map#######################################################
    wd.find_element(By.ID, 'posmap').click()

#########################map#######################################################
    wd.find_element_by_tag_name('body').send_keys(Keys.CONTROL + Keys.END)
    wd.find_element(By.XPATH, '//*[@id="post_data"]/div[3]/div[3]/div/div/button').click()
    time.sleep(2)
###################################PAGE1###################################
###################################PAGE2###################################
###########################################Bedrooms#########################################################
    wait.until(EC.element_to_be_clickable((By.ID, "select2-web_room-container")))
    wd.find_element(By.ID, 'select2-web_room-container').click()
    bedroom_el = wd.find_element(By.ID, 'web_room')
    for bedroom_option in bedroom_el.find_elements_by_tag_name('option'):
        if bedroom == ['1'] or bedroom == ['1 ห้อง']:
            if bedroom_option.text == '1 ห้อง':
                bedroom_option.click()  # select() in earlier versions of webdriver
                break
        elif bedroom == ['2'] or bedroom == ['2 ห้อง']:
            if bedroom_option.text == '2 ห้อง':
                bedroom_option.click()  # select() in earlier versions of webdriver
                break
        elif bedroom == ['3'] or bedroom == ['3 ห้อง']:
            if bedroom_option.text == '3 ห้อง':
                bedroom_option.click()  # select() in earlier versions of webdriver
                break
        elif bedroom == ['4'] or bedroom == ['4 ห้อง']:
            if bedroom_option.text == '4 ห้อง':
                bedroom_option.click()  # select() in earlier versions of webdriver
                break
        elif bedroom == ['5'] or bedroom == ['5 ห้อง']:
            if bedroom_option.text == '5 ห้อง':
                bedroom_option.click()  # select() in earlier versions of webdriver
                break
        elif bedroom == ['6'] or bedroom == ['6 ห้อง']:
            if bedroom_option.text == '6 ห้อง':
                bedroom_option.click()  # select() in earlier versions of webdriver
                break
        elif bedroom == ['7'] or bedroom == ['7 ห้อง']:
            if bedroom_option.text == '7 ห้อง':
                bedroom_option.click()  # select() in earlier versions of webdriver
                break
        elif bedroom == ['8'] or bedroom == ['8 ห้อง']:
            if bedroom_option.text == '8 ห้อง':
                bedroom_option.click()  # select() in earlier versions of webdriver
                break
        elif bedroom == ['9'] or bedroom == ['9 ห้อง']:
            if bedroom_option.text == '9 ห้อง':
                bedroom_option.click()  # select() in earlier versions of webdriver
                break
        elif bedroom == ['10'] or bedroom == ['10 ห้อง']:
            if bedroom_option.text == '10 ห้อง':
                bedroom_option.click()  # select() in earlier versions of webdriver
                break
        elif bedroom == ['มากกว่า 10'] or bedroom == ['มากกว่า 10']:
            if bedroom_option.text == 'มากกว่า 10':
                bedroom_option.click()  # select() in earlier versions of webdriver
                break
##########################################Bedrooms#########################################################
##########################################Bathrooms#########################################################
    wd.find_element(By.ID, 'select2-web_bathroom-container').click()
    bathroom_el = wd.find_element(By.ID, 'web_bathroom')
    for bathroom_option in bathroom_el.find_elements_by_tag_name('option'):
        if toilet == ['1'] or toilet == ['1 ห้องน้ำ']:
            if bathroom_option.text == '1 ห้องน้ำ':
                bathroom_option.click()  # select() in earlier versions of webdriver
                break
        elif toilet == ['2'] or toilet == ['2 ห้องน้ำ']:
            if bathroom_option.text == '2 ห้องน้ำ':
                bathroom_option.click()  # select() in earlier versions of webdriver
                break
        elif toilet == ['3'] or toilet == ['3 ห้องน้ำ']:
            if bathroom_option.text == '3 ห้องน้ำ':
                bathroom_option.click()  # select() in earlier versions of webdriver
                break
        elif toilet == ['4'] or toilet == ['4 ห้องน้ำ']:
            if bathroom_option.text == '4 ห้องน้ำ':
                bathroom_option.click()  # select() in earlier versions of webdriver
                break
        elif toilet == ['5'] or toilet == ['5 ห้องน้ำ']:
            if bathroom_option.text == '5 ห้องน้ำ':
                bathroom_option.click()  # select() in earlier versions of webdriver
                break
        elif toilet == ['มากกว่า 5']:
            if bathroom_option.text == 'มากกว่า 5':
                bathroom_option.click()  # select() in earlier versions of webdriver
                break
        else:
            if bathroom_option.text == '1 ห้องน้ำ':
                bathroom_option.click()  # select() in earlier versions of webdriver
                break

##########################################Bathrooms#########################################################
##########################################Level#########################################################
    wd.find_element(By.ID, 'select2-web_floor-container').click()
    level_el = wd.find_element(By.ID, 'web_floor')
    for level_option in level_el.find_elements_by_tag_name('option'):
        if level_option.text == '1':
            level_option.click()  # select() in earlier versions of webdriver
            break

##########################################Level#########################################################
##########################################area#########################################################
    wd.find_element(By.ID, 'web_area_size').send_keys(max_area[0])

##########################################area#########################################################
##########################################Selling price#########################################################
    wd.find_element(By.ID, 'web_price').send_keys(f_price[0])

##########################################Selling price#########################################################
##########################################Special Additional#########################################################

    # wd.find_element(By.XPATH, '//*[@id="web_keeping_pet"]').click()
    # wd.find_element(By.XPATH, '//*[@id="topic_duplex"]').click()
    # wd.find_element(By.XPATH, '//*[@id="topic_penthouse"]').click()

##########################################Special Additional#########################################################
##########################################Matterport URL#########################################################
    # wd.find_element(By.ID, 'web_matterport').send_keys('1')

##########################################Matterport URL#########################################################
##########################################Youtube URL#########################################################
    # wd.find_element(By.ID, 'web_youtube').send_keys('1')

##########################################Youtube URL#########################################################
##########################################picture#########################################################
    for n_img in range(int(len(galleryUrls))):
        wd.find_element(By.ID, 'fileupload').send_keys(galleryUrls[n_img])
##########################################picture#########################################################
    wd.find_element(By.XPATH, '//*[@id="post_data_main"]/div[8]/div/div/div/button[2]').click()
    wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="post_data"]/div[1]/div/div[2]/div')))
    wd.find_element(By.XPATH, '//*[@id="post_data"]/div[1]/div/div[2]/div').click()
    wd.find_element(By.XPATH,'//*[@id="post_data"]/div[3]/button').click()

    # wd.find_element(By.CLASS_NAME, 'web_post_accept').click()
    # wd.find_element(By.XPATH, '//*[@id="post_data"]/div[3]/button').click()

###################################PAGE2###################################


###########################loop###############################################
# for data in doc:
#     clickpost()
#     fill_data()

###########################loop###############################################
################################################################

click_login()
query()
fill_login()
click_createpost()
fill_data()
# try:
#     fill_data()
# except Exception as e:
#     print(e)
################################################################

