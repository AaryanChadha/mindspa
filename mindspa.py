# import time
# import os
# import getpass
# import platform
# import threading
# import tkinter as tk
# from tkinter import messagebox, simpledialog
# from gtts import gTTS
# from pygame import mixer
# import signal
# import matplotlib.pyplot as plt
# from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
# from collections import defaultdict
# import numpy as np
# import json
# import tempfile

# # setup
# username = getpass.getuser()
# os_type = platform.system()

# if os_type == "Windows":
#     downloads_dir = f"C:\\Users\\{username}\\Downloads\\mind audios"
# else:
#     downloads_dir = f"/home/{username}/Downloads/mind audios"

# audio_files = {
#     "1": {
#         "1": {
#             "1": os.path.join(downloads_dir, "guided_relax.mp3"),
#             "2": os.path.join(downloads_dir, "guided_sleep.mp3"),
#             "3": os.path.join(downloads_dir, "guided_concentrate.mp3")
#         },
#         "2": {
#             "1": os.path.join(downloads_dir, "unguided_relax.mp3"),
#             "2": os.path.join(downloads_dir, "unguided_sleep.mp3"),
#             "3": os.path.join(downloads_dir, "unguided_concentrate.mp3")
#         }
#     },
#     "2": os.path.join(downloads_dir, "stress_management.mp3"),
#     "3": os.path.join(downloads_dir, "sleep_improvement.mp3"),
#     "4": os.path.join(downloads_dir, "mood_enhancement.mp3"),
#     "5": os.path.join(downloads_dir, "studymode.mp3"),
#     "6": os.path.join(downloads_dir, "creativity_mode.mp3")
# }

# ad_text = "Your meditation quality will drastically increase by purchasing NutriBoom's flagship MediSpa products on our website, such as gratitude journals, exclusive merchandise, essential oils, pills, vitamins, juices, incense sticks, aromatherapy candles and more. These will make you healthy, wealthy, and wise. So if you care about becoming smarter, living a healthy and long life, you will not miss out on our amazing exclusive offers!"

# SESSION_FILE = "session_data.json"

# class MindSpa:
#     def __init__(self):
#         self.root = tk.Tk()
#         self.start_button = tk.Button(self.root, text="START", command=self.start_thread)
#         self.stop_button = tk.Button(self.root, text="STOP", command=self.stop)
#         self.pause_button = tk.Button(self.root, text="PAUSE", command=self.pause)
#         self.resume_button = tk.Button(self.root, text="RESUME", command=self.resume)
#         self.graph_button = tk.Button(self.root, text="GRAPHS", command=self.show_graphs)
#         self.volume_scale = tk.Scale(self.root, from_=0, to=1, resolution=0.01, orient=tk.HORIZONTAL, command=self.adjust_volume, label="Volume")
#         self.start_button.pack()
#         self.stop_button.pack()
#         self.pause_button.pack()
#         self.resume_button.pack()
#         self.graph_button.pack()
#         self.volume_scale.pack()
#         self.audio_file = ""
#         self.duration = 0
#         self.start_time = 0
#         self.is_paused = False
#         self.is_playing_ad = False
#         self.stop_event = threading.Event()
#         self.session_data = defaultdict(list)
#         self.attention_data = []
#         self.current_attention_score = 100
#         self.load_session_data()
#         mixer.init()
#         self.volume_scale.set(mixer.music.get_volume())
#         self.verify_files(audio_files)
#         signal.signal(signal.SIGINT, self.stop)
#         self.root.mainloop()

#     def start_thread(self):
#         mode = self.ask_mode()
#         if mode == "1":
#             type = self.ask_type()
#             focus = self.ask_focus()
#         else:
#             type = focus = None
#         duration = self.ask_duration()
#         threading.Thread(target=self.start, args=(mode, type, focus, duration), daemon=True).start()

#     def start(self, mode, type, focus, duration):
#         if mode == "1":
#             self.audio_file = audio_files[mode][type][focus]
#         else:
#             self.audio_file = audio_files[mode]
#         self.duration = duration
#         self.start_time = time.time()
#         self.stop_event.clear()
#         self.attention_data = []
#         self.current_attention_score = 100
#         mixer.music.load(self.audio_file)
#         self.play()

#     def stop(self):
#         self.stop_event.set()
#         mixer.music.stop()
#         session_duration = time.time() - self.start_time
#         self.session_data['session_durations'].append(session_duration)
#         self.session_data['attention_scores'].append(self.calculate_attention_score())
#         self.save_session_data()
#         self.root.quit()
#         if messagebox.askyesno("Continue?", "Would you like to start a new session?", parent=self.root):
#             self.__init__()

#     def pause(self):
#         self.is_paused = True
#         mixer.music.pause()
#         self.current_attention_score -= 10

#     def resume(self):
#         self.is_paused = False
#         mixer.music.unpause()
#         self.current_attention_score += 10

#     def adjust_volume(self, volume):
#         mixer.music.set_volume(float(volume))

#     def verify_files(self, audio_files):
#         for file in audio_files.values():
#             if isinstance(file, dict):
#                 self.verify_files(file)
#             else:
#                 if not os.path.exists(file):
#                     raise Exception(f"Audio file {file} does not exist")

#     def play(self):
#         ad_interval = self.duration / 5  # Ad will be played 5 times during the session
#         ad_count = 0
#         while not self.stop_event.is_set():
#             if not self.is_paused and not self.is_playing_ad:
#                 if time.time() - self.start_time >= ad_interval:
#                     self.play_ad()
#                     ad_count += 1
#                     if ad_count == 5:
#                         break
#                     self.start_time = time.time() 
#                     continue
#                 if not mixer.music.get_busy():
#                     mixer.music.load(self.audio_file)
#                     mixer.music.play()
#             time.sleep(1)

#     def play_ad(self):
#         self.is_playing_ad = True
#         tts = gTTS(ad_text)
#         with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as fp:
#             tts.write_to_fp(fp)
#             tmp_file = fp.name
#             mixer.music.load(tmp_file)
#             mixer.music.play()
#             while mixer.music.get_busy() and not self.stop_event.is_set():
#                 time.sleep(1)
#         os.remove(tmp_file)
#         self.is_playing_ad = False
#         mixer.music.load(self.audio_file)

