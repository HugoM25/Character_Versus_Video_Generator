from moviepy.editor import *
import os
def main():
    current_path = os.getcwd()
    path_perso = "\Res\Persos\One_Piece\Zoro"
    start_time = 211
    end_time = 213
    clip = VideoFileClip(current_path + path_perso + "\\brut.mp4")
    clip = clip.subclip(start_time,end_time)
    clip.write_videofile(current_path + path_perso + "\\vid1.mp4", codec="libx264", remove_temp= True, fps=30)

def main2() :
    import cv2
    vidcap = cv2.VideoCapture("D:\Youtube\AnimeFights\zoroVSwarlords.mp4")
    success, image = vidcap.read()
    count = 0

    while success:
        cv2.imwrite("tmp/frame%d.jpg" % count, image)  # save frame as JPEG file
        success, image = vidcap.read()
        count += 1
if __name__ == "__main__" :
    main()
