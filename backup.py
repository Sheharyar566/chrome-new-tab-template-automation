import os, shutil
from functions import writeLog
from functions import exceptionLogger

backup_dir = 'F:\\Private\\backup\\'

def backup(project, icons_src, images_src):
    try:
        ####################################################################
        writeLog('Creating the backup folder')

        project = backup_dir + project
        os.mkdir(project)

        writeLog('Backup folder created successfully')

        #####################################################################
        writeLog('Copying icons from project\'s icon folder to backup folder')

        icons_dest = project + '\\icons'
        os.mkdir(icons_dest)

        for icon in os.listdir(icons_src):
            shutil.copy(icons_src + icon, icons_dest + '\\' + icon)

        writeLog('Icons copied successfully!')

        #####################################################################
        writeLog('Copying images from project\'s images folder to backup folder')

        images_dest = project + '\\images'
        os.mkdir(images_dest)

        for image in os.listdir(images_src):
            shutil.copy(images_src + image, images_dest + '\\' + image)

        writeLog('Images copied successfully!')

    except Exception as e:
        writeLog('\n#######################################################')
        writeLog('Error occured')
        writeLog(e)
        print('Error occured')