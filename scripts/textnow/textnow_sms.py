 #-*-coding:utf-8-*-

from selenium import webdriver  
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import hashlib

#from webdriver_manager.chrome import ChromeDriverManager
#from selenium.webdriver.chrome.options import Options
import undetected_chromedriver.v2 as uc
#import undetected_chromedriver as uc

import os
import time
import json
import cfscrape
import importlib,sys
importlib.reload(sys)

class Textnow:  

  def __init__(self, PHONE_NUMBER, MESSAGE, TN_USER, TN_PASS, TN_COOKIE):
    self.TN_USER = TN_USER
    self.TN_PASS = TN_PASS
    self.TN_COOKIE = TN_COOKIE
    self.PHONE_NUMBER = PHONE_NUMBER
    self.MESSAGE = MESSAGE
    self.url = "https://www.textnow.com/login"
    self.msg_url = "https://www.textnow.com/messaging"

  def getDriver(self):
    #profile = webdriver.FirefoxProfile()
    #proxy = '127.0.0.1:10808'
    #ip, port = proxy.split(":")
    #port = int(port)
    ## 不使用代理的协议，注释掉对应的选项即可
    #settings = {
    #  'network.proxy.type': 1,
    #  'network.proxy.http': ip,
    #  'network.proxy.http_port': port,
    #  'network.proxy.ssl': ip,  # https的网站,
    #  'network.proxy.ssl_port': port,
    #}
    #
    ## 更新配置文件
    #for key, value in settings.items():
    #    profile.set_preference(key, value)
    #profile.update_preferences()
    
    #https://github.com/mozilla/geckodriver/releases
    options = webdriver.FirefoxOptions()
    options.add_argument('-headless')  # 无头参数
    options.add_argument('-private')  # 隐身模式
    driver = webdriver.Firefox(options=options)
    #
    #driver = webdriver.Firefox(executable_path='geckodriver', options=options)
    #driver = webdriver.Firefox(firefox_profile=profile, options=options)
    #driver = webdriver.Firefox(proxy = proxy)

    #https://sites.google.com/a/chromium.org/chromedriver/home
    #options = webdriver.ChromeOptions()
    #options.add_argument('--headless')# 无头参数
    #options.add_argument('--disable-web-security')# 禁用web安全参数
    #options.add_argument('--incognito')# 无痕参数
    #options.add_argument('--user-agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36"')# user-agent参数
    
    #chrome_driver = '/opt/hostedtoolcache/Python/3.7.9/x64/lib/python3.7/site-packages/seleniumbase-1.42.4-py3.7.egg/seleniumbase/drivers/chromedriver'  #chromedriver的文件位置
    #driver = webdriver.Chrome(executable_path = chrome_driver, chrome_options=options)   
    
    #这两种设置都进行才有效
    #driver.set_page_load_timeout(5)
    #driver.set_script_timeout(5)
    return driver
   
   
  def getDriverOther(self):
    print("进入谷歌驱动")
   #browser = uc.Chrome(version_main=98)
   #uc.TARGET_VERSION = 98
    #driver = uc.Chrome()
   #
    #chrome_options = uc.ChromeOptions()
    path_to_data_dir='/opt/hostedtoolcache/Python/3.8.12/x64'
    #options = webdriver.ChromeOptions() 
    #options.add_argument("start-maximized")
    #options.add_argument('--headless')
    #options.add_argument('--no-sandbox')
    #options.add_argument('--disable-dev-shm-usage')
    options = uc.ChromeOptions() 
    options.add_argument("start-maximized")
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
      
    options.add_argument('--disable-popup-blocking')
    # setting profile
    options.user_data_dir = path_to_data_dir

    # MAKE SURE YOU SWITCH THE VERSION OF CHROME TO YOUR VERSION , MY VERSION IS 99
    driver = uc.Chrome(options=options,version_main=99)
    #chrome_driver='/opt/hostedtoolcache/Python/3.8.12/x64/lib/python3.8/site-packages/seleniumbase-1.42.4-py3.8.egg/seleniumbase/drivers/chromedriver'
    #driver = uc.Chrome(executable_path = os.environ.get("CHROMEDRIVER_PATH"), options = options)
    
    

    #chrome_options.add_argument('--headless')# 无头参数
    #chrome_options.add_argument('--disable-web-security')# 禁用web安全参数
    #chrome_options.add_argument('--incognito')# 无痕参数
    #driver = uc.Chrome(options=chrome_options)
   # driver = uc.Chrome(executable_path = chrome_driver, chrome_options=options)
    return driver
   
  def getDriverTwo(self):
    print("进入驱动")
    scraper = cfscrape.create_scraper(delay = 10)
    return scraper
   
   
  def getChromeDriver(self):
     #chromedriver的文件位置
    chrome_driver='/opt/hostedtoolcache/Python/3.8.12/x64/lib/python3.8/site-packages/seleniumbase-1.42.4-py3.8.egg/seleniumbase/drivers/chromedriver'
    #options = webdriver.ChromeOptions()
    #options.add_argument('--headless')# 无头参数
    #options.add_argument('--disable-web-security')# 禁用web安全参数
    #options.add_argument('--incognito')# 无痕参数
    #driver = webdriver.Chrome(executable_path = chrome_driver, chrome_options=options)   
    chrome_options = webdriver.ChromeOptions()

    #options = webdriver.ChromeOptions()
