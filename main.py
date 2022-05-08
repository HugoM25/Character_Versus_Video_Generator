import moviepy.editor as mpy
import numpy as np
import cv2
from PIL import Image, ImageFont, ImageDraw
from os.path import exists
#My libraries ---------------------------
from ScriptReader import *
from ImageManipulation import *
from AssetsLoader import *
from GeneratorFrames import *

def generate_edit_type1(script_infos, fps=30,folder_video_images="Temp", res_folder_path="Res", resolution_video=(1920,1080)) :
    count_img = 0
    #Read Script
    script_infos = ScriptReader('Res/script.txt')
    #Import song and timestamps
    part_of_video = load_timestamps(res_folder_path + "/" + script_infos.song)

    #Import images
    image_list1 = load_all_of_perso(res_folder_path + "/" + script_infos.perso1, ["vid1.mp4","vid2.mp4"] , 90)
    image_list2 = load_all_of_perso(res_folder_path + "/" + script_infos.perso2, ["vid1.mp4","vid2.mp4"] , 90)

    #Resize them
    new_height = int(resolution_video[0] / 2)
    for j in range(0,len(image_list1)) :
        image_list1[j] = resize_images(image_list1[j], new_height=new_height)
    for j in range(0,len(image_list2)) :
        image_list2[j] = resize_images(image_list2[j], new_height=new_height)
    #Create video frames
    count_img = create_video_frames_vid(part_of_video,count_img,image_list1,image_list2,script_infos,resolution_video,folder_video_images,fps)
    #Concatenate images into video (and add audio)
    write_video(folder_video_images, count_img,  res_folder_path + "/" + script_infos.song + "/soundtrack.wav")

def generate_edit_type2(script_infos,fps=30, folder_video_images="Temp", res_folder_path="Res", resolution_video=(1920,1080)) :
    count_img = 0

    #Import characters and their images
    image_gr1_list = []
    image_gr2_list = []
    new_height = int(resolution_video[0] / 2)
    for perso in script_infos.perso_gr1 :
        images_perso = load_all_of_perso(res_folder_path + "/" + perso, ["body.png","vid2.mp4"] , 90)
        # Resize them
        for j in range(0, len(images_perso)):
            images_perso[j] = resize_images(images_perso[j], new_height=new_height)
        for j in range(0, len(images_perso)):
            images_perso[j] = resize_images(images_perso[j], new_height=new_height)
        image_gr1_list.append(images_perso)

    for perso in script_infos.perso_gr2 :
        images_perso = load_all_of_perso(res_folder_path + "/" + perso, ["body.png","vid1.mp4"] , 90)
        # Resize them
        for j in range(0, len(images_perso)):
            images_perso[j] = resize_images(images_perso[j], new_height=new_height)
        for j in range(0, len(images_perso)):
            images_perso[j] = resize_images(images_perso[j], new_height=new_height)
        image_gr2_list.append(images_perso)

    background = load_background(res_folder_path+"/Backgrounds", script_infos.background)
    #Import song and timeStamps
    part_of_video = load_timestamps(res_folder_path + "/" + script_infos.song)

    #Resize background
    background = create_background(background, resolution_video)
    count_img = create_video_frames_type2(part_of_video,count_img,image_gr1_list,image_gr2_list, background, script_infos,resolution_video, folder_video_images, fps)
    write_video(folder_video_images, count_img, res_folder_path + "/" + script_infos.song + '/soundtrack.wav')

def main() :
    fps = 30
    folder_video_images = "Temp"
    res_folder_path = "Res"
    # Make sure resolution is in good order (rigth now it is not)
    resolution_video = (1920, 1080)

    script_infos = ScriptReader('Res/script2.txt')

    if script_infos.typeOfEdit == 1 :
        generate_edit_type1(script_infos,fps, folder_video_images, res_folder_path,resolution_video)
    elif script_infos.typeOfEdit == 2 :
        generate_edit_type2(script_infos, fps, folder_video_images, res_folder_path, resolution_video)

if __name__ == '__main__':
    main()
