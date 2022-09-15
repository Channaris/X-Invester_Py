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
#   myquery = {'name':'ไอดีโอ สาทร-ท่าพระ  ห้องว่าง ให้เช่า ❗️❗️ แอดไลน์ได้เลย Line ID: @condo789    (มี @ ด้วย)'}
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
url = "https://www.thaihometown.com/member/"

wd.get(url)
wait = WebDriverWait(wd, 10)
####url################################
##########################click_login################################################################
def click_login():
    wd.implicitly_wait(0.5)
    link = wd.find_element(By.ID, 'top_login')
    # link.click()
    # print("Click Login_Button")

# click_login()

##########################click_login##########################################

###############################fill_login##########################################
def fill_login():
    wd.implicitly_wait(0.5)
    wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="loginform"]/tbody/tr[2]/td[2]/input'))).send_keys("jatossob@gmail.com")
    wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="loginform"]/tbody/tr[3]/td[2]/input'))).send_keys("123456Zx")
    link = wd.find_element(By.XPATH, '//*[@id="loginform"]/tbody/tr[4]/td[2]/table/tbody/tr/td[1]')
    link.click()
    print("Click Login_Button finish")

###############################fill_login##########################################

#######################click_createpost#######################################
def click_createpost():
    time.sleep(5)
    # link = wd.find_element(By.XPATH, '//*[@id="Sfal"]/center/a')
    # print("found Createpost")
    # link.click()
    # print("Click Createpost")
    wd.get('https://www.thaihometown.com/addnew')
    
########################click_createpost######################################

