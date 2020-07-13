import pyperclip
from time import sleep
from pyautogui import click, scroll, moveTo, position, hotkey, press, write

def uploader(project_name):
    chromeStoreDashboard = 'https://chrome.google.com/webstore/devconsole/6ef36149-0c2d-4623-9d07-32f2b8d1c33b'
    packed_src = 'F:\\Private\\packed\\' + project_name

    description = '''{project} New Tab & Wallpapers Collection
Created by Solodev

########################################################################

{project} New Tab Extension brings a new look to your Chrome browser.
Install {project} New Tab and enjoy handpicked HD images of {project} wallpapers.

# Perks of {project} New Tab Extension (created by Solodev)

✓ High quality wallpapers with every new tab
✓ Current Date/Time
✓ Shortcut links to social networks and shopping websites
✓ Multiple search engines to help you search through different websites:
    -  Google
    -  YouTube
    -  Amazon
    -  G2A (to search games)
    -  Kinguin (Best game deals)

####################################################################################

You can also support us at: https://www.buymeacoffee.com/RONpy5oXJ

We are going to add more feature for you to have better experience on your browser. It's a promise.

If you liked the {project} New Tab Wallpapers extension we suggest you to take a look our other extensions.'''.format(project=project_name)

    mini_description = '''{project} New Tab Extension brings a new look to your Chrome browser.
Install {project} New Tab and enjoy handpicked HD images of {project} wallpapers.'''.format(project = project_name)

    storage = 'The storage permission is required to persist changes in the extension.'

    ####################################################################################
    ####################### Launching chrome ###########################################
    sleep(0.5)
    press('win')

    sleep(0.5)
    write('chrome', interval=0.15)

    sleep(0.5)
    press('enter')

    ####################################################################################
    ####################### Opening chrome web store dashboard #########################
    pyperclip.copy(chromeStoreDashboard)

    sleep(1.5)
    hotkey('ctrl', 'v')

    sleep(0.5)
    press('enter')

    ####################################################################################
    ####################### Clicking on add new item ###################################
    sleep(5)
    for i in range(0, 8):
        if i == 7:
            sleep(0.5)
            press('space')
            sleep(1)
        
        sleep(0.1)
        press('tab')

        if i == 7:
            sleep(0.1)
            press('space')

    ####################################################################################
    ####################### Uploading zip file #########################################
    sleep(0.5)
    pyperclip.copy(packed_src + '\\' + project_name + '.zip')

    sleep(0.5)
    hotkey('ctrl', 'v')

    sleep(0.5)
    press('enter')
                                        
    sleep(60)

    ####################################################################################
    ####################### Opening privacy section ####################################
    sleep(1)
    moveTo(753, 177, duration=0.5)
    click()

    for i in range(0, 6):
        sleep(0.1)
        press('tab')

    sleep(0.5)
    press('enter')

    ####################################################################################
    ####################### Pasting the mini-description and storage ###################
    sleep(1)
    for i in range(0, 15):
        if i == 10:
            sleep(0.5)
            pyperclip.copy(mini_description)

            sleep(1)
            hotkey('ctrl', 'v')

        if i == 13:
            sleep(0.5)
            pyperclip.copy(storage)
            
            sleep(1)
            hotkey('ctrl', 'v')

        if i == 14:
            sleep(0.5)
            press('right')

        sleep(0.1)
        press('tab')

    ####################################################################################
    ####################### Saving privacy section changes #############################
    sleep(1)
    moveTo(753, 177, duration=0.5)
    click()

    sleep(0.1)
    press('tab')

    sleep(0.1)
    press('tab')

    sleep(0.1)
    press('space')

    ####################################################################################
    ####################### Moving to listing section ##################################
    sleep(5)
    click()
    
    for i in range(0, 5):
        i
        sleep(0.1)
        press('tab')

    sleep(0.1)
    press('enter')

    ####################################################################################
    ####################### Selecting the category #####################################
    sleep(2)
    moveTo(621, 649, duration=0.5)
    click()

    sleep(0.5)
    moveTo(577, 444, duration=0.5)
    click()

    sleep(0.5)
    moveTo(575, 737, duration=0.5)
    click()

    ####################################################################################
    ####################### Selecting the language #####################################
    sleep(0.5)
    moveTo(577, 444, duration=0.5)
    scroll(-500)
    sleep(1)
    click()

    ####################################################################################
    ####################### Uploading first image #####################################
    sleep(0.5)
    scroll(-800)

    sleep(0.5)
    click()

    sleep(1)
    press('0')

    sleep(0.5)
    press('enter')

    ####################################################################################
    ####################### Uploading second image #####################################
    sleep(20)
    moveTo(720, 444, duration=0.25)
    click()

    sleep(1)
    press('1')
    
    sleep(0.5)
    press('enter')

    ####################################################################################
    ####################### Uploading third image ######################################
    sleep(20)
    moveTo(900, 444, duration=0.25)
    click()

    sleep(1)
    press('2')

    sleep(0.5)
    press('enter')

    ####################################################################################
    ####################### Uploading fourth image #####################################
    sleep(20)
    moveTo(1050, 444, duration=0.25)
    click()

    sleep(1)
    press('3')

    sleep(0.5)
    press('enter')

    ####################################################################################
    ####################### Uploading fifth image #####################################
    sleep(20)
    moveTo(1200, 444, duration=0.25)
    click()

    sleep(1)
    press('4')

    sleep(0.5)
    press('enter')

    ####################################################################################
    ####################### Entering description #######################################
    sleep(20)
    scroll(1000)

    sleep(1)
    moveTo(753, 177, duration=0.5)
    click()

    pyperclip.copy(description)

    sleep(0.5)
    moveTo(618, 525, duration=0.25)
    click()

    sleep(1)
    hotkey('ctrl', 'v')

    ####################################################################################
    ################################# Saving changes ###################################
    sleep(1)
    moveTo(753, 177, duration=0.5)
    click()

    sleep(0.5)
    press('tab')
    
    sleep(0.5)
    press('tab')

    sleep(0.5)
    press('space')

    ####################################################################################
    ################################# Submitting extension #############################
    sleep(4)
    click()

    sleep(0.5)
    press('tab')

    sleep(0.5)
    press('space')

    sleep(1)
    for i in range(0, 3):
        sleep(0.1)
        press('tab')

    sleep(0.5)
    press('space')

    sleep(10)
    hotkey('alt', 'f4')

uploader('Abstract')