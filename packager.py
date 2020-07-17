import os
import shutil
import pyautogui
from PIL import Image
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def packager(project):
    try:
        ###########################################################################
        ########################## Screenshotr ####################################
        # writeLog('Generating screenshots')

        chrome_options = Options()
        chrome_options.add_experimental_option("useAutomationExtension", False)
        chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
        chrome_options.add_argument("--start-fullscreen")
        chrome_options.add_argument("--auto-open-devtools-for-tabs")

        driver = webdriver.Chrome(executable_path='F:\\Installations\\driver\\chromedriver', options=chrome_options)
        driver.get('chrome://extensions')

        def capture():
            sleep(0.5)
            pyautogui.moveTo(1309, 11, 0.5)
            pyautogui.click()

            sleep(0.5)
            pyautogui.write('c', 0.25)
            pyautogui.press('enter')

            sleep(5)
            pyautogui.moveTo(1582, 874, 0.5)
            pyautogui.click()

        sleep(1)
        pyautogui.moveTo(1089, 13, 0.5)
        pyautogui.click()

        sleep(0.5)
        pyautogui.moveTo(1046, 250, 0.5)
        pyautogui.click()

        sleep(0.5)
        pyautogui.dragTo(1350, 250, 1)

        sleep(0.5)
        pyautogui.moveTo(633, 18, 0.5)
        pyautogui.click()

        sleep(0.5)
        pyautogui.write('1280', interval=0.25)

        sleep(0.5)
        pyautogui.press('tab')

        sleep(0.5)
        pyautogui.write('800', interval=0.25)

        for i in range(0, 4):
            print(i)
            sleep(0.25)
            pyautogui.hotkey('shift', 'tab')

        sleep(0.25)
        pyautogui.press('space')

        sleep(0.25)
        pyautogui.press('tab')

        sleep(0.25)
        pyautogui.press('space')

        sleep(0.25)
        pyautogui.hotkey('ctrl', 'v')

        sleep(0.25)
        pyautogui.press('tab')

        sleep(0.25)
        pyautogui.press('enter')

        sleep(0.5)
        driver.get('chrome://newtab')

        ###################################################
        ################### Screenshot 1 ##################
        sleep(1)
        pyautogui.moveTo(1118, 785, 0.5)
        pyautogui.click()

        capture()

        for i in range(0, 5):
            sleep(0.5)
            pyautogui.moveTo(1144, 315, 0.5)
            pyautogui.click()

            sleep(0.5)
            pyautogui.scroll(-490)

            if i == 2:
                pyautogui.scroll(-25)
            
            sleep(0.5)
            if i == 4:
                pyautogui.moveTo(1144, 725, 0.5)
            pyautogui.click()
            
            capture()

        sleep(1)
        driver.close()

        ########################################################################
        ################################# Copy screenshots ####################
        scrnshot_src = 'C:\\Users\\Sheha\\Downloads'
        scrnshot_dest = 'F:\\Private\\packed\\' + project + '\\'

        i = 0

        for filename in os.listdir(scrnshot_src):
            if 'chrome-extension' in filename:
                size = 1280, 800
                img = Image.open(scrnshot_src + '\\' + filename)
                img.thumbnail(size, Image.ANTIALIAS)
                img.save(scrnshot_dest + str(i) + '.png', 'PNG')
                i = i + 1
    
    except Exception as e:
        print(e)