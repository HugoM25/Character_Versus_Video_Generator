import moviepy.editor as mpy
import numpy as np
import cv2
from PIL import Image, ImageFont, ImageDraw

def combine_image(image_up, image_down, text_to_write, resolution_video = (1920,1080)) :
    #Create background
    final_image = Image.new('RGB', (resolution_video[1],resolution_video[0]))
    #Add images
    final_image.paste(image_up, (int((resolution_video[1]-image_up.size[0])/2),0))
    final_image.paste(image_down, (int((resolution_video[1]-image_down.size[0])/2), int(resolution_video[0]/2)))
    #Add text
    final_image_edit = ImageDraw.Draw(final_image)
    font_text = ImageFont.truetype("impact.ttf", 80)
    w, h = final_image_edit.textsize(text_to_write, font=font_text)
    final_image_edit.text((int((resolution_video[1]-w)/2),int((resolution_video[0]-h)/2)) , text_to_write,font=font_text, stroke_width=5, stroke_fill=(0,0,0))

    return final_image

def full_screen_image(image, resolution_video=(1920,1080)) :
    final_image = Image.new('RGB', (resolution_video[1], resolution_video[0]))
    new_height = resolution_video[0]
    image = image.resize((int(new_height * image.size[0] / image.size[1]), new_height))

    final_image.paste(image, (int((resolution_video[1]-image.size[0])/2),0))
    return final_image

def read_script_file(script_path) :
    script_infos = {}
    with open(script_path) as f :
        lines = f.readlines()
    #Clean list
    lines = [x.replace("\n", "") for x in lines]

    #Add list to info dict
    script_infos["Perso1"] = lines[0].split(" ")[0]
    script_infos["Perso2"] = lines[0].split(" ")[2]

    script_infos["Song"] = lines[1]

    script_infos["Comparison"] = []
    for i in range(2, len(lines)) :
        script_infos["Comparison"].append(lines[i].split(" "))

    return script_infos

def create_video_frames_img(part_of_video, count_img, image1, image2, script_infos,resolution_video =(1920,1080), folder_video_images = "Temp", fps=30) :
    j = 0
    k = 0
    while j < len(part_of_video)-1 and k < len(script_infos["Comparison"]) :
        if j == 0 :
            img = combine_image(image1, image2, script_infos["Perso1"].split("/")[-1] + " VS " + script_infos["Perso2"].split("/")[-1], resolution_video)
            for i in range(0, (part_of_video[1] - part_of_video[0]) * fps):
                img.save(folder_video_images + "/frame" + str(count_img) + ".jpg")
                count_img+=1
        elif j % 2 == 1 :
            img = combine_image(image1, image2, script_infos["Comparison"][k][0], resolution_video)
            for i in range(0, (part_of_video[j+1] - part_of_video[j]) * fps):
                img.save(folder_video_images + "/frame" + str(count_img) + ".jpg")
                count_img+=1
        else :
            if (int(script_infos["Comparison"][k][1]) == 1) :
                img = full_screen_image(image1)
            else :
                img = full_screen_image(image2)

            for i in range(0, (part_of_video[j+1] - part_of_video[j]) * fps):
                img.save(folder_video_images + "/frame" + str(count_img) + ".jpg")
                count_img+=1
            k+=1
        j+=1
    return count_img