#     def calculate_attention_score(self):
#         if not self.attention_data:
#             return None
#         return sum(self.attention_data) / len(self.attention_data)

#     def load_session_data(self):
#         if not os.path.exists(SESSION_FILE):
#             return
#         with open(SESSION_FILE, "r") as f:
#             self.session_data = json.load(f)

#     def save_session_data(self):
#         with open(SESSION_FILE, "w") as f:
#             json.dump(self.session_data, f)

#     def ask_mode(self):
#         return simpledialog.askstring("Input", "Enter Mode (1: Meditation, 2: Stress Management, 3: Sleep Improvement, 4: Mood Enhancement, 5: Study Mode, 6: Creativity Mode)", parent=self.root)

#     def ask_type(self):
#         return simpledialog.askstring("Input", "Enter Type (1: Guided, 2: Unguided)", parent=self.root)

#     def ask_focus(self):
#         return simpledialog.askstring("Input", "Enter Focus (1: Relax, 2: Sleep, 3: Concentrate)", parent=self.root)

#     def ask_duration(self):
#         return int(simpledialog.askstring("Input", "Enter Duration in Minutes", parent=self.root))

#     def show_graphs(self):
#         fig, ax = plt.subplots(2)
#         ax[0].plot(range(len(self.session_data['session_durations'])), self.session_data['session_durations'])
#         ax[0].set_title('Session Durations')
#         ax[0].set_xlabel('Session')
#         ax[0].set_ylabel('Duration (s)')
#         ax[1].plot(range(len(self.session_data['attention_scores'])), self.session_data['attention_scores'])
#         ax[1].set_title('Attention Scores')
#         ax[1].set_xlabel('Session')
#         ax[1].set_ylabel('Score')
#         fig.tight_layout(pad=3.0)
#         graph = FigureCanvasTkAgg(fig, master=self.root)
#         graph.get_tk_widget().pack()

# if __name__ == "__main__":
#     MindSpa()

# import time
# import os
# import getpass
# import platform
# import threading
# import tkinter as tk
# from tkinter import messagebox, simpledialog
# from gtts import gTTS
# from pygame import mixer
# import signal
# import matplotlib.pyplot as plt
# from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
# from collections import defaultdict
# import numpy as np
# import json
# import tempfile

# # setup
# username = getpass.getuser()
# os_type = platform.system()

# if os_type == "Windows":
#     downloads_dir = f"C:\\Users\\{username}\\Downloads\\mind audios"
# else:
#     downloads_dir = f"/home/{username}/Downloads/mind audios"

# audio_files = {
#     "1": {
#         "1": {
#             "1": os.path.join(downloads_dir, "guided_relax.mp3"),
#             "2": os.path.join(downloads_dir, "guided_sleep.mp3"),
#             "3": os.path.join(downloads_dir, "guided_concentrate.mp3")
#         },
#         "2": {
#             "1": os.path.join(downloads_dir, "unguided_relax.mp3"),
#             "2": os.path.join(downloads_dir, "unguided_sleep.mp3"),
#             "3": os.path.join(downloads_dir, "unguided_concentrate.mp3")
#         }
#     },
#     "2": os.path.join(downloads_dir, "stress_management.mp3"),
#     "3": os.path.join(downloads_dir, "sleep_improvement.mp3"),
#     "4": os.path.join(downloads_dir, "mood_enhancement.mp3"),
#     "5": os.path.join(downloads_dir, "studymode.mp3"),
#     "6": os.path.join(downloads_dir, "creativity_mode.mp3")
# }

# ad_text = "Your meditation quality will drastically increase by purchasing NutriBoom's flagship MediSpa products on our website, such as gratitude journals, exclusive merchandise, essential oils, pills, vitamins, juices, incense sticks, aromatherapy candles and more. These will make you healthy, wealthy, and wise. So if you care about becoming smarter, living a healthy and long life, you will not miss out on our amazing exclusive offers!"

# SESSION_FILE = "session_data.json"

# class MindSpa:
#     def __init__(self):
#         self.root = tk.Tk()
#         self.start_button = tk.Button(self.root, text="START", command=self.start_thread)
#         self.stop_button = tk.Button(self.root, text="STOP", command=self.stop)
#         self.pause_button = tk.Button(self.root, text="PAUSE", command=self.pause)
#         self.resume_button = tk.Button(self.root, text="RESUME", command=self.resume)
#         self.graph_button = tk.Button(self.root, text="GRAPHS", command=self.show_graphs)
#         self.volume_scale = tk.Scale(self.root, from_=0, to=1, resolution=0.01, orient=tk.HORIZONTAL, command=self.adjust_volume, label="Volume")
#         self.start_button.pack()
#         self.stop_button.pack()
#         self.pause_button.pack()
#         self.resume_button.pack()
#         self.graph_button.pack()
#         self.volume_scale.pack()
#         self.audio_file = ""
#         self.duration = 0
#         self.start_time = 0
#         self.is_paused = False
#         self.is_playing_ad = False
#         self.stop_event = threading.Event()
#         self.session_data = defaultdict(list)
#         self.attention_data = []
#         self.current_attention_score = 100
#         self.load_session_data()
#         mixer.init()
#         self.volume_scale.set(mixer.music.get_volume())
#         self.verify_files(audio_files)
#         signal.signal(signal.SIGINT, self.stop)
#         self.root.mainloop()

#     def start_thread(self):
#         mode = self.ask_mode()
#         if mode == "1":
#             type = self.ask_type()
#             focus = self.ask_focus()
#         else:
#             type = focus = None
#         duration = self.ask_duration()
#         threading.Thread(target=self.start, args=(mode, type, focus, duration), daemon=True).start()

#     def start(self, mode, type, focus, duration):
#         if mode == "1":
#             self.audio_file = audio_files[mode][type][focus]
#         else:
#             self.audio_file = audio_files[mode]
#         self.duration = duration
#         self.start_time = time.time()
#         self.stop_event.clear()
#         self.attention_data = []
#         self.current_attention_score = 100
#         mixer.music.load(self.audio_file)
#         self.play()

#     def stop(self):
#         self.stop_event.set()
#         mixer.music.stop()
#         session_duration = time.time() - self.start_time
#         self.session_data['session_durations'].append(session_duration)
#         self.session_data['attention_scores'].append(self.calculate_attention_score())
#         self.save_session_data()
#         self.root.quit()
#         if messagebox.askyesno("Continue?", "Would you like to start a new session?", parent=self.root):
#             self.__init__()

