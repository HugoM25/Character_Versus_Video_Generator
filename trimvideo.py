from moviepy.editor import *
import os
def main():
    current_path = os.getcwd()
    path_perso = "\Res\Persos\One_Piece\Flamingo"
    start_time =141
    end_time = 144
    clip = VideoFileClip(current_path + path_perso + "\\brut.mp4")
    clip = clip.subclip(start_time,end_time)
    clip.write_videofile(current_path + path_perso + "\\vid2.mp4", codec="libx264", remove_temp= True, fps=30)

if __name__ == "__main__" :
    main()