################################fill_data####################################
def fill_data():
################ข้อมูลทั่วไป#######################################
    print(post_topic)
    wait.until(EC.element_to_be_clickable((By.ID, "headtitle")))#.send_keys(post_topic)#หัวข้อประกาศ
    # wait.until(EC.element_to_be_clickable((By.ID, "headtitle")))#.send_keys(post_topic)#หัวข้อประกาศ
    # headtitle = wd.find_element(By.ID,'headtitle')
    # wd.execute_script(JS_ADD_TEXT_TO_INPUT, headtitle, post_topic)
    # wait.until(EC.element_to_be_clickable((By.ID, "headtitle"))).send_keys(1)#หัวข้อประกาศ

    def headtitle_th():
        headtitle_th = wd.find_element(By.ID,"headtitle")
        pyperclip.copy(str(post_topic[0]))
        act = ActionChains(wd)
        act.send_keys_to_element(headtitle_th).key_down(Keys.CONTROL).send_keys("v").key_up(Keys.CONTROL).perform()
        wait.until(EC.element_to_be_clickable((By.ID, "headtitle"))).send_keys(1)#หัวข้อประกาศ
    headtitle_th()

    # wait.until(EC.element_to_be_clickable((By.ID, "ad_title")))#.send_keys(description)#รายละเอียดประกาศ
    # ad_title = wd.find_element(By.ID,'ad_title')
    # wd.execute_script(JS_ADD_TEXT_TO_INPUT, ad_title, description)

    def ad_title():
        ad_title = wd.find_element(By.ID,"ad_title")
        pyperclip.copy(str(description[0]))
        act = ActionChains(wd)
        act.send_keys_to_element(ad_title).key_down(Keys.CONTROL).send_keys("v").key_up(Keys.CONTROL).perform()
    ad_title()
    ################################ประเภทประกาศ######################################################
    print(list_type)
    selected_typepart = Select(wd.find_element_by_id ('typepart'))
    if list_type == ['sell'] or list_type == ['ขาย'] or ['sell'] in list_type or ['ขาย'] in list_type:
        selected_typepart.select_by_visible_text('ประกาศขาย')
    elif list_type == ['down'] or list_type == ['ประกาศขายดาวน์']:
        selected_typepart.select_by_visible_text('ประกาศขายดาวน์')
    elif list_type == ['rent'] or list_type == ['เช่า'] or ['rent'] in list_type or ['เช่า'] in list_type:
        selected_typepart.select_by_visible_text('ประกาศให้เช่า')
    elif list_type == ['rentandsell']:
        selected_typepart.select_by_visible_text('ประกาศขาย และให้เช่า')
    ################################ประเภทประกาศ######################################################
    ################################ประเภทอสังหาริมทรัพย์################################################property_typeselected_property_type = Select(wd.find_element_by_id ('typepart'))
    selected_property_type = Select(wd.find_element_by_id ('property_type'))
    # if typepart == "บ้านเดี่ยวหลังใหญ่":
    # selected_property_type.select_by_visible_text('บ้านเดี่ยวหลังใหญ่')
    print(str(property_type))
    if property_type[0] == "[ObjectId('62bd7104f0521b8890fe9a11')]":
        selected_property_type.select_by_visible_text('บ้าน')
    elif property_type[0] == "[ObjectId('62bd7104f0521b8890fe9a0f')]":
        selected_property_type.select_by_visible_text('คอนโดมิเนียม')
    elif property_type[0] == "[ObjectId('62bd7104f0521b8890fe9a15')]":
        selected_property_type.select_by_visible_text('ทาวน์โฮม 2-4 ชั้น')
    elif property_type[0] == "ทาวน์เฮ้าส์ 1-2 ชั้น":
        selected_property_type.select_by_visible_text('ทาวน์เฮ้าส์ 1-2 ชั้น')
    elif property_type[0] == "อพาร์ทเม้นท์":
        selected_property_type.select_by_visible_text('อพาร์ทเม้นท์')
    elif property_type[0] == "ทาวน์โฮม 2-4 ชั้น":
        selected_property_type.select_by_visible_text('ทาวน์โฮม 2-4 ชั้น')
    elif property_type[0] == "ตึกแถว / อาคารพาณิชย์":
        selected_property_type.select_by_visible_text('ตึกแถว / อาคารพาณิชย์')
    elif property_type[0] == "สำนักงาน":
        selected_property_type.select_by_visible_text('สำนักงาน')
    elif property_type[0] == "โฮมออฟฟิศ":
        selected_property_type.select_by_visible_text('โฮมออฟฟิศ')
    elif property_type[0] == "โรงงาน":
        selected_property_type.select_by_visible_text('โรงงาน')
    elif property_type[0] == "คลังสินค้า":
        selected_property_type.select_by_visible_text('คลังสินค้า')
    elif property_type[0] == "โกดัง / สโตร์":
        selected_property_type.select_by_visible_text('โกดัง / สโตร์')
    elif property_type[0] == "ขาย-เซ้ง ธุรกิจ | กิจการ | โรงแรม":
        selected_property_type.select_by_visible_text('ขาย-เซ้ง ธุรกิจ | กิจการ | โรงแรม')
    elif property_type[0] == "ที่ดิน":
        selected_property_type.select_by_visible_text('ที่ดิน')
    ################################ประเภทอสังหาริมทรัพย์######################################################
    ################################เนื้อที่######################################################
    wait.until(EC.element_to_be_clickable((By.ID, "property_area"))).send_keys(max_area[0])#เนื้อที่
    selected_property_sqm = Select(wd.find_element_by_id ('property_sqm'))
    # selected = Select(wd.find_element_by_id ('select2-results'))
    # if typepart == "ตรม":
    selected_property_sqm.select_by_value('1')#ตรม
    # # elif typepart == "ตรว":
    # selected_property_sqm.select_by_value('2')#ตรว
    # # elif typepart == "ไร่":
    # selected_property_sqm.select_by_value('3')#ไร่
    ################################เนื้อที่######################################################
    ################################พื้นที่ใช้สอย######################################################
    wait.until(EC.element_to_be_clickable((By.ID, "property_right_area"))).send_keys(max_area[0])#เนื้อที่
    property_right_area = Select(wd.find_element_by_id ('property_right_sqm'))
    # selected = Select(wd.find_element_by_id ('select2-results'))
    # if typepart == "ตรม":
    property_right_area.select_by_value('1')#ตรม
    # elif typepart == "ตรว":
    # property_right_area.select_by_value('2')#ตรว
    ################################พื้นที่ใช้สอย######################################################
    ################################จำนวนห้องนอน######################################################
    room1 = Select(wd.find_element_by_id ('room1'))

    print(bedroom)
    if [1] in bedroom:
        room1.select_by_value('1')
    elif [2] in bedroom:
        room1.select_by_value('2')
    elif [3] in bedroom:
        room1.select_by_value('3')
    elif [4] in bedroom:
        room1.select_by_value('4')
    else:
        print("else room1.select_by_value('1')")
        room1.select_by_value('1')
    ################################จำนวนห้องนอน######################################################
    ################################จำนวนห้องน้ำ######################################################
    room2 = Select(wd.find_element_by_id ('room2'))
    # selected = Select(wd.find_element_by_id ('select2-results'))
    # room1.select_by_value(nroom)
    if [1] in toilet:
        room2.select_by_value('1')
    elif [2] in toilet:
        room2.select_by_value('2')
    elif [3] in toilet:
        room2.select_by_value('3')
    elif [4] in toilet:
        room2.select_by_value('4')
    else:
        print("else room2.select_by_value('1')")
        room2.select_by_value('1')
    ################################จำนวนห้องน้ำ######################################################
    ################################เครื่องปรับอากาศ######################################################
    def conditioning():
        conditioning = Select(wd.find_element_by_name ('conditioning'))
        # # selected = Select(wd.find_element_by_id ('select2-results'))
        # # room1.select_by_value(nroom)
        # # if room1 == "1"
        # conditioning.select_by_value('1')
        # # if room1 == "2":
        # conditioning.select_by_value('2')
        # # elif room1 == "3":
        # conditioning.select_by_value('3')
        # # elif room1 == "4":
        # conditioning.select_by_value('4')
        # # elif room1 == "5":
        # conditioning.select_by_value('5')
        # # elif room1 == "6":
        # conditioning.select_by_value('6')
        # # elif room1 == "7":
        # conditioning.select_by_value('7')
        # # elif room1 == "8":
        # conditioning.select_by_value('8')
        # # elif room1 == "9":
        # conditioning.select_by_value('9')
        # # elif room1 == "10":
        # conditioning.select_by_value('10')
        conditioning = Select(wd.find_element_by_name ('conditioning'))

    ################################เครื่องปรับอากาศ######################################################
    ################################ที่จอดรถ######################################################
    def carpark():
        carpark = Select(wd.find_element_by_name ('carpark'))
        # # selected = Select(wd.find_element_by_id ('select2-results'))
        # # carpark.select_by_value(nroom)
        # # if carpark == "1"
        # carpark.select_by_value('1')
        # # if carpark == "2":
        # carpark.select_by_value('2')
        # # elif carpark == "3":
        # carpark.select_by_value('3')
        # # elif carpark == "4":
        # carpark.select_by_value('4')
        # # elif carpark == "5":
        # carpark.select_by_value('5')
        # # elif carpark == "6":
        # carpark.select_by_value('6')
        # # elif carpark == "7":
        # carpark.select_by_value('7')
        # # elif carpark == "8":
        # carpark.select_by_value('8')
        # # elif carpark == "9":
        # carpark.select_by_value('9')
        # # elif carpark == "10":
        # carpark.select_by_value('10')
        carpark = Select(wd.find_element_by_name ('carpark'))

    ################################ที่จอดรถ######################################################
    ################################เฟอร์นิเจอร์######################################################
    furniture1 = wd.find_element(By.ID,'furniture1')
    furniture2 = wd.find_element(By.ID,'furniture2')
    furniture3 = wd.find_element(By.ID,'furniture3')
    # if furniture =='มี':
    #     furniture1.click()
    # elif furniture =='ไม่มี':
    #     furniture2.click()
    # else:
    #     furniture3.click()
    furniture3.click()
    ################################เฟอร์นิเจอร์######################################################
    ################################เครื่องใช้ไฟฟ้า######################################################
    electric1 = wd.find_element(By.ID,'electric1')
    electric2 = wd.find_element(By.ID,'electric2')
    electric3 = wd.find_element(By.ID,'electric3')
    # if furniture =='มี':
    #     electric1.click()
    # elif furniture =='ไม่มี':
    #     electric2.click()
    # else:
    #     electric3.click()
    electric3.click()
    ################################เครื่องใช้ไฟฟ้า######################################################
    ################################การต่อเติมพื้นที่ใช้สอย######################################################

    ################################การต่อเติมพื้นที่ใช้สอย######################################################
    ################################สิ่งอำนวยความสะดวก######################################################

    ################################สิ่งอำนวยความสะดวก######################################################
    ################################ที่ตั้ง######################################################
    #bangkok
    if 'กรุงเทพมหานคร' in state:
        property_city_bkk = Select(wd.find_element_by_name ('property_city_bkk'))
        property_city_bkk.select_by_visible_text((city[0]))
        
    #bangkok
    #จังหวัดที่ตั้ง
    else:
        property_country_2 = Select(wd.find_element_by_name ('property_country_2'))
        property_country_2.select_by_visible_text((state[0]))
    # property_country_2.select_by_visible_text('อ่างทอง')


    #จังหวัดที่ตั้ง
    #อำเภอ
        property_city_2 = Select(wd.find_element_by_name ('property_city_2'))
        property_city_2.select_by_visible_text((city[0]))


    #อำเภอ

    ################################ที่ตั้ง######################################################
    ################################ขั้น2ราคา######################################################
    #ขาย
    if 'sell' in list_type:
        sell_price = wd.find_element(By.ID,'selling_price')
        sell_price.send_keys(f_price[0])
    #ขาย
    #เช่า
    elif 'rent' in list_type:
        rent_price = wd.find_element(By.ID,'rent_price')
        rent_price.send_keys(f_price[0])
        type_forrent = Select(wd.find_element_by_id ('type_forrent'))
        type_forrent.select_by_visible_text('ต่อเดือน')
    # type_forrent.select_by_visible_text('ต่อสัปดาห์')
    # type_forrent.select_by_visible_text('ต่อวัน')
    else:
        wd.find_element(By.NAME, 'notprice').click()
        
    #เช่า
    #ราคาต่อหน่อย
    # price_unit = wd.find_element(By.ID,'price_unit')
    # price_unit.send_keys('111')
    # typeunit1 = wd.find_element(By.ID,'typeunit1')
    # typeunit2 = wd.find_element(By.ID,'typeunit2')
    # typeunit3 = wd.find_element(By.ID,'typeunit3')
    # #check if
    # typeunit1.click()
    #ราคาต่อหน่อย

    ################################ขั้น2ราคา######################################################
    ################################ขั้น3######################################################
    def state3():
        # wd.find_element(By.ID, 'info0').click()
        # wd.find_element(By.ID, 'info1').click()
        # wd.find_element(By.ID, 'info2').click()
        # wd.find_element(By.ID, 'info3').click()
        # wd.find_element(By.ID, 'info4').click()
        # wd.find_element(By.ID, 'info5').click()
        # wd.find_element(By.ID, 'info6').click()
        # wd.find_element(By.ID, 'info7').click()
        # wd.find_element(By.ID, 'info8').click()
        # wd.find_element(By.ID, 'info9').click()
        # wd.find_element(By.ID, 'info10').click()
        # wd.find_element(By.ID, 'info11').click()
        # wd.find_element(By.ID, 'info12').click()
        # wd.find_element(By.ID, 'info13').click()
        # wd.find_element(By.ID, 'info14').click()
        # wd.find_element(By.ID, 'info15').click()
        # wd.find_element(By.ID, 'info16').click()
        # wd.find_element(By.ID, 'info17').click()
        # wd.find_element(By.ID, 'info18').click()
        # wd.find_element(By.ID, 'info19').click()
        # wd.find_element(By.ID, 'info20').click()
        # wd.find_element(By.ID, 'info21').click()
        # wd.find_element(By.ID, 'info22').click()
        # wd.find_element(By.ID, 'info23').click()
        # wd.find_element(By.ID, 'info24').click()
        # wd.find_element(By.ID, 'info25').click()
        # wd.find_element(By.ID, 'info26').click()
        # wd.find_element(By.ID, 'info27').click()
        wd.find_element(By.ID, 'info28').click()
        # wd.find_element(By.ID, 'info29').click()
        # wd.find_element(By.ID, 'info30').click()
        # wd.find_element(By.ID, 'info31').click()
        # wd.find_element(By.ID, 'info32').click()
        # wd.find_element(By.ID, 'info33').click()
        # wd.find_element(By.ID, 'info34').click()
        wd.find_element(By.ID, 'info35').click()
        # wd.find_element(By.ID, 'info36').click()
        # wd.find_element(By.ID, 'info37').click()
        # wd.find_element(By.ID, 'info38').click()
        # wd.find_element(By.ID, 'info39').click()
        # wd.find_element(By.ID, 'info40').click()
        # wd.find_element(By.ID, 'info41').click()
        # wd.find_element(By.ID, 'info42').click()
        # wd.find_element(By.ID, 'info43').click()
        # wd.find_element(By.ID, 'info44').click()
        # wd.find_element(By.ID, 'info45').click()
        wd.find_element(By.ID, 'info46').click()
        # wd.find_element(By.ID, 'info47').click()
        # wd.find_element(By.ID, 'info48').click()
        # wd.find_element(By.ID, 'info49').click()
        # wd.find_element(By.ID, 'info50').click()
        # wd.find_element(By.ID, 'info51').click()
        # wd.find_element(By.ID, 'info52').click()
        # wd.find_element(By.ID, 'info53').click()
        # wd.find_element(By.ID, 'info54').click()
        # wd.find_element(By.ID, 'info55').click()
        # wd.find_element(By.ID, 'info56').click()
        # wd.find_element(By.ID, 'info57').click()
        # wd.find_element(By.ID, 'info58').click()
        # wd.find_element(By.ID, 'info59').click()
        # wd.find_element(By.ID, 'info60').click()
        # wd.find_element(By.ID, 'info61').click()
        # wd.find_element(By.ID, 'info62').click()
        # wd.find_element(By.ID, 'info63').click()
        # wd.find_element(By.ID, 'info64').click()
        # wd.find_element(By.ID, 'info65').click()
        # wd.find_element(By.ID, 'info66').click()

        # wd.find_element(By.ID, 'info70').click()
        # wd.find_element(By.ID, 'info71').click()
        # wd.find_element(By.ID, 'info72').click()
        # wd.find_element(By.ID, 'info73').click()
        # wd.find_element(By.ID, 'info74').click()
        # wd.find_element(By.ID, 'info75').click()
        # wd.find_element(By.ID, 'info76').click()
        # wd.find_element(By.ID, 'info77').click()
        # wd.find_element(By.ID, 'info78').click()
        # wd.find_element(By.ID, 'info79').click()
        # wd.find_element(By.ID, 'info80').click()
        # wd.find_element(By.ID, 'info81').click()
        # wd.find_element(By.ID, 'info82').click()
        # wd.find_element(By.ID, 'info83').click()
        # wd.find_element(By.ID, 'info84').click()
        # wd.find_element(By.ID, 'info85').click()
        # wd.find_element(By.ID, 'info86').click()
        # wd.find_element(By.ID, 'info87').click()
        # wd.find_element(By.ID, 'info88').click()
        # wd.find_element(By.ID, 'info89').click()
        # wd.find_element(By.ID, 'info90').click()
        # wd.find_element(By.ID, 'info91').click()
        # wd.find_element(By.ID, 'info92').click()
        # wd.find_element(By.ID, 'info93').click()
        # wd.find_element(By.ID, 'info94').click()
        # wd.find_element(By.ID, 'info95').click()
        # wd.find_element(By.ID, 'info96').click()
        # wd.find_element(By.ID, 'info97').click()
        # wd.find_element(By.ID, 'info98').click()
        # wd.find_element(By.ID, 'info99').click()
        # wd.find_element(By.ID, 'info100').click()
        # wd.find_element(By.ID, 'info101').click()
        # wd.find_element(By.ID, 'info102').click()
        # wd.find_element(By.ID, 'info103').click()
        # wd.find_element(By.ID, 'info104').click()
        # wd.find_element(By.ID, 'info105').click()
        # wd.find_element(By.ID, 'info106').click()
        # wd.find_element(By.ID, 'info107').click()
        # wd.find_element(By.ID, 'info108').click()
        # wd.find_element(By.ID, 'info109').click()
        # wd.find_element(By.ID, 'info110').click()
        # wd.find_element(By.ID, 'info111').click()
        # wd.find_element(By.ID, 'info112').click()
        # wd.find_element(By.ID, 'info113').click()
        # wd.find_element(By.ID, 'info114').click()
        # wd.find_element(By.ID, 'info115').click()
        # wd.find_element(By.ID, 'info116').click()
        # wd.find_element(By.ID, 'info117').click()
        # wd.find_element(By.ID, 'info118').click()
        # wd.find_element(By.ID, 'info119').click()
        # wd.find_element(By.ID, 'info120').click()
        # wd.find_element(By.ID, 'info121').click()
        # wd.find_element(By.ID, 'info122').click()
        # wd.find_element(By.ID, 'info123').click()
        # wd.find_element(By.ID, 'info124').click()
        # wd.find_element(By.ID, 'info125').click()
        # wd.find_element(By.ID, 'info126').click()
        # wd.find_element(By.ID, 'info127').click()
        # wd.find_element(By.ID, 'info128').click()
        # # wd.find_element(By.ID, 'info129').click()
        # # wd.find_element(By.ID, 'info130').click()
        # # wd.find_element(By.ID, 'info131').click()
        # # wd.find_element(By.ID, 'info132').click()
        # # wd.find_element(By.ID, 'info133').click()
        # # wd.find_element(By.ID, 'info134').click()
        wd.find_element(By.ID, 'info67').click()
        wd.find_element(By.ID, 'info68').click()
        wd.find_element(By.ID, 'info69').click()
    state3()
    ################################ขั้น3######################################################
    ################################captcha######################################################
    captcha_src = wd.find_element_by_xpath('//*[@id="inAddnew"]/table/tbody/tr[5]/td/table/tbody/tr/td/div[1]/img').get_attribute("src")

    captcha = captcha_src.split('=')[1]

    wd.find_element(By.ID, 'string1').send_keys(captcha)
    ################################captcha######################################################
    #########################################################
    wd.find_element(By.ID, 'imgSubmitForm').click()
    time.sleep(3)
    try:
        wd.switch_to.alert.accept()
        print(wd.switch_to.alert.text)
    except:
        print('pass')
    # if wd.switch_to.alert.text == '*** กรุณาแก้ไขหัวข้อประกาศ ใช้ซ้ำ!! กับประกาศรายการอื่น ***':
    #     print('*** กรุณาแก้ไขหัวข้อประกาศ ใช้ซ้ำ!! กับประกาศรายการอื่น ***')
    # img_button = 
    time.sleep(25)
    #########################################################