# If options.headless = True, the website will not load
    chrome_options.headless = False
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')
    chrome_options.add_argument("--window-size=1920,1080") 
    chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
    chrome_options.add_experimental_option('useAutomationExtension', False)
    chrome_options.add_argument('--disable-blink-features=AutomationControlled')
    chrome_options.add_argument('user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36')

    driver = webdriver.Chrome(options = chrome_options)
    
    driver.execute_cdp_cmd('Page.addScriptToEvaluateOnNewDocument', {
    "source": '''
    Object.defineProperty(navigator, 'webdriver', {
        get: () => undefined
    });
    Object.defineProperty(navigator, 'plugins', {
            get: function() { return {"0":{"0":{}},"1":{"0":{}},"2":{"0":{},"1":{}}}; }
    });
    Object.defineProperty(navigator, 'languages', {
        get: () => ["en-US", "en"]
    });
    Object.defineProperty(navigator, 'mimeTypes', {
        get: function() { return {"0":{},"1":{},"2":{},"3":{}}; }
    });

    window.screenY=23;
    window.screenTop=23;
    window.outerWidth=1337;
    window.outerHeight=825;
    window.chrome =
    {
      app: {
        isInstalled: false,
      },
      webstore: {
        onInstallStageChanged: {},
        onDownloadProgress: {},
      },
      runtime: {
        PlatformOs: {
          MAC: 'mac',
          WIN: 'win',
          ANDROID: 'android',
          CROS: 'cros',
          LINUX: 'linux',
          OPENBSD: 'openbsd',
        },
        PlatformArch: {
          ARM: 'arm',
          X86_32: 'x86-32',
          X86_64: 'x86-64',
        },
        PlatformNaclArch: {
          ARM: 'arm',
          X86_32: 'x86-32',
          X86_64: 'x86-64',
        },
        RequestUpdateCheckStatus: {
          THROTTLED: 'throttled',
          NO_UPDATE: 'no_update',
          UPDATE_AVAILABLE: 'update_available',
        },
        OnInstalledReason: {
          INSTALL: 'install',
          UPDATE: 'update',
          CHROME_UPDATE: 'chrome_update',
          SHARED_MODULE_UPDATE: 'shared_module_update',
        },
        OnRestartRequiredReason: {
          APP_UPDATE: 'app_update',
          OS_UPDATE: 'os_update',
          PERIODIC: 'periodic',
        },
      },
    };
    window.navigator.chrome =
    {
      app: {
        isInstalled: false,
      },
      webstore: {
        onInstallStageChanged: {},
        onDownloadProgress: {},
      },
      runtime: {
        PlatformOs: {
          MAC: 'mac',
          WIN: 'win',
          ANDROID: 'android',
          CROS: 'cros',
          LINUX: 'linux',
          OPENBSD: 'openbsd',
        },
        PlatformArch: {
          ARM: 'arm',
          X86_32: 'x86-32',
          X86_64: 'x86-64',
        },
        PlatformNaclArch: {
          ARM: 'arm',
          X86_32: 'x86-32',
          X86_64: 'x86-64',
        },
        RequestUpdateCheckStatus: {
          THROTTLED: 'throttled',
          NO_UPDATE: 'no_update',
          UPDATE_AVAILABLE: 'update_available',
        },
        OnInstalledReason: {
          INSTALL: 'install',
          UPDATE: 'update',
          CHROME_UPDATE: 'chrome_update',
          SHARED_MODULE_UPDATE: 'shared_module_update',
        },
        OnRestartRequiredReason: {
          APP_UPDATE: 'app_update',
          OS_UPDATE: 'os_update',
          PERIODIC: 'periodic',
        },
      },
    };
    ['height', 'width'].forEach(property => {
        const imageDescriptor = Object.getOwnPropertyDescriptor(HTMLImageElement.prototype, property);

        // redefine the property with a patched descriptor
        Object.defineProperty(HTMLImageElement.prototype, property, {
            ...imageDescriptor,
            get: function() {
                // return an arbitrary non-zero dimension if the image failed to load
            if (this.complete && this.naturalHeight == 0) {
                return 20;
            }
                return imageDescriptor.get.apply(this);
            },
        });
    });

    const getParameter = WebGLRenderingContext.getParameter;
    WebGLRenderingContext.prototype.getParameter = function(parameter) {
        if (parameter === 37445) {
            return 'Intel Open Source Technology Center';
        }
        if (parameter === 37446) {
            return 'Mesa DRI Intel(R) Ivybridge Mobile ';
        }

        return getParameter(parameter);
    };

    const elementDescriptor = Object.getOwnPropertyDescriptor(HTMLElement.prototype, 'offsetHeight');

    Object.defineProperty(HTMLDivElement.prototype, 'offsetHeight', {
        ...elementDescriptor,
        get: function() {
            if (this.id === 'modernizr') {
            return 1;
            }
            return elementDescriptor.get.apply(this);
        },
    });
    '''
})
    #driver = webdriver.Chrome(executable_path = chrome_driver, options = chrome_options)
   
   
    return driver
   
   
   
   
   
    
  #从缓存文件中读取cookie
  def read_cookie(self):
    #每个账号固定一个md5，以防多个账号冲突
    md5 = hashlib.md5(self.TN_COOKIE.encode(encoding='UTF-8')).hexdigest()
    try:
      fr=open('.cache/' + md5 + '_cookies.json','r')
      cookies=json.load(fr)
      fr.close()
      return cookies
    except:
      return None 
      
  #保存cookie到缓存文件
  def write_cookie(self, driver):
    #每个账号固定一个md5，以防多个账号冲突
    md5 = hashlib.md5(self.TN_COOKIE.encode(encoding='UTF-8')).hexdigest()

    cookies=driver.get_cookies()
    try:
      fw=open('.cache/' + md5 + '_cookies.json','w')
      json.dump(cookies,fw)
      fw.close()
    except:
      return None 
  
  # 检查cookie是否正常
  def check_cookie(self, driver):
    url = self.msg_url
    try:
      driver.get(url)
    except:
      pass
      
    time.sleep(5)
    if driver.current_url == url:
      return True
    return False
    
  #登录
  def login(self, driver):
    
    try:
      driver.get(self.url)
    except:
      pass
      
    time.sleep(3)

    if self.TN_COOKIE:
      # 采用cookie登录
      
      success = False
      #优先读取缓存cookie文件
      cookies = self.read_cookie()
      if cookies:
        driver.delete_all_cookies()
        for cookie in cookies:
          if 'expiry' in cookie:
            del cookie['expiry']
          driver.add_cookie(cookie)
        #检测是否登录成功
        success = self.check_cookie(driver)
      
      if not success:
        #通过设定的cookie登录
        cookies=self.TN_COOKIE.split('; ')
        driver.delete_all_cookies()
        for cookie in cookies:
          key = cookie.split('=')[0]
          value = cookie.split('=')[1]
          driver.add_cookie({"name":key,"value":value})
        #检测是否登录成功
        success = self.check_cookie(driver)
      
      if success:
        print('登录成功')
        #保存最新的cookie到缓存文件
        self.write_cookie(driver)
        return success

      #采用用户名密码登录
          
      print('cookie登录失败，尝试用用户名密码登录')

      #presence_of_element_located： 当我们不关心元素是否可见，只关心元素是否存在在页面中。
      #visibility_of_element_located： 当我们需要找到元素，并且该元素也可见。
      
      WebDriverWait(driver, 3).until(EC.visibility_of_element_located((By.XPATH, "//input[@name='username']")))
      uname_box = driver.find_element_by_xpath("//input[@name='username']")
      pass_box = driver.find_element_by_xpath("//input[@name='password']")
      uname_box.send_keys(self.TN_USER)
      pass_box.send_keys(self.TN_PASS)

      login_btn = driver.find_element_by_xpath("//button[@type='submit']")
      login_btn.click()

    
    #显性等待，每隔3s检查一下条件是否成立
    try:
      WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, "//div[@class='notification-priming-modal']")))
    except:
      pass

    #检测是否登录成功
    success = self.check_cookie(driver)
    if success:
      print('登录成功')
      #保存最新的cookie到缓存文件
      self.write_cookie(driver)
    else:
      print('登录失败，请更换Cookie')
    
    return success
  
  def send_text(self):

    #driver = self.getDriverOther()
    driver = self.getChromeDriver()
    #driver = self.getDriverOther()
    if self.login(driver):

      # remove通知提示框
      driver.execute_script("document.querySelectorAll('#recent-header .toast-container').forEach(function(e,i){console.log(e.href)})")
      time.sleep(1)
     
      driver.execute_script("document.querySelectorAll('.notification-priming-modal').forEach(function(e,i){console.log(e.href)})")
      time.sleep(1)
      
      #检测jQuery是否存在，如果不存在，则手动加载一次
      driver.execute_script("if(!window.jQuery){var scriptEle=document.createElement('script');scriptEle.src='https://cdn.jsdelivr.net/gh/jquery/jquery@3.2.1/dist/jquery.min.js';document.body.append(scriptEle)}")
      time.sleep(3)
  #   current_html = driver.execute_script("return document.documentElement.outerHTML")
      time.sleep(10)
   #重新打开页面
 #   driver.get(self.msg_url)
