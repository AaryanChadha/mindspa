
MindSpa
Welcome to MindSpa - a mood-enhancing audio program developed for NutriBoom's MindSpa product (Springdales Hackathon 23).

Overview
MindSpa offers a variety of audio sessions to promote relaxation, reduce stress, improve sleep, enhance mood, boost creativity, and increase concentration. The program allows you to choose from different modes, including Meditation, Stress Management, Sleep Improvement, Mood Enhancement, Study Mode, and Creativity Boost. Each session can be customized with options such as Guided or Unguided meditation and focus areas like Relax, Sleep, or Concentrate. You can specify the duration of the session, and background music will play during the session to help you relax.

Setup
Before running the program, follow these steps:

Download Audio Files: Please download the required audio files from the Google Drive link: https://drive.google.com/drive/folders/1TZs1WfI4NE_36ik-bxp-2Ehfb8lUZhQ-?usp=sharing. After downloading, ensure that the files remain unchanged in the 'mind audios' folder within your 'Downloads' directory. The file names should not be modified for the program to access them correctly. If needed, unzip the folder before running the program.

Install Required Python Packages: MindSpa relies on several Python packages - gTTS, pygame, and tkinter. To install these packages, open Command Prompt (Windows) or Terminal (Mac) and execute the following commands:

Copy code
pip install gTTS
pip install pygame
If you encounter any issues, try using 'pip3' instead of 'pip', or ensure that your pip installation is up-to-date.

How to Use
The program provides a user-friendly GUI with the following controls:

START: Click this button to initiate a session. You will be prompted to choose the mode, type (for Meditation mode), focus (for Meditation mode), and duration of the session.

STOP: Click this button to terminate the current session and exit the program.

PAUSE: Use this button to pause the ongoing session. You can resume the session later by clicking the "RESUME" button.

RESUME: Click this button to continue a paused session.

Volume Slider: Adjust the slider to control the playback volume. Note that adjusting the volume when no music is playing will display an error message.

During each session, an advertisement will play at every 20% interval of the specified duration. The "PAUSE" and "RESUME" buttons will be disabled during the advertisement playback.

Permissions
MindSpa does not require any special permissions. However, it needs access to the 'Downloads' folder in your user profile to locate the audio files. If the program cannot find the files, ensure that they are in the correct location with the appropriate file names.

Relax and enjoy the MindSpa experience!