#     def pause(self):
#         self.is_paused = True
#         mixer.music.pause()
#         self.current_attention_score -= 10

#     def resume(self):
#         self.is_paused = False
#         mixer.music.unpause()
#         self.current_attention_score += 10

#     def adjust_volume(self, volume):
#         mixer.music.set_volume(float(volume))

#     def verify_files(self, audio_files):
#         for file in audio_files.values():
#             if isinstance(file, dict):
#                 self.verify_files(file)
#             else:
#                 if not os.path.exists(file):
#                     raise Exception(f"Audio file {file} does not exist")

#     def play(self):
#         ad_interval = self.duration / 5  # Ad will be played 5 times during the session
#         ad_count = 0
#         while not self.stop_event.is_set():
#             if not self.is_paused and not self.is_playing_ad:
#                 if time.time() - self.start_time >= ad_interval:
#                     self.play_ad()
#                     ad_count += 1
#                     if ad_count == 5:
#                         break
#                     self.start_time = time.time() 
#                     continue
#                 if not mixer.music.get_busy():
#                     mixer.music.load(self.audio_file)
#                     mixer.music.play()
#             time.sleep(1)

#     def play_ad(self):
#         self.is_playing_ad = True
#         tts = gTTS(ad_text)
#         with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as fp:
#             tts.write_to_fp(fp)
#             tmp_file = fp.name

#         # Load and play the ad
#         mixer.music.load(tmp_file)
#         mixer.music.play()

#         # Wait for the ad to finish playing
#         while mixer.music.get_busy() and not self.stop_event.is_set():
#             time.sleep(1)

#         # Clean up the temporary file
#         os.remove(tmp_file)

#         self.is_playing_ad = False
#         mixer.music.load(self.audio_file)


#     def calculate_attention_score(self):
#         if not self.attention_data:
#             return None
#         return sum(self.attention_data) / len(self.attention_data)

#     def load_session_data(self):
#         if not os.path.exists(SESSION_FILE):
#             return
#         with open(SESSION_FILE, "r") as f:
#             self.session_data = json.load(f)

#     def save_session_data(self):
#         with open(SESSION_FILE, "w") as f:
#             json.dump(self.session_data, f)

#     def ask_mode(self):
#         return simpledialog.askstring("Input", "Enter Mode (1: Meditation, 2: Stress Management, 3: Sleep Improvement, 4: Mood Enhancement, 5: Study Mode, 6: Creativity Mode)", parent=self.root)

#     def ask_type(self):
#         return simpledialog.askstring("Input", "Enter Type (1: Guided, 2: Unguided)", parent=self.root)

#     def ask_focus(self):
#         return simpledialog.askstring("Input", "Enter Focus (1: Relax, 2: Sleep, 3: Concentrate)", parent=self.root)

#     def ask_duration(self):
#         return int(simpledialog.askstring("Input", "Enter Duration in Minutes", parent=self.root))

#     def show_graphs(self):
#         fig, ax = plt.subplots(2)
#         ax[0].plot(range(len(self.session_data['session_durations'])), self.session_data['session_durations'])
#         ax[0].set_title('Session Durations')
#         ax[0].set_xlabel('Session')
#         ax[0].set_ylabel('Duration (s)')
#         ax[1].plot(range(len(self.session_data['attention_scores'])), self.session_data['attention_scores'])
#         ax[1].set_title('Attention Scores')
#         ax[1].set_xlabel('Session')
#         ax[1].set_ylabel('Score')
#         fig.tight_layout(pad=3.0)
#         graph = FigureCanvasTkAgg(fig, master=self.root)
#         graph.get_tk_widget().pack()

# if __name__ == "__main__":
#     MindSpa()
# import time
# import os
# import getpass
# import platform
# import threading
# import tkinter as tk
# from tkinter import messagebox, simpledialog
# from gtts import gTTS
# from pygame import mixer
# import signal
# import matplotlib.pyplot as plt
# from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
# from collections import defaultdict
# from datetime import datetime
# import numpy as np
# import json
# import tempfile

# # setup
# username = getpass.getuser()
# os_type = platform.system()

# if os_type == "Windows":
#     downloads_dir = f"C:\\Users\\{username}\\Downloads\\mind audios"
# else:
#     downloads_dir = f"/home/{username}/Downloads/mind audios"

# audio_files = {
#     "1": {
#         "1": {
#             "1": os.path.join(downloads_dir, "guided_relax.mp3"),
#             "2": os.path.join(downloads_dir, "guided_sleep.mp3"),
#             "3": os.path.join(downloads_dir, "guided_concentrate.mp3")
#         },
#         "2": {
#             "1": os.path.join(downloads_dir, "unguided_relax.mp3"),
#             "2": os.path.join(downloads_dir, "unguided_sleep.mp3"),
#             "3": os.path.join(downloads_dir, "unguided_concentrate.mp3")
#         }
#     },
#     "2": os.path.join(downloads_dir, "stress_management.mp3"),
#     "3": os.path.join(downloads_dir, "sleep_improvement.mp3"),
#     "4": os.path.join(downloads_dir, "mood_enhancement.mp3"),
#     "5": os.path.join(downloads_dir, "studymode.mp3"),
#     "6": os.path.join(downloads_dir, "creativity_mode.mp3")
# }

# ad_text = "Your meditation quality will drastically increase by purchasing NutriBoom's flagship MediSpa products on our website, such as gratitude journals, exclusive merchandise, essential oils, pills, vitamins, juices, incense sticks, aromatherapy candles and more. These will make you healthy, wealthy, and wise. So if you care about becoming smarter, living a healthy and long life, you will not miss out on our amazing exclusive offers!"

# SESSION_FILE = "session_data.json"

# def is_valid_mode(mode):
#     try:
#         mode = int(mode)
#         return mode in (1, 2, 3, 4, 5, 6)
#     except ValueError:
#         return False

# def is_valid_type(type):
#     try:
#         type = int(type)
#         return type in (1, 2)
#     except ValueError:
#         return False

# def is_valid_focus(focus):
#     try:
#         focus = int(focus)
#         return focus in (1, 2, 3)
#     except ValueError:
#         return False

