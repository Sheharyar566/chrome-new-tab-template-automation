from PIL import Image
import os, shutil

iconName = input('Input the original icon file name: ')
projectName = input('Input the project name: ')

srcFile = 'C:\\Users\\Sheha\\Downloads\\' + iconName
destFile = 'F:\\Work\\' + projectName + '\\public\\assets\\icons\\'

if os.path.isfile(srcFile):
    for i in range(1, 20):
        multiple = i * 8

        if(multiple == 16 or multiple == 24 or multiple == 32 or multiple == 48 or multiple == 64 or multiple == 128):
            img = Image.open(srcFile)
            
            size = multiple, multiple
            img.thumbnail(size, Image.ANTIALIAS)
            img.save(destFile + 'icon-' + str(multiple) + '.png', optimize=True)

            img.close()

    print('Done!')
else:
    print('Image file not found')