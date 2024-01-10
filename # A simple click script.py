# 点点点
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def expand_shadow_element(element):
  shadow_root = driver.execute_script('return arguments[0].shadowRoot', element)
  #driver.implicitly_wait(10)
  driver.implicitly_wait(0.5)
  return shadow_root

options = webdriver.EdgeOptions() #selenium4已支持edge
options.use_chromium = True
options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
driver = webdriver.Edge(options = options)

print(driver)
# 找到包含第一个 Shadow DOM 的元素
shadow_host_1 = driver.find_element(By.TAG_NAME,'macroponent-f51912f4c700201072b211d4d8c26010')
print(shadow_host_1)

# 执行 JavaScript 以访问第一个 Shadow DOM
shadow_root_1 = expand_shadow_element(shadow_host_1)
print(shadow_root_1)

shadow_host_2 = shadow_root_1.find_element(By.CSS_SELECTOR,'div > sn-canvas-appshell-root')
print(shadow_host_2)

# 在 Shadow DOM 中找到 iframe 元素
iframe_element = shadow_host_2.find_element(By.ID,'gsft_main')
print(iframe_element)

# 切换到 iframe
driver.switch_to.frame(iframe_element)

# 找到iframe内的#document
iframe_document = driver.find_element(By.CSS_SELECTOR, 'html')
print(iframe_document)

totalrows = iframe_document.find_element(By.XPATH,'//div[5]//td[2]//span[1]//div/span[2]/span[2]').text
print(f'共有{totalrows}条记录')

countrange = int(totalrows.replace(",", ""))/50
countrange = math.ceil(countrange)
print(f'需要跑{countrange}次')

for i in range(countrange):
    print(f'第{i+1}次')

    # 打勾
    driver.find_element(By.XPATH,'//*[@id="hdr_alm_hardware"]/th[1]/span/label').click()
    target = driver.find_element(By.XPATH,'//*[@id="hdr_alm_hardware"]/th[1]/span/label')       
    driver.execute_script("arguments[0].scrollIntoView();", target) 
    time.sleep(1)

    # 点绿勾
    driver.find_element(By.XPATH,'//*[@id="certify_checked_elements"]').click()
    target = driver.find_element(By.XPATH,'//*[@id="certify_checked_elements"]')       
    driver.execute_script("arguments[0].scrollIntoView();", target) 
    time.sleep(15)

    # 点下一页
    try:
      driver.find_element(By.XPATH,'//div[5]//div[6]//table//td[2]//span[1]//button[3]').click()
      target = driver.find_element(By.XPATH,'//div[5]//div[6]//table//td[2]//span[1]//button[3]')       
      driver.execute_script("arguments[0].scrollIntoView();", target) 
      time.sleep(2)
    except:
      print("跑完了")

# driver.switch_to.default_content()