def create_video_frames_vid(part_of_video, count_img, image_list1, image_list2, script_infos, resolution_video =(1920,1080), folder_video_images = "Temp", fps=30) :
    j = 0
    k = 0
    while j < len(part_of_video)-1 and k < len(script_infos["Comparison"]) :
        index_list1 = 0
        index_list2 = 0
        if j == 0 :
            for i in range(0, (int(part_of_video[1] - part_of_video[0]) * fps)):
                img = combine_image(image_list1[index_list1], image_list2[index_list2], script_infos["Perso1"].split("/")[-1] + " VS " + script_infos["Perso2"].split("/")[-1], resolution_video)
                img.save(folder_video_images + "/frame" + str(count_img) + ".jpg")
                count_img+=1

                index_list1 += 1
                index_list2 += 1
                if index_list2 >= len(image_list2) :
                    index_list2 = 0
                if index_list1 >= len(image_list1) :
                    index_list1 = 0

        elif j % 2 == 1 :
            for i in range(0, int((part_of_video[j+1] - part_of_video[j]) * fps)):
                img = combine_image(image_list1[index_list1], image_list2[index_list2],script_infos["Comparison"][k][0], resolution_video)
                img.save(folder_video_images + "/frame" + str(count_img) + ".jpg")
                count_img+=1

                index_list1 += 1
                index_list2 += 1
                if index_list2 >= len(image_list2) :
                    index_list2 = 0
                if index_list1 >= len(image_list1) :
                    index_list1 = 0
        else :
            for i in range(0, int((part_of_video[j+1] - part_of_video[j]) * fps)):

                if (int(script_infos["Comparison"][k][1]) == 1):
                    img = full_screen_image(image_list1[index_list1])
                else:
                    img = full_screen_image(image_list2[index_list2])

                img.save(folder_video_images + "/frame" + str(count_img) + ".jpg")

                count_img+=1

                index_list1 += 1
                index_list2 += 1
                if index_list2 >= len(image_list2) :
                    index_list2 = 0
                if index_list1 >= len(image_list1) :
                    index_list1 = 0
            k+=1
        j+=1
    return count_img

def write_video(pathFolderImages, numberOfFrames, audio_path, fps=30.0) :
    image_files = []
    for i in range(0, numberOfFrames) :
        image_files.append(pathFolderImages + "/frame" + str(i) +".jpg")
    clip = mpy.ImageSequenceClip(image_files, fps=fps)
    audio_clip = mpy.AudioFileClip(audio_path).set_duration(clip.duration)
    new_audio_clip = mpy.CompositeAudioClip([audio_clip])
    clip = clip.set_audio(new_audio_clip)
    clip.write_videofile('project.mp4', codec="libx264", remove_temp= True, fps=fps)


def compile_sound_video(path_file_video, path_file_audio):
    final_vid = mpy.VideoFileClip(path_file_video)
    final_audio = mpy.AudioFileClip(path_file_audio)

    new_audioClip = mpy.CompositeAudioClip([final_audio])

    final_vid = final_vid.set_audio(new_audioClip)
    final_vid.write_videofile("finalVideo.mp4", codec='libx264', audio_codec="aac")

def load_image_perso(path_perso) :
    img_perso  = Image.open(path_perso + "/pic1.jpg")
    return img_perso

def load_video_perso(path_perso, lenmax=-1) :
    img_list_perso = []
    cap = cv2.VideoCapture(path_perso + "/vid1.mp4")
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

def load_timestamps(path_song) :
    with open(path_song + "/timestamps.txt") as f :
        lines = f.readlines()
    #Clean list
    timestamps_list = lines[0].replace("\n", "").split(",")
    timestamps_list = [ float(x) for x in timestamps_list]
    return timestamps_list

def main() :


    fps = 30
    folder_video_images = "Temp"
    res_folder_path = "Res"
    count_img = 0
    resolution_video = (1920,1080)
    #Read Script
    script_infos = read_script_file('Res/script.txt')
    #Import song and timestamps
    part_of_video = load_timestamps(res_folder_path + "/" + script_infos["Song"])
    #Import images
    image_list1 = load_video_perso(res_folder_path + "/" + script_infos["Perso1"], 90)
    image_list2 = load_video_perso(res_folder_path + "/" + script_infos["Perso2"], 90)
    #Resize them
    new_height = int(resolution_video[0] / 2)
    for i in range(0, len(image_list1)) :
        image_list1[i] = image_list1[i].resize((int(new_height * image_list1[i].size[0] / image_list1[i].size[1]) , new_height) )
    for j in range(0, len(image_list2)) :
        image_list2[j] = image_list2[j].resize((int(new_height * image_list2[j].size[0] / image_list2[j].size[1]), new_height))
    #Create video frames
    count_img = create_video_frames_vid(part_of_video,count_img,image_list1,image_list2,script_infos,resolution_video,folder_video_images,fps)
    #Concatenate images into video
    write_video(folder_video_images, count_img,  res_folder_path + "/" + script_infos["Song"] + "/soundtrack.wav")
    #Add music to the video
    #compile_sound_video("project.mp4", res_folder_path + "/" + script_infos["Song"] + "/soundtrack.wav")

if __name__ == '__main__':
    main()
