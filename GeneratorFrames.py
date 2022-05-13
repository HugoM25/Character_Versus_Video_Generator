import moviepy.editor as mpy

from ImageManipulation import *

def create_video_frames_edit1(part_of_video, count_img, characters_img, background, script_infos, resolution_video = (1920,1080)
                        , folder_video_images = "Temp", fps = 30):
    j = 0
    k = 0
    defiler = FrameDefiler("backward", 0, 0)
    index_list1, index_list2 = defiler.reset()
    while j < len(part_of_video) - 1 and k < len(script_infos.comparisons):
        if j == 0:
            perso_up = characters_img[0]
            perso_down = characters_img[1]
            defiler.change_max(len(perso_up[1]), len(perso_down[1]))
            index_list1, index_list2 = defiler.reset()
            text_to_write = script_infos.title[0] + "\n" + script_infos.title[1] + "\n" + script_infos.title[2]
            t_start = count_img
            nb_frames = (int(part_of_video[1] - part_of_video[0]) * fps)
            for i in range(0, nb_frames):
                img = combine_image(perso_up[1][index_list1], perso_down[1][index_list2], resolution_video)
                img = add_text_to_image(img, text_to_write, count_img - t_start, resolution_video, start_size=100, change_size=False, align="center")
                img.save(folder_video_images + "/frame" + str(count_img) + ".jpg")
                count_img += 1
                index_list1, index_list2 = defiler.defile(index_list1, index_list2, 1, 1)
        # Comparison part
        elif j % 2 == 1:
            # Set up the defiler object
            perso_up = characters_img[0]
            perso_down = characters_img[1]

            defiler.change_max(len(perso_up[1]), len(perso_down[1]))
            index_list1, index_list2 = defiler.reset()

            text_to_write = script_infos.comparisons[k][0]
            t_start = count_img
            for i in range(0, int((part_of_video[j+1] - part_of_video[j]) * fps)):
                img = combine_image(perso_up[1][index_list1], perso_down[1][index_list2], resolution_video)
                img = add_text_to_image(img, text_to_write, count_img - t_start, resolution_video, change_size=False, start_size=100)

                img.save(folder_video_images + "/frame" + str(count_img) + ".jpg")
                count_img+=1
                index_list1, index_list2 = defiler.defile(index_list1, index_list2, 1, 1)
        # Show winnerPart
        else:
            # Set up the defiler object
            perso_winner = characters_img[int(script_infos.comparisons[k][1])]

            defiler.change_max(len(perso_winner[2]), 0)
            index_list1, index_list2 = defiler.reset()
            nb_frames = int((part_of_video[j + 1] - part_of_video[j]) * fps)
            for i in range(0, nb_frames):
                img = full_screen_image(perso_winner[2][index_list1])
                index_list1, index_list2 = defiler.defile(index_list1, index_list2, 1, 0)
                img.save(folder_video_images + "/frame" + str(count_img) + ".jpg")
                count_img += 1
            k += 1
        j += 1

    return count_img

def create_video_frames_edit2(part_of_video, count_img, characters_img, background, script_infos, resolution_video = (1920,1080)
                        , folder_video_images = "Temp", fps = 30):
    j = 0
    k = 0
    defiler = FrameDefiler("backward", 0, 0)
    index_list1, index_list2 = defiler.reset()
    while j < len(part_of_video) - 1 and k < len(script_infos.comparisons):
        if j == 0:
            perso_up = characters_img[int(script_infos.comparisons[0][0])]
            perso_down = characters_img[int(script_infos.comparisons[0][1])]
            defiler.change_max(len(perso_up[1]), len(perso_down[1]))
            index_list1, index_list2 = defiler.reset()
            text_to_write = script_infos.title[0] + "\n" + script_infos.title[1] + "\n" + script_infos.title[2]
            t_start = count_img
            nb_frames = (int(part_of_video[1] - part_of_video[0]) * fps)
            for i in range(0, nb_frames):
                img = combine_image(perso_up[1][index_list1], perso_down[1][index_list2], resolution_video)
                img = add_text_to_image(img, text_to_write, count_img - t_start, resolution_video, start_size=100, change_size=False, align="center")
                img.save(folder_video_images + "/frame" + str(count_img) + ".jpg")
                count_img += 1
                index_list1, index_list2 = defiler.defile(index_list1, index_list2, 1, 1)
        # Comparison part
        elif j % 2 == 1:
            perso_left = characters_img[int(script_infos.comparisons[k][0])]
            perso_right = characters_img[int(script_infos.comparisons[k][1])]
            nb_frames = int((part_of_video[j + 1] - part_of_video[j]) * fps)
            for i in range(0, nb_frames):
                t = i / nb_frames
                img = body_comp_images(perso_left[0][0], perso_right[0][0], t, background,resolution_video)
                img.save(folder_video_images + "/frame" + str(count_img) + ".jpg")
                count_img += 1
        # Show winnerPart
        else:
            # Set up the defiler object
            perso_winner = characters_img[int(script_infos.comparisons[k][2])]

            defiler.change_max(len(perso_winner[2]), 0)
            index_list1, index_list2 = defiler.reset()
            nb_frames = int((part_of_video[j + 1] - part_of_video[j]) * fps)
            for i in range(0, nb_frames):
                img = full_screen_image(perso_winner[2][index_list1])
                index_list1, index_list2 = defiler.defile(index_list1, index_list2, 1, 0)
                img.save(folder_video_images + "/frame" + str(count_img) + ".jpg")
                count_img += 1
            k += 1
        j += 1

    return count_img

class FrameDefiler() :
    def __init__(self, mode, max_list1, max_list2):
        self.mode = mode
        self.sens1 = 1
        self.sens2 = 1
        self.max_list1 = max_list1
        self.max_list2 = max_list2

    def reset(self):
        self.sens1 = 1
        self.sens2 = 1
        return 0,0
    def change_max(self, max_list1, max_list2):
        self.max_list1 = max_list1
        self.max_list2 = max_list2

    def defile(self, index_list1, index_list2, supp1, supp2):
        new_ind1 = index_list1 + supp1 * self.sens1
        new_ind2 = index_list2 + supp2 * self.sens2
        if self.mode == "restart":
            if new_ind1 >= self.max_list1:
                new_ind1 = 0
            if new_ind2 >= self.max_list2:
                new_ind2 = 0
        elif self.mode == "backward" :
            if new_ind1 >= self.max_list1 or new_ind1 < 0 :
                self.sens1 *= -1
                new_ind1 += supp1*self.sens1
            if new_ind2 >= self.max_list2 or new_ind2 < 0 :
                self.sens2 *= -1
                new_ind2 += supp2*self.sens2

        return new_ind1, new_ind2


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