# def is_valid_duration(duration):
#     try:
#         duration = int(duration)
#         return duration > 0
#     except ValueError:
#         return False

# class MindSpa:
#     def __init__(self):
#         self.root = tk.Tk()
#         self.start_button = tk.Button(self.root, text="START", command=self.start_thread)
#         self.stop_button = tk.Button(self.root, text="STOP", command=self.stop)
#         self.pause_button = tk.Button(self.root, text="PAUSE", command=self.pause)
#         self.resume_button = tk.Button(self.root, text="RESUME", command=self.resume)
#         self.graph_button = tk.Button(self.root, text="GRAPHS", command=self.show_graphs)
#         self.volume_scale = tk.Scale(self.root, from_=0, to=1, resolution=0.01, orient=tk.HORIZONTAL, command=self.adjust_volume, label="Volume")
#         self.start_button.pack()
#         self.stop_button.pack()
#         self.pause_button.pack()
#         self.resume_button.pack()
#         self.graph_button.pack()
#         self.volume_scale.pack()
#         self.audio_file = ""
#         self.duration = 0
#         self.start_time = 0
#         self.is_paused = False
#         self.is_playing_ad = False
#         self.stop_event = threading.Event()
#         self.session_data = defaultdict(list)
#         self.attention_data = []
#         self.current_attention_score = 100
#         self.load_session_data()
#         mixer.init()
#         self.volume_scale.set(mixer.music.get_volume())
#         self.verify_files(audio_files)
#         signal.signal(signal.SIGINT, self.stop)
#         self.root.mainloop()

#     def start_thread(self):
#         mode = self.ask_mode()
#         if mode == "1":
#             type = self.ask_type()
#             focus = self.ask_focus()
#         else:
#             type = focus = None
#         duration = self.ask_duration()
#         threading.Thread(target=self.start, args=(mode, type, focus, duration), daemon=True).start()

#     def start(self, mode, type, focus, duration):
#         if mode == "1":
#             self.audio_file = audio_files[mode][type][focus]
#         else:
#             self.audio_file = audio_files[mode]
#         self.duration = duration
#         self.start_time = time.time()
#         self.stop_event.clear()
#         self.attention_data = []
#         self.current_attention_score = 100
#         mixer.music.load(self.audio_file)
#         self.play()

#     def stop(self):
#         self.stop_event.set()
#         mixer.music.stop()
#         session_duration = time.time() - self.start_time
#         self.session_data['session_durations'].append(session_duration)
#         self.session_data['attention_scores'].append(self.calculate_attention_score())
#         self.save_session_data()
#         self.root.quit()
#         if messagebox.askyesno("Continue?", "Would you like to start a new session?", parent=self.root):
#             self.__init__()

#     def pause(self):
#         self.is_paused = True
#         mixer.music.pause()
#         self.current_attention_score -= 10

#     def resume(self):
#         self.is_paused = False
#         mixer.music.unpause()
#         self.current_attention_score += 10

#     def adjust_volume(self, volume):
#         mixer.music.set_volume(float(volume))

#     def verify_files(self, audio_files):
#         for file in audio_files.values():
#             if isinstance(file, dict):
#                 self.verify_files(file)
#             else:
#                 if not os.path.exists(file):
#                     raise Exception(f"Audio file {file} does not exist")

#     def play(self):
#         ad_interval = self.duration / 5  # Ad will be played 5 times during the session
#         ad_count = 0
#         while not self.stop_event.is_set():
#             if not self.is_paused and not self.is_playing_ad:
#                 if time.time() - self.start_time >= ad_interval:
#                     self.play_ad()
#                     ad_count += 1
#                     if ad_count == 5:
#                         break
#                     self.start_time = time.time()
#                     continue
#                 if not mixer.music.get_busy():
#                     mixer.music.load(self.audio_file)
#                     mixer.music.play()
#             time.sleep(1)

#     def play_ad(self):
#         self.is_playing_ad = True
#         tts = gTTS(ad_text)
#         with tempfile.NamedTemporaryFile(suffix=".mp3", delete=False) as fp:
#             tmp_file = fp.name
#             tts.save(tmp_file)
#             mixer.music.load(tmp_file)
#             mixer.music.play()
#             while mixer.music.get_busy() and not self.stop_event.is_set():
#                 time.sleep(1)
#         os.remove(tmp_file)
#         self.is_playing_ad = False
#         mixer.music.load(self.audio_file)

#     def calculate_attention_score(self):
#         if not self.attention_data:
#             return None
#         return sum(self.attention_data) / len(self.attention_data)

#     def load_session_data(self):
#         if not os.path.exists(SESSION_FILE):
#             return
#         with open(SESSION_FILE, "r") as f:
#             self.session_data = json.load(f)

#     def save_session_data(self):
#         with open(SESSION_FILE, "w") as f:
#             json.dump(self.session_data, f)

#     def ask_mode(self):
#         while True:
#             mode = simpledialog.askstring("Input", "Enter Mode (1: Meditation, 2: Stress Management, 3: Sleep Improvement, 4: Mood Enhancement, 5: Study Mode, 6: Creativity Mode)", parent=self.root)
#             if is_valid_mode(mode):
#                 return mode
#             else:
#                 messagebox.showerror("Error", "Invalid mode. Please enter a number between 1 and 6.")

#     def ask_type(self):
#         while True:
#             type = simpledialog.askstring("Input", "Enter Type (1: Guided, 2: Unguided)", parent=self.root)
#             if is_valid_type(type):
#                 return type
#             else:
#                 messagebox.showerror("Error", "Invalid type. Please enter either 1 or 2.")

#     def ask_focus(self):
#         while True:
#             focus = simpledialog.askstring("Input", "Enter Focus (1: Relax, 2: Sleep, 3: Concentrate)", parent=self.root)
#             if is_valid_focus(focus):
#                 return focus
#             else:
#                 messagebox.showerror("Error", "Invalid focus. Please enter a number between 1 and 3.")

#     def ask_duration(self):
#         while True:
#             duration = simpledialog.askstring("Input", "Enter Duration in Minutes", parent=self.root)
#             if is_valid_duration(duration):
#                 return int(duration)
#             else:
#                 messagebox.showerror("Error", "Invalid duration. Please enter a positive number.")

