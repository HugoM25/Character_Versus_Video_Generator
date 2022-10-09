# Anime_Versus_VideoGenerator
Video generator of anime characters comparisons

# What is it ?
This program is a command line tool to generate videos of anime characters comparisons in the same style as : [this video](https://www.youtube.com/shorts/wQrzgNojzug)
or the style of [this video](https://www.youtube.com/shorts/GL-gNR3gBA0)

# Example

More videos can be found on this channel : https://www.tiktok.com/@animeversus2022

<p align="center">
 <img src="https://github.com/HugoM25/Anime_Versus_Video_Generator/blob/master/vid1.gif" alt="animated" />
  <img src="https://github.com/HugoM25/Anime_Versus_Video_Generator/blob/master/vid2.gif" alt="animated" />
</p>

# How to use it ?

<h2> Usage </h2>
To use this program you can use a command like this :

```Shell
python main.py --scriptPath pathToYourTxtFile --resFolder PathToResFolder
```

The available arguments are: 

- `--fps` : The fps of video
- `--supptemp` : Contains the decision to delete/backup the temporary files used for the video (by default True)
- `--tempFolder` : Path to the folder used to store temporary files
- `--resFolder` : Path to the folder with the video and images resources
- `--scriptPath` : Path to the script to read

<h2> Setup </h2>

<h3> How to organize the database of resources ? </h3>

Here is the way I used to organize my database of characters/songs/backgrounds/scripts (not mandatory) :


:file_folder: Res

------->:file_folder: Backgrounds

---------------->:camera:backgrounds_pic.jpg

------->:file_folder: Musique

---------------->:file_folder: Song1

------------------------>:cd: soundtrack.wav

------------------------>:page_with_curl: timestamps.txt

------->:file_folder: Persos

--------------->:file_folder: Character1

------------------------>:camera: body.png

------------------------>:video_camera: vid1.mp4

------------------------>:video_camera: vid2.mp4

------->:file_folder: Scripts

-------------->:page_with_curl: script.txt


<h3> How to write a .txt script file ? </h3>

To use this program you will have to use a .txt file containing the script of the video.
For the moment, this program supports 2 types of edits. 

<h4> Edit Style 1 : </h4>

```
//DO NOT REMOVE ----- characters
//Comments are written using "//" 
//Configuration Line
edit_type=1,fps=30
------------------------------------------
//Perso Line
//PathOfPerso bodyImgPath ShowVidPath WinnerVidPath (in ResFolder)
Persos/One_piece/Sanji body.png vid1.mp4 vid2.mp4
Persos/One_Piece/Luffy_Wano body.png vid1.mp4 vid2.mp4
------------------------------------------
//backgroundPath in res folder
Backgrounds/back3.jpg
------------------------------------------
//song path in res folder
Musique/Song1
------------------------------------------
//Title 
Naruto_(sage_mode) VS Luffy
------------------------------------------
//Comparisons
//if edit 1 : SKILL winner
//if edit 2 : perso1 perso2 winner
BATTLE_IQ 0
SPEED 0
STRENGTH 1
DURABILTY 0
SKILLS/ABILITIES 0
TALK_NO_JUTSU 0
OVERALL 0 
------------------------------------------
```

<h4> Edit Style 2 : </h4>

```
//DO NOT REMOVE ----- characters
//Comments are written using "//" 
//Configuration Line
edit_type=2,fps=30
------------------------------------------
//Perso Line
//PathOfPerso bodyImgPath ShowVidPath WinnerVidPath (in ResFolder)
Persos/One_Piece/Zoro body.png vid1.mp4 vid2.mp4
Persos/Demon_Slayer/Shinobu body.png vid1.mp4 vid2.mp4
Persos/Demon_Slayer/Mitsuri body.png
Persos/Demon_Slayer/Obanai body.png
Persos/Demon_Slayer/Sanemi body.png
Persos/Demon_Slayer/Giyu body.png vid1.mp4 vid2.mp4
Persos/Demon_Slayer/Gyomei body.png
------------------------------------------
//backgroundPath in res folder
Backgrounds/back8.jpg
------------------------------------------
//song path in res folder
Musique/Song3
------------------------------------------
//Title 
Zoro VS Demon Slayer Verse
------------------------------------------
//Comparisons
//if edit 1 : SKILL winner
//if edit 2 : perso1 perso2 winner
0 1 0
0 2 0
0 3 0
0 4 0
0 5 0 
0 6 0
0 7 0
------------------------------------------
```
# Why ?

I have seen many videos with this format (of varying quality). I thought that this format could easily be automated. So I developed this tool which allows to speed up the production of videos while keeping a correct quality constantly.
