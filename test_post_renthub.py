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
url = "https://www.renthub.in.th/"

wd.get(url)
wait = WebDriverWait(wd, 10)
####url################################
##########################click_login################################################################
def click_login():
    wd.implicitly_wait(10)
    # login_button = WebDriverWait(wd, 10).until(EC.element_to_be_clickable(EC.element_to_be_clickable(By.XPATH, '//*[@id="__next"]/div/header/div/span[1]'))
    # login_button.click()
    time.sleep(3)
    link = wd.find_element(By.XPATH, '//*[@id="__next"]/div[1]/div[3]/div/div[2]/span[1]')
    link.click()
    print("Click Login_Button")

# click_login()

##########################click_login##########################################

###############################fill_login##########################################
def fill_login():
    wd.implicitly_wait(0.5)
    wait.until(EC.element_to_be_clickable((By.NAME, 'email'))).send_keys("testgingging@gmail.com")
    wait.until(EC.element_to_be_clickable((By.NAME, "password"))).send_keys("qwerty123456Zx")
    link = wd.find_element(By.XPATH, '/html/body/reach-portal/div/div/div[2]/div[2]/div/div[2]/div/div/div[1]/div/form/div/button')
    link.click()
    print("Click Login_Button finish")

###############################fill_login##########################################

#######################click_createpost#######################################
def click_createpost():
    time.sleep(5)
    wd.get('https://dashboard.renthub.in.th/members/listings/new')
    
########################click_createpost######################################

################################fill_data####################################
def fill_data():
    time.sleep(5)
    # close_button = wd.find_element(By.XPATH, '/html/body/reach-portal/div/div/div[2]/div/div/form/button')
    # close_button.click()
    # print("close_announce_button")

#################ข้อมูลที่พัก#######################################
    wait.until(EC.element_to_be_clickable((By.NAME, "name.th")))#.send_keys(post_topic)

    def headtitle_th():
        headtitle_th = wd.find_element(By.NAME, "name.th")
        pyperclip.copy(str(post_topic[0]))
        act = ActionChains(wd)
        act.send_keys_to_element(headtitle_th).key_down(Keys.CONTROL).send_keys("v").key_up(Keys.CONTROL).perform()
        wd.find_element(By.NAME,'name.th').send_keys(4)

    headtitle_th()

    def headtitle_en():
        headtitle_en = wd.find_element(By.NAME,'title.en')
        pyperclip.copy(str(post_topic[0]))
        act = ActionChains(wd)
        act.send_keys_to_element(headtitle_en).key_down(Keys.CONTROL).send_keys("v").key_up(Keys.CONTROL).perform()
        wd.find_element(By.NAME,'name.en').send_keys(4)
    # headtitle_en()
    # # wait.until(EC.element_to_be_clickable((By.NAME, "name.th"))).send_keys('ประกาศขาย 26/8/65')
    # wait.until(EC.element_to_be_clickable((By.NAME, "name.en"))).send_keys(post_topic)
    # # wait.until(EC.element_to_be_clickable((By.NAME, "name.en"))).send_keys('sell post at 26/8/65')
    wait.until(EC.element_to_be_clickable((By.NAME, "houseNumber.th"))).send_keys("0123")
    wait.until(EC.element_to_be_clickable((By.NAME, "road.th"))).send_keys("ถนนกก")
    wait.until(EC.element_to_be_clickable((By.NAME, "street.th"))).send_keys("ซอยกก")
    # wait.until(EC.element_to_be_clickable((By.NAME, "houseNumber.en"))).send_keys("test(English)12345657891011121311415161718")
    # wait.until(EC.element_to_be_clickable((By.NAME, "road.en"))).send_keys("test(English)12345657891011121311415161718")
    # wait.until(EC.element_to_be_clickable((By.NAME, "street.en"))).send_keys("test(English)12345657891011121311415161718")