#     def show_graphs(self):
#         fig, ax = plt.subplots(2)
#         ax[0].plot(range(len(self.session_data['session_durations'])), self.session_data['session_durations'])
#         ax[0].set_title('Session Durations')
#         ax[0].set_xlabel('Session')
#         ax[0].set_ylabel('Duration (s)')
#         ax[1].plot(range(len(self.session_data['attention_scores'])), self.session_data['attention_scores'])
#         ax[1].set_title('Attention Scores')
#         ax[1].set_xlabel('Session')
#         ax[1].set_ylabel('Score')
#         fig.tight_layout(pad=3.0)
#         graph = FigureCanvasTkAgg(fig, master=self.root)
#         graph.get_tk_widget().pack()

# if __name__ == "__main__":
#     MindSpa()

# import time
# import os
# import getpass
# import platform
# import threading
# import tkinter as tk
# from tkinter import messagebox, simpledialog
# from gtts import gTTS
# from pygame import mixer
# import signal
# import matplotlib.pyplot as plt
# from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
# from collections import defaultdict
# import tempfile
# import json

# # setup
# username = getpass.getuser()
# os_type = platform.system()

# if os_type == "Windows":
#     downloads_dir = f"C:\\Users\\{username}\\Downloads\\mind audios"
# else:
#     downloads_dir = f"/home/{username}/Downloads/mind audios"

# audio_files = {
#     "1": {
#         "1": {
#             "1": os.path.join(downloads_dir, "guided_relax.mp3"),
#             "2": os.path.join(downloads_dir, "guided_sleep.mp3"),
#             "3": os.path.join(downloads_dir, "guided_concentrate.mp3")
#         },
#         "2": {
#             "1": os.path.join(downloads_dir, "unguided_relax.mp3"),
#             "2": os.path.join(downloads_dir, "unguided_sleep.mp3"),
#             "3": os.path.join(downloads_dir, "unguided_concentrate.mp3")
#         }
#     },
#     "2": os.path.join(downloads_dir, "stress_management.mp3"),
#     "3": os.path.join(downloads_dir, "sleep_improvement.mp3"),
#     "4": os.path.join(downloads_dir, "mood_enhancement.mp3"),
#     "5": os.path.join(downloads_dir, "studymode.mp3"),
#     "6": os.path.join(downloads_dir, "creativity_mode.mp3")
# }

# ad_text = "Your meditation quality will drastically increase by purchasing NutriBoom's flagship MediSpa products on our website, such as gratitude journals, exclusive merchandise, essential oils, pills, vitamins, juices, incense sticks, aromatherapy candles and more. These will make you healthy, wealthy, and wise. So if you care about becoming smarter, living a healthy and long life, you will not miss out on our amazing exclusive offers!"

# SESSION_FILE = "session_data.json"

# class MindSpa:
#     def __init__(self):
#         self.root = tk.Tk()
#         self.start_button = tk.Button(self.root, text="START", command=self.start_thread)
#         self.stop_button = tk.Button(self.root, text="STOP", command=self.stop)
#         self.pause_button = tk.Button(self.root, text="PAUSE", command=self.pause)
#         self.resume_button = tk.Button(self.root, text="RESUME", command=self.resume)
#         self.graph_button = tk.Button(self.root, text="GRAPHS", command=self.show_graphs)
#         self.volume_scale = tk.Scale(self.root, from_=0, to=1, resolution=0.01, orient=tk.HORIZONTAL, command=self.adjust_volume, label="Volume")
#         self.start_button.pack()
#         self.stop_button.pack()
#         self.pause_button.pack()
#         self.resume_button.pack()
#         self.graph_button.pack()
#         self.volume_scale.pack()
#         self.audio_file = ""
#         self.duration = 0
#         self.start_time = 0
#         self.is_paused = False
#         self.is_playing_ad = False
#         self.stop_event = threading.Event()
#         self.session_data = defaultdict(list)
#         self.attention_data = []
#         self.current_attention_score = 100
#         self.load_session_data()
#         mixer.init()
#         self.volume_scale.set(mixer.music.get_volume())
#         self.verify_files(audio_files)
#         signal.signal(signal.SIGINT, self.stop)
#         self.root.mainloop()

#     def start_thread(self):
#         mode = self.ask_mode()
#         if mode == "1":
#             type = self.ask_type()
#             focus = self.ask_focus()
#         else:
#             type = focus = None
#         duration = self.ask_duration()
#         threading.Thread(target=self.start, args=(mode, type, focus, duration), daemon=True).start()

#     def start(self, mode, type, focus, duration):
#         if mode == "1":
#             self.audio_file = audio_files[mode][type][focus]
#         else:
#             self.audio_file = audio_files[mode]
#         self.duration = duration
#         self.start_time = time.time()
#         self.stop_event.clear()
#         self.attention_data = []
#         self.current_attention_score = 100
#         mixer.music.load(self.audio_file)
#         self.play()

#     def stop(self):
#         self.stop_event.set()
#         mixer.music.stop()
#         session_duration = time.time() - self.start_time
#         self.session_data['session_durations'].append(session_duration)
#         self.session_data['attention_scores'].append(self.calculate_attention_score())
#         self.save_session_data()
#         self.root.quit()
#         if messagebox.askyesno("Continue?", "Would you like to start a new session?", parent=self.root):
#             self.__init__()

#     def pause(self):
#         self.is_paused = True
#         mixer.music.pause()
#         self.current_attention_score -= 10

#     def resume(self):
#         self.is_paused = False
#         mixer.music.unpause()
#         self.current_attention_score += 10

#     def adjust_volume(self, volume):
#         mixer.music.set_volume(float(volume))

#     def verify_files(self, audio_files):
#         for file in audio_files.values():
#             if isinstance(file, dict):
#                 self.verify_files(file)
#             else:
#                 if not os.path.exists(file):
#                     raise Exception(f"Audio file {file} does not exist")

#     def play(self):
#         ad_interval = self.duration / 5  # Ad will be played 5 times during the session
#         ad_count = 0
#         while not self.stop_event.is_set():
#             if not self.is_paused and not self.is_playing_ad:
#                 if time.time() - self.start_time >= ad_interval:
#                     self.play_ad()
#                     ad_count += 1
#                     if ad_count == 5:
#                         break
#                     self.start_time = time.time() 
#                     continue
#                 if not mixer.music.get_busy():
#                     mixer.music.load(self.audio_file)
#                     mixer.music.play()
#             time.sleep(1)

