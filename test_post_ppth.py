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
import pyperclip

################################################################

PATH = "D:\\work\\web_scraping\\program\\chromedriver.exe"
# PATH = "D:\\work\\web_scraping\\program\\geckodriver.exe"

# os.environ['webdriver.chrome.driver'] = PATH
# wd = webdriver.Firefox(PATH)
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

##########################query################################################################

##End of db zone###
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
url = "https://propertyhub.in.th/"

wd.get(url)
wait = WebDriverWait(wd, 10)
####url################################
##########################click_login################################################################
def click_login():
    wd.implicitly_wait(10)
    # login_button = WebDriverWait(wd, 10).until(EC.element_to_be_clickable(EC.element_to_be_clickable(By.XPATH, '//*[@id="__next"]/div/header/div/span[1]'))
    # login_button.click()
    time.sleep(3)
    link = wd.find_element(By.XPATH, '//*[@id="__next"]/div/header/div/span[1]')
    link.click()
    print("Click Login_Button")

# click_login()

##########################click_login##########################################

###############################fill_login##########################################
def fill_login():
    wd.implicitly_wait(0.5)
    #0961599447
    wait.until(EC.element_to_be_clickable((By.NAME, 'email'))).send_keys("testgingging@gmail.com")
    wait.until(EC.element_to_be_clickable((By.NAME, "password"))).send_keys("qwerty123456Zx")
    link = wd.find_element(By.XPATH, '/html/body/div[4]/div/div/div/div[2]/div/div/div[1]/form/div/div/button')
    link.click()
    print("Click Login_Button finish")

###############################fill_login##########################################

#######################click_createpost#######################################
def click_createpost():
    time.sleep(5)
    link = wd.find_element(By.XPATH, '//*[@id="__next"]/div/header/div/a[5]')
    print("found Createpost")
    link.click()
    print("Click Createpost")
    
########################click_createpost######################################

################################fill_data####################################
def fill_data():
    time.sleep(5)
    # close_button = wd.find_element(By.XPATH, '/html/body/reach-portal/div/div/div[2]/div/div/form/button')
    # close_button.click()
    # print("close_announce_button")

################ข้อมูลทั่วไป#######################################
    wait.until(EC.element_to_be_clickable((By.NAME, "title.th")))#.send_keys(post_topic)

    def headtitle_th():
        headtitle_th = wd.find_element(By.XPATH,'//*[@id="__next"]/div/div[2]/div[2]/div/form/div/div/div[1]/div[1]/div[1]/div/input')
        pyperclip.copy(str(post_topic[0]))
        act = ActionChains(wd)
        act.send_keys_to_element(headtitle_th).key_down(Keys.CONTROL).send_keys("v").key_up(Keys.CONTROL).perform()
    headtitle_th()

    def headtitle_en():
        headtitle_en = wd.find_element(By.NAME,'title.en')
        pyperclip.copy(str(post_topic[0]))
        act = ActionChains(wd)
        act.send_keys_to_element(headtitle_en).key_down(Keys.CONTROL).send_keys("v").key_up(Keys.CONTROL).perform()
    # headtitle_en()

    wd.find_element(By.XPATH, '/html/body/div[1]/div/div[2]/div[2]/div/form/div/div/div[1]/div[3]/div[1]/div/div[1]/input').click()
    wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="projectId"]/div/div[1]/input'))).send_keys(address[0])
    project_name = wd.find_element(By.XPATH, '//*[@id="listbox--1"]/li[1]')
    project_name.click()
    
    # wait.until(EC.element_to_be_clickable((By.NAME, "roomInformation.building"))).send_keys("testอาคาร")