#จังหวัด
    wd.find_element(By.XPATH,'//*[@class = "css-1k30fl1"][1]').click()

    # wd.find_element(By.XPATH,'//span[contains(text(),"เลือกจังหวัด")]').click()

    # wd.find_element(By.XPATH,'//*[@id="button--listbox-input--2"]').click()
    def list_provinces():
        KBI=wd.find_element(By.XPATH,'//*[@id="option-81--listbox-input--2"]')#กระบี่
        BKK=wd.find_element(By.XPATH,'//*[@id="option-10--listbox-input--2"]')#กรุงเทพมหานคร
        KRI=wd.find_element(By.XPATH,'//*[@id="option-71--listbox-input--2"]')#กาญจนบุรี
        KSN=wd.find_element(By.XPATH,'//*[@id="option-46--listbox-input--2"]')#กาฬสินธุ์
        KPT=wd.find_element(By.XPATH,'//*[@id="option-62--listbox-input--2"]')#กำแพงเพชร
        KKN=wd.find_element(By.XPATH,'//*[@id="option-40--listbox-input--2"]')#ขอนแก่น
        CTI=wd.find_element(By.XPATH,'//*[@id="option-22--listbox-input--2"]')#จันทบุรี
        CCO=wd.find_element(By.XPATH,'//*[@id="option-24--listbox-input--2"]')#ฉะเชิงเทรา
        CBI=wd.find_element(By.XPATH,'//*[@id="option-20--listbox-input--2"]')#ชลบุรี
        CNT=wd.find_element(By.XPATH,'//*[@id="option-18--listbox-input--2"]')#ชัยนาท
        CPM=wd.find_element(By.XPATH,'//*[@id="option-36--listbox-input--2"]')#ชัยภูมิ
        CRI=wd.find_element(By.XPATH,'//*[@id="option-57--listbox-input--2"]')#เชียงราย
        CMI=wd.find_element(By.XPATH,'//*[@id="option-50--listbox-input--2"]')#เชียงใหม่
        CPN=wd.find_element(By.XPATH,'//*[@id="option-86--listbox-input--2"]')#ชุมพร
        TRG=wd.find_element(By.XPATH,'//*[@id="option-92--listbox-input--2"]')#ตรัง
        TRT=wd.find_element(By.XPATH,'//*[@id="option-23--listbox-input--2"]')#ตราด
        TAK=wd.find_element(By.XPATH,'//*[@id="option-63--listbox-input--2"]')#ตาก
        NYK=wd.find_element(By.XPATH,'//*[@id="option-26--listbox-input--2"]')#นครนายก
        NPT=wd.find_element(By.XPATH,'//*[@id="option-73--listbox-input--2"]')#นครปฐม
        NPM=wd.find_element(By.XPATH,'//*[@id="option-48--listbox-input--2"]')#นครพนม
        NMA=wd.find_element(By.XPATH,'//*[@id="option-30--listbox-input--2"]')#นครราชสีมา
        NST=wd.find_element(By.XPATH,'//*[@id="option-80--listbox-input--2"]')#นครศรีธรรมราช
        NSN=wd.find_element(By.XPATH,'//*[@id="option-60--listbox-input--2"]')#นครสวรรค์
        NBI=wd.find_element(By.XPATH,'//*[@id="option-12--listbox-input--2"]')#นนทบุรี
        NWT=wd.find_element(By.XPATH,'//*[@id="option-96--listbox-input--2"]')#นราธิวาส
        NAN=wd.find_element(By.XPATH,'//*[@id="option-55--listbox-input--2"]')#น่าน
        BRM=wd.find_element(By.XPATH,'//*[@id="option-31--listbox-input--2"]')#บุรีรัมย์
        BKN=wd.find_element(By.XPATH,'//*[@id="option-38--listbox-input--2"]')#บึงกาฬ
        PTE=wd.find_element(By.XPATH,'//*[@id="option-13--listbox-input--2"]')#ปทุมธานี
        PKN=wd.find_element(By.XPATH,'//*[@id="option-77--listbox-input--2"]')#ประจวบคีรีขันธ์
        PRI=wd.find_element(By.XPATH,'//*[@id="option-25--listbox-input--2"]')#ปราจีนบุรี
        PTN=wd.find_element(By.XPATH,'//*[@id="option-94--listbox-input--2"]')#ปัตตานี
        PBI=wd.find_element(By.XPATH,'//*[@id="option-76--listbox-input--2"]')#เพชรบุรี
        PNB=wd.find_element(By.XPATH,'//*[@id="option-67--listbox-input--2"]')#เพชรบูรณ์
        AYA=wd.find_element(By.XPATH,'//*[@id="option-14--listbox-input--2"]')#พระนครศรีอยุธยา
        PRE=wd.find_element(By.XPATH,'//*[@id="option-54--listbox-input--2"]')#แพร่
        PYO=wd.find_element(By.XPATH,'//*[@id="option-56--listbox-input--2"]')#พะเยา
        PNA=wd.find_element(By.XPATH,'//*[@id="option-82--listbox-input--2"]')#พังงา
        PLG=wd.find_element(By.XPATH,'//*[@id="option-93--listbox-input--2"]')#พัทลุง
        PCT=wd.find_element(By.XPATH,'//*[@id="option-66--listbox-input--2"]')#พิจิตร
        PLK=wd.find_element(By.XPATH,'//*[@id="option-65--listbox-input--2"]')#พิษณุโลก
        PKT=wd.find_element(By.XPATH,'//*[@id="option-83--listbox-input--2"]')#ภูเก็ต
        MKM=wd.find_element(By.XPATH,'//*[@id="option-44--listbox-input--2"]')#มหาสารคาม
        MDH=wd.find_element(By.XPATH,'//*[@id="option-49--listbox-input--2"]')#มุกดาหาร
        MSN=wd.find_element(By.XPATH,'//*[@id="option-58--listbox-input--2"]')#แม่ฮ่องสอน
        YST=wd.find_element(By.XPATH,'//*[@id="option-35--listbox-input--2"]')#ยโสธร
        YLA=wd.find_element(By.XPATH,'//*[@id="option-95--listbox-input--2"]')#ยะลา
        RET=wd.find_element(By.XPATH,'//*[@id="option-45--listbox-input--2"]')#ร้อยเอ็ด
        RNG=wd.find_element(By.XPATH,'//*[@id="option-85--listbox-input--2"]')#ระนอง
        RYG=wd.find_element(By.XPATH,'//*[@id="option-21--listbox-input--2"]')#ระยอง
        RBR=wd.find_element(By.XPATH,'//*[@id="option-70--listbox-input--2"]')#ราชบุรี
        LRI=wd.find_element(By.XPATH,'//*[@id="option-16--listbox-input--2"]')#ลพบุรี
        LEI=wd.find_element(By.XPATH,'//*[@id="option-42--listbox-input--2"]')#เลย
        LPG=wd.find_element(By.XPATH,'//*[@id="option-52--listbox-input--2"]')#ลำปาง
        LPN=wd.find_element(By.XPATH,'//*[@id="option-51--listbox-input--2"]')#ลำพูน
        SSK=wd.find_element(By.XPATH,'//*[@id="option-33--listbox-input--2"]')#ศรีสะเกษ
        SNK=wd.find_element(By.XPATH,'//*[@id="option-47--listbox-input--2"]')#สกลนคร
        SKA=wd.find_element(By.XPATH,'//*[@id="option-90--listbox-input--2"]')#สงขลา
        STN=wd.find_element(By.XPATH,'//*[@id="option-91--listbox-input--2"]')#สตูล
        SPK=wd.find_element(By.XPATH,'//*[@id="option-11--listbox-input--2"]')#สมุทรปราการ
        SKM=wd.find_element(By.XPATH,'//*[@id="option-75--listbox-input--2"]')#สมุทรสงคราม
        SKN=wd.find_element(By.XPATH,'//*[@id="option-74--listbox-input--2"]')#สมุทรสาคร
        SKW=wd.find_element(By.XPATH,'//*[@id="option-27--listbox-input--2"]')#สระแก้ว
        SRI=wd.find_element(By.XPATH,'//*[@id="option-19--listbox-input--2"]')#สระบุรี
        SBR=wd.find_element(By.XPATH,'//*[@id="option-17--listbox-input--2"]')#สิงห์บุรี
        STI=wd.find_element(By.XPATH,'//*[@id="option-64--listbox-input--2"]')#สุโขทัย
        SPB=wd.find_element(By.XPATH,'//*[@id="option-72--listbox-input--2"]')#สุพรรณบุรี
        SNI=wd.find_element(By.XPATH,'//*[@id="option-84--listbox-input--2"]')#สุราษฎร์ธานี
        SRN=wd.find_element(By.XPATH,'//*[@id="option-32--listbox-input--2"]')#สุรินทร์
        NKI=wd.find_element(By.XPATH,'//*[@id="option-43--listbox-input--2"]')#หนองคาย
        NBP=wd.find_element(By.XPATH,'//*[@id="option-39--listbox-input--2"]')#หนองบัวลำภู
        ATG=wd.find_element(By.XPATH,'//*[@id="option-15--listbox-input--2"]')#อ่างทอง
        ACR=wd.find_element(By.XPATH,'//*[@id="option-37--listbox-input--2"]')#อำนาจเจริญ
        UDN=wd.find_element(By.XPATH,'//*[@id="option-41--listbox-input--2"]')#อุดรธานี
        UTT=wd.find_element(By.XPATH,'//*[@id="option-53--listbox-input--2"]')#อุตรดิตถ์
        UTI=wd.find_element(By.XPATH,'//*[@id="option-61--listbox-input--2"]')#อุทัยธานี
        UBN=wd.find_element(By.XPATH,'//*[@id="option-34--listbox-input--2"]')#อุบลราชธานี

    # if province == 'กรุงเทพมหานคร':
    #     BKK.click()
    wd.find_element(By.XPATH,province_xpath.format(state[0])).click()
    