#     def play_ad(self):
#         self.is_playing_ad = True
#         tts = gTTS(ad_text)
#         with tempfile.NamedTemporaryFile(suffix=".mp3", delete=False) as fp:
#             tmp_file = fp.name
#             tts.save(tmp_file)
#             mixer.music.load(tmp_file)
#             mixer.music.play()
#             while mixer.music.get_busy() and not self.stop_event.is_set():
#                 time.sleep(1)
#         os.remove(tmp_file)
#         self.is_playing_ad = False
#         mixer.music.load(self.audio_file)

#     def calculate_attention_score(self):
#         if not self.attention_data:
#             return None
#         return sum(self.attention_data) / len(self.attention_data)

#     def load_session_data(self):
#         if not os.path.exists(SESSION_FILE):
#             return
#         with open(SESSION_FILE, "r") as f:
#             self.session_data = json.load(f)

#     def save_session_data(self):
#         with open(SESSION_FILE, "w") as f:
#             json.dump(self.session_data, f)

#     def ask_mode(self):
#         return simpledialog.askstring("Input", "Enter Mode (1: Meditation, 2: Stress Management, 3: Sleep Improvement, 4: Mood Enhancement, 5: Study Mode, 6: Creativity Mode)", parent=self.root)

#     def ask_type(self):
#         return simpledialog.askstring("Input", "Enter Type (1: Guided, 2: Unguided)", parent=self.root)

#     def ask_focus(self):
#         return simpledialog.askstring("Input", "Enter Focus (1: Relax, 2: Sleep, 3: Concentrate)", parent=self.root)

#     def ask_duration(self):
#         while True:
#             try:
#                 duration = int(simpledialog.askstring("Input", "Enter Duration in Minutes", parent=self.root))
#                 if duration <= 0:
#                     raise ValueError
#                 return duration
#             except (ValueError, TypeError):
#                 messagebox.showerror("Invalid Input", "Please enter a valid positive integer for duration.")

#     def show_graphs(self):
#         fig, ax = plt.subplots(2)
#         ax[0].plot(range(len(self.session_data['session_durations'])), self.session_data['session_durations'])
#         ax[0].set_title('Session Durations')
#         ax[0].set_xlabel('Session')
#         ax[0].set_ylabel('Duration (s)')
#         ax[1].plot(range(len(self.session_data['attention_scores'])), self.session_data['attention_scores'])
#         ax[1].set_title('Attention Scores')
#         ax[1].set_xlabel('Session')
#         ax[1].set_ylabel('Score')
#         fig.tight_layout(pad=3.0)
#         graph = FigureCanvasTkAgg(fig, master=self.root)
#         graph.get_tk_widget().pack()

# if __name__ == "__main__":
#     MindSpa()

# import time
# import os
# import getpass
# import platform
# import threading
# import tkinter as tk
# from tkinter import messagebox, simpledialog
# from gtts import gTTS
# from pygame import mixer
# import signal
# import matplotlib.pyplot as plt
# from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
# from collections import defaultdict
# import json
# import tempfile

# # setup
# username = getpass.getuser()
# os_type = platform.system()

# if os_type == "Windows":
#     downloads_dir = f"C:\\Users\\{username}\\Downloads\\mind audios"
# else:
#     downloads_dir = f"/home/{username}/Downloads/mind audios"

# audio_files = {
#     "1": {
#         "1": {
#             "1": os.path.join(downloads_dir, "guided_relax.mp3"),
#             "2": os.path.join(downloads_dir, "guided_sleep.mp3"),
#             "3": os.path.join(downloads_dir, "guided_concentrate.mp3")
#         },
#         "2": {
#             "1": os.path.join(downloads_dir, "unguided_relax.mp3"),
#             "2": os.path.join(downloads_dir, "unguided_sleep.mp3"),
#             "3": os.path.join(downloads_dir, "unguided_concentrate.mp3")
#         }
#     },
#     "2": os.path.join(downloads_dir, "stress_management.mp3"),
#     "3": os.path.join(downloads_dir, "sleep_improvement.mp3"),
#     "4": os.path.join(downloads_dir, "mood_enhancement.mp3"),
#     "5": os.path.join(downloads_dir, "studymode.mp3"),
#     "6": os.path.join(downloads_dir, "creativity_mode.mp3")
# }

# ad_text = "Your meditation quality will drastically increase by purchasing NutriBoom's flagship MediSpa products on our website, such as gratitude journals, exclusive merchandise, essential oils, pills, vitamins, juices, incense sticks, aromatherapy candles and more. These will make you healthy, wealthy, and wise. So if you care about becoming smarter, living a healthy and long life, you will not miss out on our amazing exclusive offers!"

# SESSION_FILE = "session_data.json"

# class MindSpa:
#     def __init__(self):
#         self.root = tk.Tk()
#         self.start_button = tk.Button(self.root, text="START", command=self.start_thread)
#         self.stop_button = tk.Button(self.root, text="STOP", command=self.stop)
#         self.pause_button = tk.Button(self.root, text="PAUSE", command=self.pause)
#         self.resume_button = tk.Button(self.root, text="RESUME", command=self.resume)
#         self.graph_button = tk.Button(self.root, text="GRAPHS", command=self.show_graphs)
#         self.volume_scale = tk.Scale(self.root, from_=0, to=1, resolution=0.01, orient=tk.HORIZONTAL, command=self.adjust_volume, label="Volume")
#         self.start_button.pack()
#         self.stop_button.pack()
#         self.pause_button.pack()
#         self.resume_button.pack()
#         self.graph_button.pack()
#         self.volume_scale.pack()
#         self.audio_file = ""
#         self.duration = 0
#         self.start_time = 0
#         self.is_paused = False
#         self.is_playing_ad = False
#         self.stop_event = threading.Event()
#         self.session_data = defaultdict(list)
#         self.attention_data = []
#         self.current_attention_score = 100
#         self.load_session_data()
#         mixer.init()
#         self.volume_scale.set(mixer.music.get_volume())
#         self.verify_files(audio_files)
#         signal.signal(signal.SIGINT, self.stop)
#         self.root.mainloop()

