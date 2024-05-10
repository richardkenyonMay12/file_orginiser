import os
from pathlib import Path
import shutil

# Path("audio").mkdir(exist_ok=True)
# Path("video").mkdir(exist_ok=True)
# Path("img").mkdir(exist_ok=True)
# Path("word").mkdir(exist_ok=True)
# Path("slides").mkdir(exist_ok=True)
# Path("excel").mkdir(exist_ok=True)
#
print(os.getcwd())

#os.chdir()
audio = (".3ga", ".aac", ".ac3", ".aif", ".aiff",
         ".alac", ".amr", ".ape", ".au", ".dss",
         ".flac", ".flv", ".m4a", ".m4b", ".m4p",
         ".mp3", ".mpga", ".ogg", ".oga", ".mogg",
         ".opus", ".qcp", ".tta", ".voc", ".wav",
         ".wma", ".wv")

video = (".webm", ".MTS", ".M2TS", ".TS", ".mov",
         ".mp4", ".m4p", ".m4v", ".mxf")

img = (".jpg", ".jpeg", ".jfif", ".pjpeg", ".pjp", ".png",
       ".gif", ".webp", ".svg", ".apng", ".avif")


word = ("doc","docm","docx","txt","wpd","wp5")

slides = ("pot", "potm","potx","ppam","ppsm","ppt", "ppsx","pps", "pptx")

excel = ("xla", "xlam", "xll","xlm","xls","xlsm","xlsx","xlt","xltm","xltx")

def is_audio(file):
    return os.path.splitext(file)[1] in audio

def is_audio(file):
    return os.path.splitext(file)[1] in video

def is_image(file):
    return os.path.splitext(file)[1] in img

def is_word(file):
    return os.path.splitext(file)[1] in word

def is_slides(file):
    return os.path.splitext(file)[1] in slides

def is_excel(file):
    return os.path.splitext(file)[1] in excel



# for file in os.listdir():
#     if is_audio(file):
        

