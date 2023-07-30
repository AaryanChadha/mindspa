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
ad_tts = gTTS(ad_text)
ad_tts.save("ad.mp3")

class MindSpa:
    def __init__(self):
        self.root = tk.Tk()
        self.start_button = tk.Button(self.root, text="START", command=self.start_thread)
        self.stop_button = tk.Button(self.root, text="STOP", command=self.stop)
        self.pause_button = tk.Button(self.root, text="PAUSE", command=self.pause)
        self.resume_button = tk.Button(self.root, text="RESUME", command=self.resume)
        self.volume_scale = tk.Scale(self.root, from_=0, to=1, resolution=0.01, orient=tk.HORIZONTAL, command=self.adjust_volume, label="Volume")
        self.start_button.pack()
        self.stop_button.pack()
        self.pause_button.pack()
        self.resume_button.pack()
        self.volume_scale.pack()
        self.audio_file = ""
        self.duration = 0
        self.start_time = 0
        self.is_paused = False
        self.is_playing_ad = False
        self.stop_event = threading.Event()
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
        mixer.music.load(self.audio_file)
        self.play()

    def stop(self):
        self.stop_event.set()
        mixer.music.stop()
        mixer.quit()
        self.root.destroy()

    def pause(self):
        if not self.is_playing_ad:
            self.is_paused = True
            mixer.music.pause()

    def resume(self):
        if not self.is_playing_ad:
            self.is_paused = False
            mixer.music.unpause()

    def play(self):
        self.is_playing_ad = False
        mixer.music.play()
        while not self.stop_event.is_set():
            if not self.is_paused and not self.is_playing_ad and (time.time() - self.start_time) > (self.duration * 60 / 5):
                self.is_playing_ad = True
                mixer.music.pause()
                mixer.music.load("ad.mp3")
                mixer.music.play()
                while mixer.music.get_busy() and not self.stop_event.is_set():
                    time.sleep(0.1)
                if self.stop_event.is_set():
                    return
                self.start_time = time.time()
                mixer.music.load(self.audio_file)
                mixer.music.play()
                self.is_playing_ad = False
            time.sleep(0.1)

    def adjust_volume(self, volume):
        volume = float(volume)
        try:
            mixer.music.set_volume(volume)
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def ask_mode(self):
        mode = simpledialog.askstring("Mode", "Choose a mode:\n1-Meditation\n2-Stress Management\n3-Sleep Improvement\n4-Mood Enhancement\n5-Study Mode\n6-Creativity Boost")
        while mode not in ['1', '2', '3', '4', '5', '6']:
            messagebox.showerror("Error", "Invalid mode selected. Please enter a number from 1 to 6.")
            mode = simpledialog.askstring("Mode", "Choose a mode:\n1-Meditation\n2-Stress Management\n3-Sleep Improvement\n4-Mood Enhancement\n5-Study Mode\n6-Creativity Boost")
        return mode

    def ask_type(self):
        type = simpledialog.askstring("Type", "Choose a type:\n1-Guided\n2-Unguided")
        while type not in ['1', '2']:
            messagebox.showerror("Error", "Invalid type selected. Please enter 1 or 2.")
            type = simpledialog.askstring("Type", "Choose a type:\n1-Guided\n2-Unguided")
        return type

    def ask_focus(self):
        focus = simpledialog.askstring("Focus", "Choose a focus:\n1-Relax\n2-Sleep\n3-Concentration")
        while focus not in ['1', '2', '3']:
            messagebox.showerror("Error", "Invalid focus selected. Please enter a number from 1 to 3.")
            focus = simpledialog.askstring("Focus", "Choose a focus:\n1-Relax\n2-Sleep\n3-Concentration")
        return focus

    def ask_duration(self):
        duration = simpledialog.askinteger("Duration", "Enter the duration in minutes:")
        while duration is None or duration <= 0:
            messagebox.showerror("Error", "Invalid duration. Please enter a positive number.")
            duration = simpledialog.askinteger("Duration", "Enter the duration in minutes:")
        return duration

    def verify_files(self, audios):
        if isinstance(audios, dict):
            for value in audios.values():
                self.verify_files(value)
        elif isinstance(audios, str):
            if not os.path.isfile(audios):
                messagebox.showerror("Error", f"File not found: {audios}")
                self.stop()

if __name__ == "__main__":
    MindSpa()