##########################################check_ifรูปแบบห้อง#########################################################
    wd.find_element(By.XPATH, '//*[@id="button--listbox-input--2"]').click()#
    select_property_type = wd.find_element(By.XPATH, '//*[@id="button--listbox-input--2"]/span')
    # select_type = Select(building_type)
    # type_list = select_type.options
    # for ele in type_list:
    #     print(ele.text)
    
    # wd.find_element(By.XPATH, '//*[@id="button--listbox-input--2"]').click()
    if property_type == ['สตูดิโอ']:
        wd.find_element(By.XPATH, '//*[@id="option-STUDIO--listbox-input--2"]').click()#
    elif [1] in bedroom:
        wd.find_element(By.XPATH, '//*[@id="option-ONE_BED_ROOM--listbox-input--2"]').click()#
    elif [2] in bedroom:
        wd.find_element(By.XPATH, '//*[@id="option-TWO_BED_ROOM--listbox-input--2"]').click()#
    elif [3] in bedroom:
        wd.find_element(By.XPATH, '//*[@id="option-THREE_BED_ROOM--listbox-input--2"]').click()#
    elif [4] in bedroom:
        wd.find_element(By.XPATH, '//*[@id="option-FOUR_BED_ROOM--listbox-input--2"]').click()#
    elif [5] in bedroom:
        wd.find_element(By.XPATH, '//*[@id="option-FIVE_BED_ROOM--listbox-input--2"]').click()#
    elif [6] in bedroom:
        wd.find_element(By.XPATH, '//*[@id="option-SIX_BED_ROOM--listbox-input--2"]').click()#
    elif ['Moff'] in bedroom:
        wd.find_element(By.XPATH, '//*[@id="option-MOFF--listbox-input--2"]').click()#
    elif ['Duplex'] in bedroom:
        wd.find_element(By.XPATH, '//*[@id="option-DUPLEX_ONE_BED--listbox-input--2"]').click()#
    elif ['Duplex 2 ห้องนอน'] in bedroom:
        wd.find_element(By.XPATH, '//*[@id="option-DUPLEX_TWO_BED--listbox-input--2"]').click()#
    elif ['Duplex 3 ห้องนอน'] in bedroom:
        wd.find_element(By.XPATH, '//*[@id="option-DUPLEX_TWO_BED--listbox-input--2"]').click()#
    elif ['Duplex 4 ห้องนอน'] in bedroom:
        wd.find_element(By.XPATH, '//*[@id="option-DUPLEX_TWO_BED--listbox-input--2"]').click()#
    elif ['Duplex 5 ห้องนอน'] in bedroom:
        wd.find_element(By.XPATH, '//*[@id="option-DUPLEX_TWO_BED--listbox-input--2"]').click()#    
    elif ['Penthouse'] in bedroom:
        wd.find_element(By.XPATH, '//*[@id="option-PENTHOUSE--listbox-input--2"]').click()#
    elif ['Villa'] in bedroom:
        wd.find_element(By.XPATH, '//*[@id="option-VILLA--listbox-input--2"]').click()#
    else:
        wd.find_element(By.XPATH, '//*[@id="option-STUDIO--listbox-input--2"]').click()#

##########################################################################################################
##########################################check_ifรูปแบบห้อง#########################################################

#     wait.until(EC.element_to_be_clickable((By.NAME, "roomInformation.roomHomeAddress"))).send_keys("testบ้านเลขที่ห้อง")
#     wait.until(EC.element_to_be_clickable((By.NAME, "roomInformation.roomNumber"))).send_keys("testหมายเลขห้อง")
    wait.until(EC.element_to_be_clickable((By.NAME, "roomInformation.onFloor"))).send_keys("1-100")

# ##########################################check_ifทิศทางห้อง#########################################################
#     wd.find_element(By.XPATH, '//*[@id="button--listbox-input--3"]/span').click()
#     room_direction = wd.find_element(By.XPATH, '//*[@id="option-NORTH--listbox-input--3"]')

# ##########################################################################################################
#     room_direction.click()
##########################################check_ifทิศทางห้อง#########################################################

    wait.until(EC.element_to_be_clickable((By.NAME, "roomInformation.numberOfBed"))).send_keys(bedroom[0].split(' ')[0])
    try:
        wait.until(EC.element_to_be_clickable((By.NAME, "roomInformation.numberOfBath"))).send_keys(toilet[0].split(' ')[0])
    except:
        wait.until(EC.element_to_be_clickable((By.NAME, "roomInformation.numberOfBath"))).send_keys(1)
    wait.until(EC.element_to_be_clickable((By.NAME, "roomInformation.roomArea"))).send_keys(max_area[0].split(' ')[0])
    wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/div/div[2]/div[2]/div/form/div/div/div[1]/div[3]/div[4]/div/div/div/div[2]/div[1]/p'))).send_keys("บันทึกช่วยจำ สำหรับเจ้าของประกาศ ไม่แสดงในหน้าประกาศ")

# ################ข้อมูลทั่วไป#######################################


#################################ประเภทประกาศ#######################################################################
    
    post_type = wd.find_element(By.XPATH,'//*[@id="postType"]')
    post_type.click()
    