############################picture###########################################
    wd.find_element(By.XPATH, '//*[@id="sample"]/div[1]').click()
    wi_XPATH =  '/html/body/input[{}]'
    for n_img in range(int(len(galleryUrls))):
    # int_img = int(len(img))
    # wd.find_element(By.ID, 'upload_image1').click()
        wd.find_element(By.XPATH, wi_XPATH.format(n_img+1)).send_keys(galleryUrls[n_img])
    print('upload_image1')

    # wd.find_element(By.XPATH, '//*[@id="link_update"]/a').click()
    # start_tab = wd.current_window_handle
    # wd.switch_to.window(wd.window_handles[1])#เปลี่ยนแท็ป
    # bi_XPATH = '//*[@id="imag{}"]'
    # for b_img in range(int(len(galleryUrls))):
    #     wd.find_element(By.XPATH, bi_XPATH.format(b_img+1)).click()
    # wd.find_element(By.XPATH, '/html/body/table/tbody/tr[1]/td/input').click()



############################picture###########################################
############################map###########################################
    wd.find_element(By.XPATH,'//*[@id="mainbody"]/h3[2]/div/div[2]/a/div').click()
    tht_tab = wd.current_window_handle
    wd.find_element(By.XPATH, '/html/body/div[2]/div[2]/table/tbody/tr[1]/td/a').click()
    all_handles = wd.window_handles
