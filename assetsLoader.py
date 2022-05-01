import cv2
from PIL import Image
from os.path import exists

def load_image_perso(path_perso) :
    img_perso  = Image.open(path_perso + "/pic1.jpg")
    return img_perso

def load_video_perso(path_perso, vid_name, lenmax=-1) :
    img_list_perso = []
    cap = cv2.VideoCapture(path_perso + vid_name)
    count = 0
    if lenmax == -1 :
        while True:
            ret, frame = cap.read()
            if not ret:
                break
            pil_img = Image.fromarray(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
            img_list_perso.append(pil_img)
    else :
        while count < lenmax:
            ret, frame = cap.read()
            if not ret:
                break
            pil_img = Image.fromarray(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
            img_list_perso.append(pil_img)
            count+=1
    return img_list_perso

def load_all_perso(path_perso, lenmax=-1) :
    final_list_img = []
    vid1_name ="/vid1.mp4"
    vid2_name ="/vid2.mp4"
    if exists(path_perso+vid1_name) :
        final_list_img.append(load_video_perso(path_perso,vid1_name,lenmax))
    if exists(path_perso+vid2_name) :
        final_list_img.append(load_video_perso(path_perso, vid2_name,lenmax))

    return final_list_img

def load_timestamps(path_song) :
    with open(path_song + "/timestamps.txt") as f :
        lines = f.readlines()
    #Clean list
    timestamps_list = lines[0].replace("\n", "").split(",")
    timestamps_list = [ float(x) for x in timestamps_list]
    return timestamps_list