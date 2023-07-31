import tkinter as tk
from tkinter import messagebox
import random

products = ['incense candles', 'gratitude journal', 'aura healing crystals', 'nutrismart pills', 'cleansing oils']

def calculate_spiritual_number(name, age):
    name_length = len(name)
    age_sum = sum(int(digit) for digit in str(age))
    return name_length + age_sum

def open_input_page():
    input_page = tk.Toplevel(root)
    input_page.title('Enter Details')

    label_name = tk.Label(input_page, text='Name')
    label_name.pack()
    global entry_name
    entry_name = tk.Entry(input_page)
    entry_name.pack()

    label_age = tk.Label(input_page, text='Age')
    label_age.pack()
    global entry_age
    entry_age = tk.Entry(input_page)
    entry_age.pack()

    label_zodiac = tk.Label(input_page, text='Zodiac Sign')
    label_zodiac.pack()
    global entry_zodiac
    entry_zodiac = tk.Entry(input_page)
    entry_zodiac.pack()

    button = tk.Button(input_page, text='Next', command=open_recommendation_page)
    button.pack()

def open_recommendation_page():
    name = entry_name.get()
    age = entry_age.get()
    spiritual_number = calculate_spiritual_number(name, age)
    product = random.choice(products)
    recommendation_page = tk.Toplevel(root)
    recommendation_page.title('Product Recommendation')

    spiritual_number_label = tk.Label(recommendation_page, text=f'Your spiritual number is {spiritual_number}.', justify='center')
    spiritual_number_label.pack()

    recommendation_line1 = tk.Label(recommendation_page, text='Based on your spiritual number, our scientifically', justify='center')
    recommendation_line1.pack()
    recommendation_line2 = tk.Label(recommendation_page, text='curated, expert-backed machine learning algorithms suggest', justify='center')
    recommendation_line2.pack()
    recommendation_line3 = tk.Label(recommendation_page, text=f'you to buy the following product: {product}.', justify='center')
    recommendation_line3.pack()
    recommendation_line4 = tk.Label(recommendation_page, text='Our scientists and computer engineers have worked with', justify='center')
    recommendation_line4.pack()
    recommendation_line5 = tk.Label(recommendation_page, text='astrologers and individuals who have mastered the spirit world', justify='center')
    recommendation_line5.pack()
    recommendation_line6 = tk.Label(recommendation_page, text='to curate this algorithm, and we believe that purchasing', justify='center')
    recommendation_line6.pack()
    recommendation_line7 = tk.Label(recommendation_page, text='this NutriBoom product will give you the added boost', justify='center')
    recommendation_line7.pack()
    recommendation_line8 = tk.Label(recommendation_page, text='you need to improve your life at this moment.', justify='center')
    recommendation_line8.pack()
    recommendation_line9 = tk.Label(recommendation_page, text='Trust Us. Boom Boom.', justify='center')
    recommendation_line9.pack()
    
    button = tk.Button(recommendation_page, text='Buy Now', bg='yellow', fg='black')
    button.pack()


root = tk.Tk()
root.title('MediaSpa Product Recommendation Engine')

button = tk.Button(root, text='Start', command=open_input_page)
button.pack()

root.mainloop()