#      scraper = cfscrape.create_scraper(delay = 10)
      web_data = driver.execute_script("return document.documentElement.outerHTML")
      print("输出当前页面内容")
      print(web_data)
 
      driver.execute_script("$('#recent-header .toast-container').remove();")
      driver.execute_script("$('.notification-priming-modal').remove();")
      driver.execute_script("$('.modal').remove();")
      time.sleep(2)
      
      for phone in self.PHONE_NUMBER.split(','):
        try:
        
          print (u'开始给%s发短信' % (phone.replace(''.join(list(phone)[-4:]),'****')))
          
          #点击 新建短信按钮
          try:
            new_text_btn = driver.find_element_by_id("newText")
            if new_text_btn.is_displayed():
              new_text_btn.click()
            else:
              driver.execute_script("arguments[0].scrollIntoView();", new_text_btn)
              if new_text_btn.is_displayed():
                new_text_btn.click()
              else:
                driver.execute_script("$(arguments[0]).click()", "#newText")
          except:
            driver.execute_script("$(arguments[0]).click()", "#newText")
            
          time.sleep(2)

          #输入：短信内容
          try:
            text_field = driver.find_element_by_id("text-input")
            if text_field.is_displayed():
              text_field.click()
              text_field.send_keys(self.MESSAGE)
            else:
              driver.execute_script("arguments[0].scrollIntoView();", text_field)
              if text_field.is_displayed():
                text_field.click()
                text_field.send_keys(self.MESSAGE)
              else:
                driver.execute_script("$(arguments[0]).val('arguments[1]')", "#text-input", self.MESSAGE)
          except:
              driver.execute_script("$(arguments[0]).val('arguments[1]')", "#text-input", self.MESSAGE)
          time.sleep(2)
          
          #输入号码
          try:
            number_field = driver.find_element_by_class_name("newConversationTextField")
            if number_field.is_displayed():
              number_field.send_keys(phone)
            else:
              driver.execute_script("arguments[0].scrollIntoView();", number_field)
              if number_field.is_displayed():
                number_field.send_keys(phone)
              else:
                driver.execute_script("$(arguments[0]).val('arguments[1]')", ".newConversationTextField", phone)
          except:
              driver.execute_script("$(arguments[0]).val('arguments[1]')", ".newConversationTextField", phone)
          time.sleep(10)

          #点击短信内容
          try:
            text_field = driver.find_element_by_id("text-input")
            if text_field.is_displayed():
              text_field.click()
            else:
              driver.execute_script("arguments[0].scrollIntoView();", text_field)
              if text_field.is_displayed():
                text_field.click()
              else:
                driver.execute_script("$(arguments[0]).focus()", "#text-input")
          except:
              driver.execute_script("$(arguments[0]).focus()", "#text-input")
          time.sleep(5)
            
          #点击发送按钮
          try:
            send_btn = driver.find_element_by_id("send_button")
            if send_btn.is_displayed():
              send_btn.click()
            else:
              driver.execute_script("arguments[0].scrollIntoView();", send_btn)
              if send_btn.is_displayed():
                send_btn.click()
              else:
                driver.execute_script("$(arguments[0]).click()", "#send_button")
                driver.execute_script("setTimeout($(arguments[0]).click,2000)", "#send_button")
          except:
            driver.execute_script("$(arguments[0]).click()", "#send_button")
            driver.execute_script("setTimeout($(arguments[0]).click,2000)", "#send_button")
          time.sleep(5)
             
        except:
          print (u'给%s发短信时发生异常：' % phone)
          info = sys.exc_info()
          #print(info)
          #print(info[0])
          print(info[1])
          time.sleep(2)
          pass
        continue
        
    print (u'处理完毕---end')
    
    driver.quit()
    