#เปลี่ยนแท็ป
    for handle in all_handles:
        if handle != tht_tab:
            wd.switch_to.window(handle)
            wd.get('https://www.google.co.th/maps')

            wd.find_element(By.XPATH, '//*[@id="searchboxinput"]').send_keys(address[0])
            wd.find_element(By.XPATH, '//*[@id="searchbox-searchbutton"]').click()
            print('clicksearch')
            time.sleep(3)
            try:
                wd.find_element(By.XPATH, '//*[@id="QA0Szd"]/div/div/div[1]/div[2]/div/div[1]/div/div/div[4]/div[5]/button').click()
                print('clickshare')
                time.sleep(2)
                wd.find_element(By.XPATH, '//*[@id="modal-dialog"]/div/div[2]/div/div[3]/div/div/div[1]/div[2]/button[2]').click()
                print('clickiframe')
                time.sleep(1)
                wd.find_element(By.XPATH, '//*[@id="modal-dialog"]/div/div[2]/div/div[3]/div/div/div/div[3]/div[1]/button[2]').click()
                print('clickcopyiframe')
                time.sleep(1)
                try:
                    wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@id="Ng57nc"]/div/button')))
                    wd.find_element(By.XPATH,'//*[@id="Ng57nc"]/div/button').click()
                except:
                    wd.find_element(By.XPATH, '//*[@id="modal-dialog"]/div/div[2]/div/div[3]/div/div/div/div[3]/div[1]/button[2]').click()
                    print('clickcopyiframe')
                    time.sleep(1)

                   

            except:
                wd.find_element(By.XPATH, '//*[@id="QA0Szd"]/div/div/div[1]/div[2]/div/div[1]/div/div/div[2]/div[1]/div[3]/div/a').click()
                print('click1')
                time.sleep(2)
                wd.find_element(By.XPATH, '//*[@id="QA0Szd"]/div/div/div[1]/div[3]/div/div[1]/div/div/div[2]/div[4]/div[5]/button').click()
                print('clickshare')
                time.sleep(2)
                wd.find_element(By.XPATH, '//*[@id="modal-dialog"]/div/div[2]/div/div[3]/div/div/div[1]/div[2]/button[2]').click()
                print('clickiframe')
                time.sleep(1)
                wd.find_element(By.XPATH, '//*[@id="modal-dialog"]/div/div[2]/div/div[3]/div/div/div/div[3]/div[1]/button[2]').click()
                print('clickcopyiframe')

#เปลี่ยนแท็ป
    wd.switch_to.window(tht_tab)

    wd.find_element(By.ID, 'iframemaps').send_keys(Keys.CONTROL, 'v')
    wd.find_element(By.ID, 'Submit_SEND').click()
    wd.find_element(By.ID, 'Submit_FORM').click()





############################map###########################################

#     WebDriverWait(wd, 10).until(EC.element_to_be_clickable((By.XPATH,"//label[@for='agreement']"))).click()
#     print("agreement.click()")
#     post_button = wd.find_element(By.XPATH, '//*[@id="__next"]/div/div[2]/div[2]/div/form/div/div/button')
#     time.sleep(5)
#     post_button.click()
#     print("Posted")

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
################################################################

def map():
    wd.get('www.google.com')


