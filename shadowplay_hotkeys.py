from pynput import keyboard
import os
import time
import glob
import subprocess
import json
import threading

videos_path = os.environ["USERPROFILE"] + "\\Videos\\"  #Adjust to whereever you store your videos
videos_path =  videos_path.replace("C:\\","D:\\")       #I have mine on the D drive
log_path = "hotkeys_log.txt"

kb = keyboard.Controller()
log_ffmpeg = True

def log(text):
    with open(log_path, "a") as file:
        file.write(text + "\n")

def save_highlight(dur = 90):    
    try:
        for filename in glob.iglob(videos_path + '**/*.mp4', recursive=True):
            if ((time.time() - os.stat(filename).st_ctime) / 60) > 1:
                continue
            
            #https://stackoverflow.com/questions/3844430/how-to-get-the-duration-of-a-video-in-python
            result = subprocess.check_output(f'ffprobe -v quiet -show_streams -select_streams v:0 -of json "{filename}"',shell=True).decode()
            duration = json.loads(result)['streams'][0]['duration']
            
            if float(duration) < 120:   #Dont touch videos which are already shorter than 120s, adjust this if you want longer clips
                continue
            
            log("Trimming to " + str(dur) + "s: " + filename)
            tempname = filename + "_temp.mp4"
            os.system("ffmpeg" + ("" if log_ffmpeg else " -loglevel quiet") + " -hide_banner -sseof -" + str(dur) + " -i \"" + filename + "\" -map 0:v -map 0:a -c copy \"" + tempname + "\" >> \"" + log_path + "\" 2>&1")
            
            log("Deleting original: " + filename)
            os.remove(filename)
            os.rename(tempname, filename)
            log("Trimmed " + filename)
            
    except Exception as e:
        log(e)
        

def save_highlight90():
    kb.press(keyboard.Key.f10)      #My shortcut to save shadowplay clips is alt+f10 (defualt), so adjust accordingly
    kb.release(keyboard.Key.f10)    #The user is already holding alt, so no need to press/release it here
    log('Hotkey pressed, waiting 40s')
    t = threading.Timer(40.0, save_highlight,[90])  #Make sure your drive is fast enough to store the full video in 40s
    t.start()   #Using time.sleep in a function called by keyboard.GlobalHotKeys causes issues, thats why a new thread will be created

def save_highlight30():
    kb.press(keyboard.Key.f10)
    kb.release(keyboard.Key.f10)
    log('Hotkey pressed, waiting 40s')
    t = threading.Timer(40.0, save_highlight,[30])
    t.start()

with keyboard.GlobalHotKeys({
        '<alt>+<f11>': save_highlight90,        #These shortcuts are used by shadowplay by default for something, so make sure to unbind those in the settings
        '<alt>+<f12>': save_highlight30}) as h:
    h.join()