#จังหวัด
#อำเภอ//*[@id="button--listbox-input--154"]
    # wd.find_element(By.XPATH,'//span[contains(text(),"เขต")]').click()
    # wd.find_element(By.CLASS_NAME,'css-1k30fl1').click()
    # wd.find_element(By.XPATH,'//*[@html-for="districtCode"]/div[1]').click()
    # select_district = wd.find_element(By.XPATH,'//span[contains(text(),"เลือกจังหวัด")]').send_keys(Keys.TAB)
    time.sleep(1)
    wd.find_element(By.XPATH,'/html/body/div[1]/div[2]/div/div[1]/form/div/div[1]/div/div[3]/div[8]/div/div/span').click()
#//*[@class = "css-1g2auqy]/div[8]/div/div/span
#//*[@id="districtCode"]/div/span
    time.sleep(1)
    wd.find_element(By.XPATH,district_xpath.format(city[0])).click()

    # time.sleep(30)
    # wd.find_element(By.XPATH,'//ul[li/@data-value=1001]').click()

    # wd.find_element(By.XPATH,'//li[contains(text(),"ดุสิต")]').click()

#อำเภอ
#ตำบล
    time.sleep(2)
    wd.find_element(By.XPATH, '/html/body/div[1]/div[2]/div/div[1]/form/div/div[1]/div/div[3]/div[9]/div/div/span').click()
    time.sleep(2)
    wd.find_element(By.XPATH, '/html/body/div[1]/div[2]/div/div[1]/form/div/div[1]/div/div[3]/div[9]/div/div/div[2]/ul').click()

    # wd.find_element(By.XPATH,'//span[contains(text(),"เลือกตำบล")]').click()
    # # wd.find_element(By.XPATH, '/html/body/div[1]/div[2]/div/div[1]/form/div/div[1]/div/div[3]/div[9]/div/div/span').click()
    # try:
    #     wd.find_element(By.XPATH,subdistrict_xpath.format(city[0])).click()
    # except:
    #     wd.find_element(By.XPATH, '/html/body/div[1]/div[2]/div/div[1]/form/div/div[1]/div/div[3]/div[9]/div/div/div[2]/ul').click()

    # wd.find_element(By.XPATH,'//li[contains(text(),"ดุสิต")]').click()

