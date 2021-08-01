# Shadowplay Multilenght Clips

This python script allows you to add two (or more) durations for your shadowplay replays.  

If used as is, you can press `alt+f11` to save the last 90 seconds or `alt+f12` to save the last 30 seconds, in addition to your default (which is assumed to be `alt+f10`)

FFmpeg is used to trim the videos once the shortcut has been pressed.  
It is recommended to run this script as admin, otherwise the hotkeys won't be detectet in certain programs (for example devmgmt.msc)  

You can use the .vbs script to start the script without a cmd window popping up.  
The hotkeys `alt+f11` and `alt+f12` are used by shadowplay by default, so make sure to unbind those in the shadowplay settings.  

The code is not perfect and not beautiful but it does what it should do perfectly fine.

# Dependencies
* Shadowplay (obviously)
* [FFmpeg and FFprobe](https://www.ffmpeg.org/)
* `pip install pynput`
