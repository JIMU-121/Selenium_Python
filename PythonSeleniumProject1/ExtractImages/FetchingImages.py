import os

FOLDER_PATH = r'C:\\Users\\bhatt\\Downloads\\Telegram Desktop\\folder 8\\slide'


def ProductImages(dir):
    imagepaths = []
    fileNames = os.listdir(dir)
    for file in fileNames:
        # print('File Name: ' + fileName)
        # print('Folder Path: ' + os.path.abspath(os.path.join(dir, fileName)).replace('\\', '\\\\'))

        imagepaths.append(os.path.abspath(os.path.join(dir, file)).replace('\\', '\\\\'))


    return imagepaths


def SlideImages(dir):
    SlideIMGs = []
    fileName = os.listdir(dir)
    for file in fileName:
        SlideIMGs.append(os.path.abspath(os.path.join(dir, file)).replace('\\', '\\\\'))

    return SlideIMGs

if __name__ == '__main__':
    ab = SlideImages(FOLDER_PATH)
    print(ab)