#ตำบล
    # time.sleep(5)

    # wait.until(EC.element_to_be_clickable((By.NAME, "postCode"))).send_keys("10001")
    wd.find_element(By.XPATH,'//*[@id="__next"]/div[2]/div/div[1]/form/div/div[1]/div/div[3]/div[11]/div[1]/button').click()
#################ข้อมูลที่พัก#######################################
#################สิ่งอำนวยควมสะดวก#######################################
    def facilities():
        wd.find_element(By.XPATH, '//*[@id="amenities.hasAir"]').click()
        wd.find_element(By.XPATH, '//*[@id="amenities.hasAir"]').click()

        wd.find_element(By.XPATH, '//*[@id="amenities.hasFurniture"]').click()
        wd.find_element(By.XPATH, '//*[@id="amenities.allowPet"]').click()
        wd.find_element(By.XPATH, '//*[@id="amenities.hasWaterHeater"]').click()
        wd.find_element(By.XPATH, '//*[@id="amenities.hasFan"]').click()
        wd.find_element(By.XPATH, '//*[@id="amenities.hasTV"]').click()
        wd.find_element(By.XPATH, '//*[@id="amenities.hasRefrigerator"]').click()
        wd.find_element(By.XPATH, '//*[@id="amenities.allowSmoking"]').click()
        wd.find_element(By.XPATH, '//*[@id="amenities.hasPhone"]').click()
        wd.find_element(By.XPATH, '//*[@id="amenities.hasParking"]').click()
        wd.find_element(By.XPATH, '//*[@id="amenities.hasBicycleParking"]').click()
        wd.find_element(By.XPATH, '//*[@id="amenities.hasLift"]').click()
        wd.find_element(By.XPATH, '//*[@id="amenities.hasPool"]').click()
        wd.find_element(By.XPATH, '//*[@id="amenities.hasFitness"]').click()
        wd.find_element(By.XPATH, '//*[@id="amenities.hasInternet"]').click()
        wd.find_element(By.XPATH, '//*[@id="amenities.hasCableTV"]').click()
        wd.find_element(By.XPATH, '//*[@id="amenities.hasKeyCardAccess"]').click()
        wd.find_element(By.XPATH, '//*[@id="amenities.hasFingerPrintAccess"]').click()
        wd.find_element(By.XPATH, '//*[@id="amenities.hasCCTV"]').click()
        wd.find_element(By.XPATH, '//*[@id="amenities.hasSecurity"]').click()
        wd.find_element(By.XPATH, '//*[@id="amenities.hasRestaurant"]').click()
        wd.find_element(By.XPATH, '//*[@id="amenities.hasShop"]').click()
        wd.find_element(By.XPATH, '//*[@id="amenities.hasLaundry"]').click()
        wd.find_element(By.XPATH, '//*[@id="amenities.hasSalon"]').click()
        wd.find_element(By.XPATH, '//*[@id="amenities.hasEvCharger"]').click()