####################################เช่า##############################
    if list_type == ['rent'] or list_type == ['เช่า'] or ['rent'] in list_type or ['เช่า'] in list_type:
        def rent():
            wd.find_element(By.XPATH,'//*[@id="option-FOR_RENT--listbox-input--4"]').click()#
    #       rent = wd.find_element(By.XPATH,'//*[@id="option-FOR_RENT--listbox-input--4"]')
    #       print("find_rent")
    #       rent.click()

    # ###################################ค่าเช่าต่อเดือน#######################
            try:
                wait.until(EC.element_to_be_clickable((By.NAME, "price.forRent.monthly.price"))).send_keys(f_price[0].replace('ราคาเช่า','').replace('บาท/เดือน',''))
            except:
                wait.until(EC.element_to_be_clickable((By.NAME, "price.forRent.monthly.price"))).send_keys(f_price[0])

    # ###################################ค่าเช่าต่อเดือน#######################
    # ###################################ค่าเช่าต่อวัน#######################
            # wait.until(EC.element_to_be_clickable((By.NAME, "price.forRent.daily.price"))).send_keys("1")
            wd.find_element(By.XPATH, '//*[@id="__next"]/div/div[2]/div[2]/div/form/div/div/div[2]/div[2]/div/div/div[2]/div/div[2]/div/label/span').click()

    # ###################################ค่าเช่าต่อวัน#######################
    # ###################################เงินมัดจำ#######################
    #       wait.until(EC.element_to_be_clickable((By.NAME, "price.forRent.deposit.amount"))).send_keys("1")
            wd.find_element(By.XPATH, '//*[@id="__next"]/div/div[2]/div[2]/div/form/div/div/div[2]/div[2]/div/div/div[3]/div/div[3]/div/label/span').click()
    ###################################เงินมัดจำ#######################
    ###################################จ่ายล่วงหน้า#######################
            # wait.until(EC.element_to_be_clickable((By.NAME, "price.forRent.advancePayment.amount"))).send_keys("1")
            wd.find_element(By.XPATH, '//*[@id="__next"]/div/div[2]/div[2]/div/form/div/div/div[2]/div[2]/div/div/div[4]/div/div[3]/div/label/span').click()

###################################จ่ายล่วงหน้า#######################
####################################เช่า##############################
        rent()
####################################ขาย##############################
    elif list_type == ['sell'] or list_type == ['ขาย'] or ['sell'] in list_type or ['ขาย'] in list_type:
    
        def sell():
            wd.find_element(By.XPATH,'//*[@id="option-FOR_SALE--listbox-input--4"]').click()#

            try:
                wait.until(EC.element_to_be_clickable((By.NAME, "price.forSale.price"))).send_keys(f_price[0].replace('ราคาขาย','').replace('บาท',''))
            except:
                wait.until(EC.element_to_be_clickable((By.NAME, "price.forSale.price"))).send_keys(f_price[0])

            # clickcall = wd.find_element(By.XPATH, '//*[@id="__next"]/div/div[2]/div[2]/div/form/div/div/div[2]/div[2]/div/div[1]/div/div[2]/div')
            # clickcall.click()

    ################################sale_with_tenant#############################################   
        # sale_with_tenant = wd.find_element(By.XPATH, '//*[@id="__next"]/div/div[2]/div[2]/div/form/div/div/div[2]/div[2]/div/div[2]/div/span')
        # sale_with_tenant.click()
        # print(sale_with_tenant)
    
################################sale_with_tenant#############################################   
####################################ขาย##############################
        sell()
#################################ประเภทประกาศ#######################################################################
##############################สิ่งอำนวยความสะดวกในห้อง########################################################

    # WebDriverWait(wd, 10).until(EC.element_to_be_clickable((By.XPATH,"//*[@id='__next']/div/div[2]/div[2]/div/form/div/div/div[3]/div[2]/div[1]/span"))).click()###เฟอร์นิเจอร์
    # WebDriverWait(wd, 10).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="__next"]/div/div[2]/div[2]/div/form/div/div/div[3]/div[2]/div[2]/span'))).click()###โทรศัพท์บ้าน
    # WebDriverWait(wd, 10).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="__next"]/div/div[2]/div[2]/div/form/div/div/div[3]/div[2]/div[3]/span'))).click()###เครื่องปรับอากาศ
    # WebDriverWait(wd, 10).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="__next"]/div/div[2]/div[2]/div/form/div/div/div[3]/div[2]/div[4]/span'))).click()###เครื่องทำน้ำร้อน/น้ำอุ่น
    # WebDriverWait(wd, 10).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="__next"]/div/div[2]/div[2]/div/form/div/div/div[3]/div[2]/div[5]/span'))).click()###ประตูห้องระบบ digital lock
    # WebDriverWait(wd, 10).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="__next"]/div/div[2]/div[2]/div/form/div/div/div[3]/div[2]/div[6]/span'))).click()###อ่างอาบน้ำ
    # WebDriverWait(wd, 10).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="__next"]/div/div[2]/div[2]/div/form/div/div/div[3]/div[2]/div[7]/span'))).click()###TV
    # WebDriverWait(wd, 10).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="__next"]/div/div[2]/div[2]/div/form/div/div/div[3]/div[2]/div[8]/span'))).click()###เตาปรุงอาหาร
    # WebDriverWait(wd, 10).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="__next"]/div/div[2]/div[2]/div/form/div/div/div[3]/div[2]/div[9]/span'))).click()###ตู้เย็น
    # WebDriverWait(wd, 10).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="__next"]/div/div[2]/div[2]/div/form/div/div/div[3]/div[2]/div[10]/span'))).click()###เครื่องดูดควัน
    # WebDriverWait(wd, 10).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="__next"]/div/div[2]/div[2]/div/form/div/div/div[3]/div[2]/div[11]/span'))).click()###อินเตอร์เน็ตไร้สาย (WIFI) ในห้อง
    # WebDriverWait(wd, 10).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="__next"]/div/div[2]/div[2]/div/form/div/div/div[3]/div[2]/div[12]/span'))).click()###เครื่องซักผ้า

