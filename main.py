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

def create_video_frames(part_of_video, count_img, image1, image2, resolution_video =(1920,1080), folder_video_images = "Temp", fps=30) :
    for j in range(0, len(part_of_video)-1) :
        if j == 0 :
            for i in range(0, (part_of_video[1] - part_of_video[0]) * fps):
                combine_image(image1, image2, "BOA VS DON FLAMINGO", resolution_video).save(folder_video_images + "/frame" + str(count_img) + ".jpg")
                count_img+=1
        elif j % 2 == 1 :
            for i in range(0, (part_of_video[j+1] - part_of_video[j]) * fps):
                combine_image(image1, image2, "STRENGTH", resolution_video).save(folder_video_images + "/frame" + str(count_img) + ".jpg")
                count_img+=1
        else :
            for i in range(0, (part_of_video[j+1] - part_of_video[j]) * fps):
                full_screen_image(image1).save(folder_video_images + "/frame" + str(count_img) + ".jpg")
                count_img+=1
    return count_img

def WriteVideo(pathFolderImages, numberOfFrames, fps=30.0) :
    image_files = []
    for i in range(0, numberOfFrames) :
        image_files.append(pathFolderImages + "/frame" + str(i) +".jpg")
    clip = mpy.ImageSequenceClip(image_files, fps=fps)
    clip.write_videofile('project.mp4', codec="libx264", remove_temp= True, fps=fps)


def CompileSoundandAudio(pathFileVideo, pathFileAudio):
    finalVid = mpy.VideoFileClip(pathFileVideo)
    finalAudio = mpy.AudioFileClip(pathFileAudio)

    new_audioClip = mpy.CompositeAudioClip([finalAudio])

    finalVid = finalVid.set_audio(new_audioClip)
    finalVid.write_videofile("finalVideo.mp4", codec='libx264', audio_codec="aac")


def main() :

    part_of_video = [0,3,4,5,6,7,8,9]
    fps = 30
    folder_video_images = "Temp"
    count_img = 0
    resolution_video = (1920,1080)
    #Import images
    image2 = Image.open("boa.jpg")
    image1 = Image.open("flamingo.jpg")
    #Resize them
    new_height = int(resolution_video[0]/2)
    image1 = image1.resize((int(new_height * image1.size[0] / image1.size[1]) , new_height) )
    image2 = image2.resize((int(new_height * image2.size[0] / image2.size[1]), new_height))
    #Create video frames
    count_img = create_video_frames(part_of_video,count_img,image1,image2,resolution_video,folder_video_images,fps)
    #Concatenate images into video
    WriteVideo(folder_video_images, count_img)
    #Add music to the video
    CompileSoundandAudio("project.mp4", "soundtrack.wav")

if __name__ == '__main__':
    main()