#################สิ่งอำนวยควมสะดวก#######################################
##########################################check_ifรูปแบบห้อง#########################################################
    if property_type[0] == [ObjectId('62bd7104f0521b8890fe9a0f')]:
        wd.find_element(By.XPATH, '//*[@id="__next"]/div[2]/div/div[1]/form/div/div[3]/div/table/tbody/tr/td[1]/div[1]/div/input').send_keys('คอนโด')
    else:
        wd.find_element(By.XPATH, '//*[@id="__next"]/div[2]/div/div[1]/form/div/div[3]/div/table/tbody/tr/td[1]/div[1]/div/input').send_keys('ที่พัก')

    print(property_type)
    print(bedroom)
    
    wd.find_element(By.XPATH, '/html/body/div[1]/div[2]/div/div[1]/form/div/div[3]/div/table/tbody/tr/td[2]/div/div/span').click()
    if property_type == ['สตูดิโอ']:
        wd.find_element(By.XPATH, '//*[@id="option-STUDIO--listbox-input--5"]').click()#
        print("if property_type == ['สตูดิโอ']:")
    elif bedroom == ['1'] or bedroom == ['1 ห้อง']:
        wd.find_element(By.XPATH, '//*[@id="option-ONE_BED_ROOM--listbox-input--5"]').click()#
        print("[1] in bedroom:")
    elif bedroom == ['2'] or bedroom == ['2 ห้อง']:
        wd.find_element(By.XPATH, '//*[@id="option-TWO_BED_ROOM--listbox-input--5"]').click()#
        print("[2] in bedroom:")
    elif bedroom == ['3'] or bedroom == ['3 ห้อง']:
        wd.find_element(By.XPATH, '//*[@id="option-THREE_BED_ROOM--listbox-input--5"]').click()#
        print("[3] in bedroom:")
    elif bedroom == ['4'] or bedroom == ['4 ห้อง']:
        wd.find_element(By.XPATH, '//*[@id="option-FOUR_BED_ROOM--listbox-input--5"]').click()#
        print("[4] in bedroom:")
    elif bedroom == ['5'] or bedroom == ['5 ห้อง']:
        wd.find_element(By.XPATH, '//*[@id="option-FIVE_BED_ROOM--listbox-input--5"]').click()#
        print("[5] in bedroom:")
    else:
        wd.find_element(By.XPATH, '//*[@id="option-STUDIO--listbox-input--5"]').click()#
        print("[else] in bedroom:")