#     def start_thread(self):
#         mode = self.ask_mode()
#         if mode == "1":
#             type = self.ask_type()
#             focus = self.ask_focus()
#         else:
#             type = focus = None
#         duration = self.ask_duration()
#         threading.Thread(target=self.start, args=(mode, type, focus, duration), daemon=True).start()

#     def start(self, mode, type, focus, duration):
#         if mode == "1":
#             self.audio_file = audio_files[mode][type][focus]
#         else:
#             self.audio_file = audio_files[mode]
#         self.duration = duration
#         self.start_time = time.time()
#         self.stop_event.clear()
#         self.attention_data = []
#         self.current_attention_score = 100
#         mixer.music.load(self.audio_file)
#         self.play()

#     def stop(self):
#         self.stop_event.set()
#         mixer.music.stop()
#         session_duration = time.time() - self.start_time
#         self.session_data['session_durations'].append(session_duration)
#         self.session_data['attention_scores'].append(self.calculate_attention_score())
#         self.save_session_data()
#         self.root.quit()
#         if messagebox.askyesno("Continue?", "Would you like to start a new session?", parent=self.root):
#             self.__init__()

#     def pause(self):
#         self.is_paused = True
#         mixer.music.pause()
#         self.current_attention_score -= 10

#     def resume(self):
#         self.is_paused = False
#         mixer.music.unpause()
#         self.current_attention_score += 10

#     def adjust_volume(self, volume):
#         mixer.music.set_volume(float(volume))

#     def verify_files(self, audio_files):
#         for file in audio_files.values():
#             if isinstance(file, dict):
#                 self.verify_files(file)
#             else:
#                 if not os.path.exists(file):
#                     raise Exception(f"Audio file {file} does not exist")

#     def play(self):
#         ad_interval = self.duration / 5  # Ad will be played 5 times during the session
#         ad_count = 0
#         while not self.stop_event.is_set():
#             if not self.is_paused and not self.is_playing_ad:
#                 if time.time() - self.start_time >= ad_interval:
#                     self.play_ad()
#                     ad_count += 1
#                     if ad_count == 5:
#                         break
#                     self.start_time = time.time() 
#                     continue
#                 if not mixer.music.get_busy():
#                     mixer.music.load(self.audio_file)
#                     mixer.music.play()
#             time.sleep(1)

#     def play_ad(self):
#         self.is_playing_ad = True
#         tts = gTTS(ad_text)
#         try:
#             with tempfile.NamedTemporaryFile(suffix=".mp3", delete=False) as fp:
#                 tmp_file = fp.name
#                 tts.save(tmp_file)
#                 mixer.music.load(tmp_file)
#                 mixer.music.play()
#                 while mixer.music.get_busy() and not self.stop_event.is_set():
#                     time.sleep(1)
#         finally:
#             if os.path.exists(tmp_file):
#                 os.remove(tmp_file)
#         self.is_playing_ad = False
#         mixer.music.load(self.audio_file)


#     def calculate_attention_score(self):
#         if not self.attention_data:
#             return None
#         return sum(self.attention_data) / len(self.attention_data)

#     def load_session_data(self):
#         if not os.path.exists(SESSION_FILE):
#             return
#         with open(SESSION_FILE, "r") as f:
#             self.session_data = json.load(f)

#     def save_session_data(self):
#         with open(SESSION_FILE, "w") as f:
#             json.dump(self.session_data, f)

#     def ask_mode(self):
#         return simpledialog.askstring("Input", "Enter Mode (1: Meditation, 2: Stress Management, 3: Sleep Improvement, 4: Mood Enhancement, 5: Study Mode, 6: Creativity Mode)", parent=self.root)

#     def ask_type(self):
#         return simpledialog.askstring("Input", "Enter Type (1: Guided, 2: Unguided)", parent=self.root)

#     def ask_focus(self):
#         return simpledialog.askstring("Input", "Enter Focus (1: Relax, 2: Sleep, 3: Concentrate)", parent=self.root)

#     def ask_duration(self):
#         duration = simpledialog.askstring("Input", "Enter Duration in Minutes", parent=self.root)
#         try:
#             duration = int(duration)
#             if duration <= 0:
#                 raise ValueError
#         except ValueError:
#             messagebox.showerror("Error", "Please enter a valid positive integer for duration.")
#             return self.ask_duration()
#         return duration

#     def show_graphs(self):
#         fig, ax = plt.subplots(2)
#         ax[0].plot(range(len(self.session_data['session_durations'])), self.session_data['session_durations'])
#         ax[0].set_title('Session Durations')
#         ax[0].set_xlabel('Session')
#         ax[0].set_ylabel('Duration (s)')
#         ax[1].plot(range(len(self.session_data['attention_scores'])), self.session_data['attention_scores'])
#         ax[1].set_title('Attention Scores')
#         ax[1].set_xlabel('Session')
#         ax[1].set_ylabel('Score')
#         fig.tight_layout(pad=3.0)
#         graph = FigureCanvasTkAgg(fig, master=self.root)
#         graph.get_tk_widget().pack()

# if __name__ == "__main__":
#     MindSpa()

import time
import os
import getpass
import platform
import threading
import tkinter as tk
from tkinter import messagebox, simpledialog
from gtts import gTTS
from pygame import mixer
import signal
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from collections import defaultdict
import numpy as np
import json
import tempfile

# setup
username = getpass.getuser()
os_type = platform.system()

if os_type == "Windows":
    downloads_dir = f"C:\\Users\\{username}\\Downloads\\mind audios"
else:
    downloads_dir = f"/home/{username}/Downloads/mind audios"

audio_files = {
    "1": {
        "1": {
            "1": os.path.join(downloads_dir, "guided_relax.mp3"),
            "2": os.path.join(downloads_dir, "guided_sleep.mp3"),
            "3": os.path.join(downloads_dir, "guided_concentrate.mp3")
        },
        "2": {
            "1": os.path.join(downloads_dir, "unguided_relax.mp3"),
            "2": os.path.join(downloads_dir, "unguided_sleep.mp3"),
            "3": os.path.join(downloads_dir, "unguided_concentrate.mp3")
        }
    },
    "2": os.path.join(downloads_dir, "stress_management.mp3"),
    "3": os.path.join(downloads_dir, "sleep_improvement.mp3"),
    "4": os.path.join(downloads_dir, "mood_enhancement.mp3"),
    "5": os.path.join(downloads_dir, "studymode.mp3"),
    "6": os.path.join(downloads_dir, "creativity_mode.mp3")
}

