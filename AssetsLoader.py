import cv2
from PIL import Image
from os.path import exists

def load_image_perso(path_perso, filename) :
    img_perso  = Image.open(path_perso + "/"+filename)
    return img_perso

def load_background(filename) :
    img_back = Image.open(filename)
    return img_back

def load_video_perso(path_perso, vid_name, lenmax=-1) :
    img_list_perso = []
    cap = cv2.VideoCapture(path_perso +"/" +vid_name)
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

def load_all_of_perso(path_perso, files_to_load, lenmax=-1) :
    final_list_img = []
    imageExtension = ["png", "jpg", "jpeg"]
    videoExtension = ["mp4"]

    for file_to_load in files_to_load :
        tmp_list = []
        if exists(path_perso+"/"+file_to_load) :
            extension_of_file = file_to_load.split(".")[1]
            if extension_of_file in videoExtension:
                tmp_list = load_video_perso(path_perso,file_to_load,lenmax)
            elif extension_of_file in imageExtension :
                tmp_list.append(load_image_perso(path_perso,file_to_load))
        final_list_img.append(tmp_list)
    return final_list_img

def load_timestamps(path_song) :
    with open(path_song + "/timestamps.txt") as f :
        lines = f.readlines()
    #Clean list
    timestamps_list = lines[0].replace("\n", "").split(",")
    timestamps_list = [ float(x) for x in timestamps_list]
    return timestamps_list