##########################################################################################################
##########################################check_ifขนาดห้อง#########################################################
    wait.until(EC.element_to_be_clickable((By.NAME, "rooms[0].minSize"))).send_keys(max_area[0].split(' ')[0])

##########################################check_ifขนาดห้อง#########################################################
##########################################check_ifเช่ารายเดือน (บาท/เดือน)#########################################################
    wd.find_element(By.ID, 'button--listbox-input--6').click()
    wait.until(EC.element_to_be_clickable((By.ID, 'option-AMOUNT--listbox-input--6')))
    wd.find_element(By.ID, 'option-AMOUNT--listbox-input--6').click()

    try:
        try:
            wait.until(EC.element_to_be_clickable((By.NAME, "rooms[0].price.monthly.minPrice"))).send_keys(s_price[0].replace('ราคาเช่า','').replace('บาท/เดือน',''))
        except:
            wait.until(EC.element_to_be_clickable((By.NAME, "rooms[0].price.monthly.minPrice"))).send_keys(s_price[0])
    except:
        try:
            wait.until(EC.element_to_be_clickable((By.NAME, "rooms[0].price.monthly.minPrice"))).send_keys(f_price[0].replace('ราคาเช่า','').replace('บาท/เดือน',''))
        except:
            wait.until(EC.element_to_be_clickable((By.NAME, "rooms[0].price.monthly.minPrice"))).send_keys(f_price[0])

    try:
        wait.until(EC.element_to_be_clickable((By.NAME, "rooms[0].price.monthly.maxPrice"))).send_keys(f_price[0].replace('ราคาเช่า','').replace('บาท/เดือน',''))
    except:
        wait.until(EC.element_to_be_clickable((By.NAME, "rooms[0].price.monthly.maxPrice"))).send_keys(f_price[0])

##########################################check_ifเช่ารายเดือน (บาท/เดือน)#########################################################
##########################################check_ifเช่ารายวัน#########################################################
    wd.find_element(By.ID, 'button--listbox-input--7').click()
    wait.until(EC.element_to_be_clickable((By.ID, 'option-CALL--listbox-input--7')))
    wd.find_element(By.ID, 'option-CALL--listbox-input--7').click()
##########################################check_ifเช่ารายวัน#########################################################
#################ค่าใช้จ่าย#######################################
#ค่าน้ำ
    wd.find_element(By.XPATH, '//*[@id="__next"]/div[2]/div/div[1]/form/div/div[4]/div/div[1]/label[6]/input').click()
#ค่าไฟ
    wd.find_element(By.XPATH, '//*[@id="__next"]/div[2]/div/div[1]/form/div/div[4]/div/div[2]/label[4]/input').click()
#ค่าบริการอื่นๆ
    wd.find_element(By.XPATH, '//*[@id="__next"]/div[2]/div/div[1]/form/div/div[4]/div/div[3]/label[3]/input').click()
#เงินมัดจำ/ประกัน
    wd.find_element(By.XPATH, '//*[@id="__next"]/div[2]/div/div[1]/form/div/div[4]/div/div[4]/label[4]/input').click()
#จ่ายล่วงหน้า
    wd.find_element(By.XPATH, '//*[@id="__next"]/div[2]/div/div[1]/form/div/div[4]/div/div[5]/label[4]/input').click()
#ค่าโทรศัพท์
    wd.find_element(By.XPATH, '//*[@id="__next"]/div[2]/div/div[1]/form/div/div[4]/div/div[6]/label[4]/input').click()
#อินเทอร์เน็ต
    wd.find_element(By.XPATH, '//*[@id="__next"]/div[2]/div/div[1]/form/div/div[4]/div/div[7]/label[4]/input').click()

