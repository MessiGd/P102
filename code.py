import dropbox
import cv2
import time
import random

start_time = time.time()

def photo():
    number = random.randint(1,100)
    videoCaptureObject = cv2.VideoCapture(0)
    result = True
    while(result):
        ret,frame = videoCaptureObject.read()
        img_name = "img"+str(number) + ".png"
        cv2.imwrite(img_name, frame)
        start_time = time.time
        result = False

    return img_name  

def uploading(img_name):
    access_token="rQ4A2gU9GUgAAAAAAAAAAac4IUbxcR5YW5U79-0MEbf1fmYn3YrlcBLSQecow6jk"
    file = img_name
    file_from = file
    file_to = "/python/"+ (img_name)
    dbx = dropbox.Dropbox(access_token) 
    with open(file_from, 'rb' ) as f:
        dbx.file_upload(f.read() , file_to, mode = dropbox.files.WriteMode.overwrite)
        print("File Uploaded")

def a():
    while(True):
        if((time.time()-start_time ) >= 5 ):
            name = photo()
            uploading(name)
            
a()        