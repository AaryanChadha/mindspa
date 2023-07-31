# MindSpa - NutriBoom Audio & Spiritual Product Recommendation Engine

## MindSpa - NutriBoom Audio

Welcome to MindSpa, a scientifically curated audio player designed to help you relax, meditate, manage stress, improve sleep, enhance mood, focus while studying, and boost creativity. It will make you smarter, healthier, and stronger using scientifically tailored graphs, medicinal recommendations, product recommendations, and of course, our top of the line, AI-generated, custom-curated audio library designed to supercharge your mindfulness, studying, creativity, and mood enhancement processes. This program allows you to create personalized meditation sessions to promote relaxation and well-being. Note: the use of advertisements is intentional to truly engage you in the NutriCore world!

### Setup

Before running the MindSpa program, please follow these setup instructions:

1. **Download the Audio Files:**

   Download the necessary audio files from this Google Drive link:
   [https://drive.google.com/drive/folders/1TZs1WfI4NE_36ik-bxp-2Ehfb8lUZhQ-?usp=drive_link]

   Make sure the audio files are placed in the 'Downloads' folder of your system, and they should remain unchanged in the 'mind audios' folder. If needed, unzip the downloaded folder.

2. **Install Required Python Packages:**

   Open Command Prompt (Windows) or Terminal (Mac) and run the following commands:

   ```
   pip install gTTS pygame matplotlib tk np
   ```

   If you encounter an error, try using 'pip3' instead of 'pip', or update pip using `python -m pip install --upgrade pip`.

### How to Use

The MindSpa program provides a graphical user interface (GUI) with various controls for your meditation sessions:

1. **Start a Session:**

   - Click the "START" button to begin a meditation session.
   - You will be prompted to choose the mode:
     - 1: Meditation
     - 2: Stress Management
     - 3: Sleep Improvement
     - 4: Mood Enhancement
     - 5: Study Mode
     - 6: Creativity Mode
   - If you select Meditation mode (1), you will be prompted to choose the type:
     - 1: Guided
     - 2: Unguided
   - If you choose Guided meditation, you will then choose the focus:
     - 1: Relax
     - 2: Sleep
     - 3: Concentrate
   - Next, enter the duration of your meditation session in minutes.

2. **Stop a Session:**

   - Click the "STOP" button to end the meditation session and exit the program.
   - The session duration and attention score will be saved in a session data file for future reference.

3. **Pause and Resume:**

   - During a session, you can click the "PAUSE" button to temporarily pause the audio.
   - Click the "RESUME" button to resume the session from where you left off.
   - Note that the "PAUSE" and "RESUME" buttons will be disabled during the periodic advertisements.

4. **Adjust Volume:**

   - The volume slider allows you to adjust the playback volume of the audio files.

### Attention Score and Session Data

The program calculates an "Attention Score" for each session based on your interactions. The Attention Score reflects your ability to stay focused during the session. Higher scores indicate better focus and relaxation.

All session data, including session durations and attention scores, are saved in a JSON file called "session_data.json" for future analysis and tracking.

### Permissions

MindSpa does not require any special permissions. However, it needs access to the 'Downloads' folder of your user profile to find the audio files. If the program cannot find the files, please ensure they are in the correct location and have the correct file names.

Enjoy a Relaxing MindSpa Experience!

We hope you enjoy your MindSpa experience and find relaxation and inner peace with our mood-enhancing audio sessions. Sit back, relax, and let MindSpa take care of your mental well-being!

## Spiritual Product Recommendation Engine

The Spiritual Product Recommendation Engine is designed to provide personalized product recommendations based on your name, age, zodiac and spiritual number.

### Setup

Before running the Spiritual Product Recommendation Engine program, please follow these setup instructions:

1. **Install Required Python Packages:**

   Open Command Prompt (Windows) or Terminal (Mac) and run the following commands:

   ```
   pip install tkinter
   ```

   If you encounter an error, try using 'pip3' instead of 'pip', or update pip using `python -m pip install --upgrade pip`.

### How to Use

The Spiritual Product Recommendation Engine provides a simple interface to generate recommendations:

1. **Start the Recommendation Engine:**

   - Click the "Start" button to open the input page.
   - Enter your name, age, and zodiac sign in the corresponding fields.

2. **Generate Recommendations:**

   - Click the "Next" button to view your spiritual number and product recommendation.
   - The spiritual number is calculated based on your name length and age sum.
   - The program will randomly select a product from a curated list based on your spiritual number.

3. **Product Recommendation:**

   - The recommendation page will display the spiritual number and the recommended product.
   - The recommendation is generated using scientifically-backed machine learning algorithms and insights from astrologers and spiritual experts.

4. **Buy Now:**

   - To purchase the recommended product, click the "Buy Now" button.

### Note:

We hope you enjoy exploring the world of spirituality with our recommendation engine and find joy in the product suggestions!