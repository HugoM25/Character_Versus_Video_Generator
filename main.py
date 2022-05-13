import argparse
#My libraries ---------------------------
from ScriptReader import *
from AssetsLoader import *
from GeneratorFrames import *

def generate_edit(script_infos,  fps=30,folder_video_images="Temp", res_folder_path="Res", resolution_video=(1920,1080)) :
    count_img = 0
    # Import characters and their images
    characters_img = []
    new_height = int(resolution_video[0] / 2)
    for perso in script_infos.persos:
        images_perso = load_all_of_perso(res_folder_path + "/" + perso[0], perso[1], 90)
        # Resize them
        for j in range(0, len(images_perso)):
            images_perso[j] = resize_images(images_perso[j], new_height=new_height)
        characters_img.append(images_perso)
    #Import Background

    background = load_background(res_folder_path +"/" + script_infos.background)
    background = create_background(background, resolution_video)
    # Import song and timeStamps
    part_of_video = load_timestamps(res_folder_path + "/" + script_infos.song)
    #Write frames according to the style of the edit
    if script_infos.type_of_edit == 1 :
        count_img = create_video_frames_edit1(part_of_video, count_img, characters_img, background,
                                    script_infos, resolution_video, folder_video_images, fps)
    elif script_infos.type_of_edit == 2 :
        count_img = create_video_frames_edit2(part_of_video, count_img, characters_img, background,
                                              script_infos, resolution_video, folder_video_images, fps)
    #Finally write the video
    write_video(folder_video_images, count_img, res_folder_path + "/" + script_infos.song + '/soundtrack.wav')


def main() :
    # Make sure resolution is in good order (rigth now it is not)
    resolution_video = (1920, 1080)

    # Parse the arguments-------------------------------------
    parser = argparse.ArgumentParser(description='Informations')
    parser.add_argument('--fps', type=int, help="FPS of the video", default=30)
    parser.add_argument('--supptemp', type=bool, help="Option to delete the temp data stored to create the final video",
                        default=True)
    parser.add_argument('--tempFolder', type=str, help="Path to the folder used to store temporary files",
                        default="Temp")
    parser.add_argument("--resFolder", type=str, help="Path to the folder with the video and images resources",
                        default="Res")
    parser.add_argument("--scriptPath", type=str, help="Path to the script to read",
                        default="Res/script.txt" )
    args = parser.parse_args()
    res_folder_path = args.resFolder
    folder_video_images = args.tempFolder
    fps = args.fps
    script_path = args.scriptPath
    suppTemp = args.supptemp


    script_infos = ScriptReader(script_path)
    print("Script ok")
    print(script_infos.persos)

    generate_edit(script_infos, fps, folder_video_images, res_folder_path, resolution_video)
if __name__ == '__main__':
    main()