ad_text = "Your meditation quality will drastically increase by purchasing NutriBoom's flagship MediSpa products on our website, such as gratitude journals, exclusive merchandise, essential oils, pills, vitamins, juices, incense sticks, aromatherapy candles and more. These will make you healthy, wealthy, and wise. So if you care about becoming smarter, living a healthy and long life, you will not miss out on our amazing exclusive offers!"

SESSION_FILE = "session_data.json"

class MindSpa:
    def __init__(self):
        self.root = tk.Tk()
        self.start_button = tk.Button(self.root, text="START", command=self.start_thread)
        self.stop_button = tk.Button(self.root, text="STOP", command=self.stop)
        self.pause_button = tk.Button(self.root, text="PAUSE", command=self.pause)
        self.resume_button = tk.Button(self.root, text="RESUME", command=self.resume)
        self.graph_button = tk.Button(self.root, text="GRAPHS", command=self.show_graphs)
        self.volume_scale = tk.Scale(self.root, from_=0, to=1, resolution=0.01, orient=tk.HORIZONTAL, command=self.adjust_volume, label="Volume")
        self.start_button.pack()
        self.stop_button.pack()
        self.pause_button.pack()
        self.resume_button.pack()
        self.graph_button.pack()
        self.volume_scale.pack()
        self.audio_file = ""
        self.duration = 0
        self.start_time = 0
        self.is_paused = False
        self.is_playing_ad = False
        self.stop_event = threading.Event()
        self.session_data = defaultdict(list)
        self.attention_data = []
        self.current_attention_score = 100
        self.load_session_data()
        mixer.init()
        self.volume_scale.set(mixer.music.get_volume())
        self.verify_files(audio_files)
        signal.signal(signal.SIGINT, self.stop)
        self.root.mainloop()

    def start_thread(self):
        mode = self.ask_mode()
        if mode == "1":
            type = self.ask_type()
            focus = self.ask_focus()
        else:
            type = focus = None
        duration = self.ask_duration()
        threading.Thread(target=self.start, args=(mode, type, focus, duration), daemon=True).start()

    def start(self, mode, type, focus, duration):
        if mode == "1":
            self.audio_file = audio_files[mode][type][focus]
        else:
            self.audio_file = audio_files[mode]
        self.duration = duration
        self.start_time = time.time()
        self.stop_event.clear()
        self.attention_data = []
        self.current_attention_score = 100
        mixer.music.load(self.audio_file)
        self.play()

    def stop(self):
        self.stop_event.set()
        mixer.music.stop()
        session_duration = time.time() - self.start_time
        self.session_data['session_durations'].append(session_duration)
        self.session_data['attention_scores'].append(self.calculate_attention_score())
        self.save_session_data()
        self.root.quit()
        if messagebox.askyesno("Continue?", "Would you like to start a new session?", parent=self.root):
            self.__init__()

    def pause(self):
        self.is_paused = True
        mixer.music.pause()
        self.current_attention_score -= 10

    def resume(self):
        self.is_paused = False
        mixer.music.unpause()
        self.current_attention_score += 10

    def adjust_volume(self, volume):
        mixer.music.set_volume(float(volume))

    def verify_files(self, audio_files):
        for file in audio_files.values():
            if isinstance(file, dict):
                self.verify_files(file)
            else:
                if not os.path.exists(file):
                    raise Exception(f"Audio file {file} does not exist")

    def play(self):
        ad_interval = self.duration / 5  # Ad will be played 5 times during the session
        ad_count = 0
        while not self.stop_event.is_set():
            if not self.is_paused and not self.is_playing_ad:
                if time.time() - self.start_time >= ad_interval:
                    self.play_ad()
                    ad_count += 1
                    if ad_count == 5:
                        break
                    self.start_time = time.time() 
                    continue
                if not mixer.music.get_busy():
                    mixer.music.load(self.audio_file)
                    mixer.music.play()
            time.sleep(1)

    def play_ad(self):
        self.is_playing_ad = True
        tts = gTTS(ad_text)
        fd, tmp_file = tempfile.mkstemp(suffix=".mp3")
        try:
            tts.save(tmp_file)
            sound = mixer.Sound(tmp_file)
            sound.play()
            while mixer.get_busy() and not self.stop_event.is_set():
                time.sleep(1)
        finally:
            os.close(fd)
            os.remove(tmp_file)
        self.is_playing_ad = False
        mixer.music.load(self.audio_file)

    def calculate_attention_score(self):
        if not self.attention_data:
            return None
        return sum(self.attention_data) / len(self.attention_data)

    def load_session_data(self):
        if not os.path.exists(SESSION_FILE):
            return
        with open(SESSION_FILE, "r") as f:
            self.session_data = json.load(f)

    def save_session_data(self):
        with open(SESSION_FILE, "w") as f:
            json.dump(self.session_data, f)

    def ask_mode(self):
        return simpledialog.askstring("Input", "Enter Mode (1: Meditation, 2: Stress Management, 3: Sleep Improvement, 4: Mood Enhancement, 5: Study Mode, 6: Creativity Mode)", parent=self.root)

    def ask_type(self):
        return simpledialog.askstring("Input", "Enter Type (1: Guided, 2: Unguided)", parent=self.root)

    def ask_focus(self):
        return simpledialog.askstring("Input", "Enter Focus (1: Relax, 2: Sleep, 3: Concentrate)", parent=self.root)

    def ask_duration(self):
        return int(simpledialog.askstring("Input", "Enter Duration in Minutes", parent=self.root))

    def show_graphs(self):
        fig, ax = plt.subplots(2)
        ax[0].plot(range(len(self.session_data['session_durations'])), self.session_data['session_durations'])
        ax[0].set_title('Session Durations')
        ax[0].set_xlabel('Session')
        ax[0].set_ylabel('Duration (s)')
        ax[1].plot(range(len(self.session_data['attention_scores'])), self.session_data['attention_scores'])
        ax[1].set_title('Attention Scores')
        ax[1].set_xlabel('Session')
        ax[1].set_ylabel('Score')
        fig.tight_layout(pad=3.0)
        graph = FigureCanvasTkAgg(fig, master=self.root)
        graph.get_tk_widget().pack()

if __name__ == "__main__":
    MindSpa()
