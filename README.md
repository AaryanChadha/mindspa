# mindspa
 gui and code for v1 of nutriboom mindspa product (springdales hackathon 23)
 
Welcome to the MindSpa program!

This program provides several options for mood-enhancing audio files, including meditation, stress management, sleep improvement, mood enhancement, study mode, and creativity boost. 
The audio files will play for a duration you specify, with periodic advertisements.

Before you run the program, please make sure to follow these steps:

1) DOWNLOAD THE AUDIO FILES:
   Please download the necessary audio files from the following Google Drive link: 
   https://drive.google.com/drive/folders/1TZs1WfI4NE_36ik-bxp-2Ehfb8lUZhQ-?usp=sharing
   After downloading, please ensure that the files are placed into a new folder named 'mind audios' in the 'Downloads' folder of the user profile. The file names should remain unchanged for the program to find them.

2) INSTALL THE REQUIRED PYTHON PACKAGES:
   This program requires several Python packages to run. These include gTTS, pygame, and tkinter. To install these, you should open Command Prompt (Windows) or Terminal (Mac) and type in the following commands:
   pip install gTTS
    pip install pygame
    If you receive an error, you may need to use 'pip3' instead of 'pip', or you might need to update pip itself.

3) HOW TO CONTROL THE PROGRAM:
    The program has a GUI with 4 buttons and a slider:

    - "START": Click this to start a session. You will be prompted to choose the mode, type (if Meditation mode is chosen), focus (if Meditation mode is chosen), and duration.
    - "STOP": Click this to stop the session and exit the program.
    - "PAUSE": Click this to pause the current session. The session can be resumed later.
    - "RESUME": Click this to resume a paused session.
    - "Volume": This is a slider that can be used to adjust the volume of the playback. Note: Adjusting the volume when no music is playing will result in an error message.

    Note: Every 20% of the session's duration, an advertisement will play. During the advertisement, the "PAUSE" and "RESUME" buttons will be disabled.

4) PERMISSIONS:
    This program does not require any special permissions. However, it does need to be able to access the 'Downloads' folder of the user profile to find the audio files. 
    If the program can't find the files, please ensure that they're in the right location and that the file names are correct.

Happy relaxing!
