<h1 align="center"> Anime Versus VideoGenerator </h1>

<p align="center">
  <img src="https://github.com/HugoM25/Anime_Versus_Video_Generator/blob/master/vid1.gif" alt="animated" />
  <img src="https://github.com/HugoM25/Anime_Versus_Video_Generator/blob/master/vid2.gif" alt="animated" />
</p>


<!-- Table of Contents -->
# Table of Contents
- [About the Project](#about-the-project)
  * [Context](#context)
  * [Made with](#made-with)
  * [Features](#features)
- [Getting Started](#getting-started)
  * [Prerequisites](#prerequisites)
  * [Installation](#installation)
  * [Files required](#files-required)
- [Usage](#usage)
  * [Commands](#commands)
  * [Scripts Writing](#scripts-writing)
     - [First Edit Style](#first-edit-style)
     - [Second Edit Style](#second-edit-style)
- [Examples](#examples)
- [License](#license)
- [Author](#author)

# About the project 



## Context

I was looking for a way to automate the creation of "shorts" type content that can be found on Youtube, Instagram, Tiktok. I discovered the format of "versus", the videos all had slightly different shapes and some looked so basic that a computer could have made them. I found the concept very simple to automate and mass produce so I made this program.

## Made with 

The project has been made 100% in python.

## Features 

This program is a command line tool to generate videos of anime characters comparisons in the same style as : [this video](https://www.youtube.com/shorts/wQrzgNojzug)
or the style of [this video](https://www.youtube.com/shorts/GL-gNR3gBA0)

# Examples

More videos can be found on this channel : https://www.tiktok.com/@animeversus2022


# Getting Started

 ## Prerequisites
 
 In order to use the program you will need to have a python 3.X interpretor installed. 
 The required libraries are listed in the [requirements.txt]() file. 
 
 ## Installation 
 
 1. Clone the project and unzip it.
 2. Install the librairies listed in [requirements.txt]()
 

## Files required 

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


# Usage 

## Commands 

To use this program you can use a command like this :

```Shell
python main.py --scriptPath pathToYourTxtFile --resFolder PathToResFolder
```

The available arguments are: 

- `--fps       ` : The fps of video
- `--supptemp  ` : Contains the decision to delete/backup the temporary files used for the video (by default True)
- `--tempFolder` : Path to the folder used to store temporary files
- `--resFolder ` : Path to the folder with the video and images resources
- `--scriptPath` : Path to the script to read


## Scripts Writing

To use this program you will have to use a .txt file containing the script of the video.
To write comments in the script start the line you want to comment with `//`.

For the moment, this program supports 2 types of edits. 

### First Edit Style 

This is an example script .txt file using Sanji and Luffy (from wano arc) to show how to write a script in the first edit style 

```txt
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

### Second Edit Style 


This is an example script .txt file using Zoro and multiple characters from Demon Slayer to show how to write a script for in the second edit style 


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

# License

Distributed under the MIT License. 

# Author 

- [@HugoM25](https://github.com/HugoM25)