#################ค่าใช้จ่าย#######################################
#################รายละเอียด#######################################
    # wd.find_element(By.XPATH, '//*[@id="__next"]/div[2]/div/div[1]/form/div/div[5]/div/div[1]/div/div/div/div[2]/div[1]').send_keys(description[0])
    # wd.find_element(By.XPATH, '//*[@id="__next"]/div[2]/div/div[1]/form/div/div[5]/div/div[2]/div/div/div/div[2]/div[1]').send_keys('test')
    def ad_title_th():
        ad_title_th = wd.find_element(By.XPATH,'//*[@id="__next"]/div[2]/div/div[1]/form/div/div[5]/div/div[1]/div/div/div/div[2]/div[1]')
        pyperclip.copy(str(description[0]))
        act = ActionChains(wd)
        act.send_keys_to_element(ad_title_th).key_down(Keys.CONTROL).send_keys("v").key_up(Keys.CONTROL).perform()
    ad_title_th()

    def ad_title_en():
        ad_title_en = wd.find_element(By.XPATH,'//*[@id="__next"]/div[2]/div/div[1]/form/div/div[5]/div/div[1]/div/div/div/div[2]/div[1]')
        pyperclip.copy(str(description[0]))
        act = ActionChains(wd)
        act.send_keys_to_element(ad_title_en).key_down(Keys.CONTROL).send_keys("v").key_up(Keys.CONTROL).perform()
    ad_title_en()
#################รายละเอียด#######################################
#################รูปภาพ#######################################
    for n_img in range(int(len(galleryUrls))):
        wd.find_element(By.XPATH, '//*[@id="__next"]/div[2]/div/div[1]/form/div/div[6]/div/div/input').send_keys(galleryUrls[n_img])
    # wd.find_element(By.XPATH, '//*[@id="__next"]/div[2]/div/div[1]/form/div/div[6]/div/div/input').send_keys("D:\\work\\web_scraping\\test_pic\\404_1.JPEG")
    
#################รูปภาพ#######################################
#################โปรโมชั่น#######################################
    wd.find_element(By.XPATH, '//*[@id="__next"]/div[2]/div/div[1]/form/div/div[7]/div/div[1]/label[3]/input').click()

#################โปรโมชั่น#######################################
#################ข้อมูลสำหรับติดต่อ#######################################
    wd.find_element(By.NAME, 'contactInformation[0].name').send_keys('test')
    wd.find_element(By.NAME, 'contactInformation[0].phone[0]').send_keys('029009000-4 ต่อ 0')
    wd.find_element(By.XPATH, '//*[@id="__next"]/div[2]/div/div[1]/form/div/div[8]/div/div/div[3]/button').click()
    wd.find_element(By.NAME, 'contactInformation[0].phone[1]').send_keys('029009000-4 ต่อ 0')
    # wd.find_element(By.CLASS_NAME, 'css-89q0b2 e1661y350').click()
    # wd.find_element(By.NAME, 'contactInformation[0].phone[2]').send_keys('029009000-4 ต่อ 0')
    wd.find_element(By.NAME, 'contactInformation[0].email').send_keys('mailusedfortest@gmail.com')
    wd.find_element(By.NAME, 'contactInformation[0].lineId').send_keys('029009000-4 ต่อ 0')

#################ข้อมูลสำหรับติดต่อ#######################################
#################ลงประกาศ#######################################
    wd.find_element(By.XPATH, '//*[@id="__next"]/div[2]/div/div[1]/form/div/button').click()
    time.sleep(1)
    wd.find_element(By.XPATH, '//*[@id="checkNameEn"]/div/div/label').click()

    wd.find_element(By.XPATH, '//*[@id="__next"]/div[2]/div/div[1]/form/div/button').click()
    print("click Posted")
    time.sleep(1)
    if wd.current_url == 'https://dashboard.renthub.in.th/members/listings':
        try:
            for n_img in range(int(len(galleryUrls))):#เอกสารที่พัก
                wd.find_element(By.XPATH, '//*[@id="__next"]/div[2]/div[2]/ul/li[1]/div/div[2]/div[3]/ul/li[1]/div[2]/form/div/div/input').send_keys(galleryUrls[n_img])
            for n_img in range(int(len(galleryUrls))):#รูปถ่ายเลขที่บ้าน
                wd.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[2]/ul/li[1]/div/div[2]/div[3]/ul/li[2]/div[2]/form/div/div/input').send_keys(galleryUrls[n_img])
            print("finish")
        except:
            print("finish")
    elif wd.current_url == 'https://dashboard.renthub.in.th/members/listings/new':
        print("cannot post")

#################ลงประกาศ#######################################
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
# if ['rent'] in list_type or ['เช่า'] in list_type:
#     fill_login()
#     click_createpost()
#     fill_data()
# else:
#     print('renthub only rent')
# try:
#     fill_data()
# except Exception as e:
#     print(e)
################################################################