##############################สิ่งอำนวยความสะดวกในห้อง########################################################

#########################################room##############################################################
    # image_list = ["D:\\work\\web_scraping\\test_pic\\404_1.png","D:\\work\\web_scraping\\test_pic\\404_2.png","D:\\work\\web_scraping\\test_pic\\404_3.png","D:\\work\\web_scraping\\test_pic\\404_4.png"]
    # for i in range(0, len(image_list)):
    for n_img in range(int(len(galleryUrls))):
        wd.find_element(By.XPATH, '//*[@id="__next"]/div/div[2]/div[2]/div/form/div/div/div[4]/div[3]/input').send_keys(galleryUrls[n_img])
    # wd.find_element(By.XPATH, '//*[@id="__next"]/div/div[2]/div[2]/div/form/div/div/div[4]/div[3]/input').send_keys("D:\\work\\web_scraping\\test_pic\\404_2.JPEG")

########################################room##############################################################
# ##########################################building##########################################################
#     wd.find_element(By.XPATH, '//*[@id="__next"]/div/div[2]/div[2]/div/form/div/div/div[4]/div[4]/input').send_keys("D:\\work\\web_scraping\\test_pic\\404_1.JPEG")
# ##########################################building##########################################################
# ##########################################similar image##########################################################
#     wd.find_element(By.XPATH, '//*[@id="__next"]/div/div[2]/div[2]/div/form/div/div/div[4]/div[5]/input').send_keys("D:\\work\\web_scraping\\test_pic\\404_1.JPEG")
# ##########################################similar image##########################################################

##############################รายละเอียด########################################################
    # des_th = wd.find_element(By.XPATH, '//*[@id="__next"]/div/div[2]/div[2]/div/form/div/div/div[5]/div[1]/div/div/div/div[2]/div[1]')
    # wd.execute_script(JS_ADD_TEXT_TO_INPUT, des_th, description)
    # des_en = wd.find_element(By.XPATH, '//*[@id="__next"]/div/div[2]/div[2]/div/form/div/div/div[5]/div[2]/div/div/div/div[2]/div[1]')
    # wd.execute_script(JS_ADD_TEXT_TO_INPUT, des_en, description)
    def des_th():
        des_th = wd.find_element(By.XPATH,'//*[@id="__next"]/div/div[2]/div[2]/div/form/div/div/div[5]/div[1]/div/div/div/div[2]/div[1]')
        pyperclip.copy(str(description[0]))
        act = ActionChains(wd)
        act.send_keys_to_element(des_th).key_down(Keys.CONTROL).send_keys("v").key_up(Keys.CONTROL).perform()
    des_th()

    def des_en():
        des_en = wd.find_element(By.XPATH,'//*[@id="__next"]/div/div[2]/div[2]/div/form/div/div/div[5]/div[2]/div/div/div/div[2]/div[1]')
        pyperclip.copy(str(description[0]))
        act = ActionChains(wd)
        act.send_keys_to_element(des_en).key_down(Keys.CONTROL).send_keys("v").key_up(Keys.CONTROL).perform()
    des_en()

# ##############################รายละเอียด########################################################

    WebDriverWait(wd, 10).until(EC.element_to_be_clickable((By.XPATH,"//label[@for='agreement']"))).click()
    print("agreement.click()")
    post_button = wd.find_element(By.XPATH, '//*[@id="__next"]/div/div[2]/div[2]/div/form/div/div/button')
    time.sleep(15)
    post_button.click()
    time.sleep(1)
    wd.find_element(By.XPATH, '//*[@id="__next"]/div/div[2]/div[2]/div/form/div/div/div[1]/div[2]/div[2]/div/div/label').click()
    wd.find_element(By.XPATH, '//*[@id="__next"]/div/div[2]/div[2]/div/form/div/div/div[3]/div[1]/div/div/div/label').click()
    post_button.click()
    print("click Posted")
    time.sleep(1)
    if wd.current_url == 'https://dashboard.propertyhub.in.th/members/listings/online':
        print("finish")
    elif wd.current_url == 'https://dashboard.propertyhub.in.th/members/listings/new':
        print("cannot post")

################################fill_data####################################
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

