import os, shutil

backup_dir = 'F:\\Private\\backup\\'

def backup(project, icons_src, images_src):
    try:
        project = backup_dir + project
        os.mkdir(project)

        icons_dest = project + '\\icons'
        os.mkdir(icons_dest)

        for icon in os.listdir(icons_src):
            shutil.copy(icons_src + icon, icons_dest + '\\' + icon)

        images_dest = project + '\\images'
        os.mkdir(images_dest)

        for image in os.listdir(images_src):
            shutil.copy(images_src + image, images_dest + '\\' + image)

    except Exception as e:
        print(e)