from tkinter import *
from PIL import Image, ImageTk
from tkinter import filedialog, messagebox
from plyer import notification
import threading
import os
import pygame
import time

# Global variables to hold the audio file and icon path
audio_file = ""
icon_file = "appicon.ico"

# Initialize pygame mixer for audio playback
pygame.mixer.init()

# Function to show notifications
def send_notification(title, msg, delay):
    time.sleep(delay)
    print("Sending notification...")
    notification.notify(
        title=title,
        message=msg,
        app_name="Notifier",
        app_icon=icon_file,
        timeout=10
    )
    if os.path.exists(audio_file):
        try:
            pygame.mixer.music.load(audio_file)
            pygame.mixer.music.play()
            while pygame.mixer.music.get_busy():
                time.sleep(1)
        except Exception as e:
            print(f"Error playing audio: {e}")
    else:
        print("Audio file not found.")

# Validate audio file extension
def validate_audio_file(file_path):
    return file_path.lower().endswith(('.mp3', '.wav'))

# Validate logo file extension
def validate_logo_file(file_path):
    return file_path.lower().endswith(('.ico', '.png', '.jpg', '.jpeg', '.gif', '.bmp', '.tiff'))

# Function to show alert with image
def show_image_alert(title, message, img_path):
    alert = Toplevel(t)
    alert.title(title)
    try:
        img = Image.open(img_path)
        tkimage = ImageTk.PhotoImage(img)
        img_label = Label(alert, image=tkimage)
        img_label.image = tkimage  # Keep a reference
        img_label.pack()
    except Exception as e:
        print(f"Error loading alert image: {e}")

    message_label = Label(alert, text=message, font=("Times New Roman", 12))
    message_label.pack(pady=10)

    close_button = Button(alert, text="Close", command=alert.destroy)
    close_button.pack(pady=5)

# Get notification details and set notification
def get_details():
    get_title = title.get(1.0, END).strip()
    get_msg = msg.get(1.0, END).strip()
    get_time = time1.get().strip()

    if not get_title or not get_msg or not get_time:
        show_image_alert("Alert", "All fields are required!", "error_image.png")
        return

    if not validate_audio_file(audio_file):
        show_image_alert("Alert", "Please select a valid audio file (.mp3 or .wav).", "error_image.png")
        return

    if not validate_logo_file(icon_file) or not icon_file.lower().endswith('.ico'):
        show_image_alert("Alert", "Please select a logo in .ico format!", "error_image.png")
        return

    try:
        int_time = int(float(get_time))
        min_to_sec = int_time * 60
        show_image_alert("Notifier Set", "Notification set!", "success_image.png")

        threading.Thread(target=send_notification, args=(get_title, get_msg, min_to_sec)).start()

    except ValueError:
        show_image_alert("Alert", "Please enter a valid numeric time.", "error_image.png")

# Function to select an audio file
def select_audio():
    global audio_file
    audio_file = filedialog.askopenfilename(filetypes=[("Audio Files", "*.mp3;*.wav")])
    if audio_file:
        if validate_audio_file(audio_file):
            audio_label.config(text=f"Selected audio: {os.path.basename(audio_file)}")
        else:
            show_image_alert("Alert", "Invalid audio file format!", "error_image.png")

# Function to select a logo image file
def select_logo():
    global icon_file
    icon_file = filedialog.askopenfilename(filetypes=[("Image Files", "*.*")])
    if icon_file:
        if validate_logo_file(icon_file):
            if not icon_file.lower().endswith('.ico'):
                show_image_alert("Alert", "Please select a logo in .ico format!", "error_image.png")
                return
            logo_label.config(text=f"Selected logo: {os.path.basename(icon_file)}")
        else:
            show_image_alert("Alert", "Invalid logo file format!", "error_image.png")

# Window setup
t = Tk()
t.title("Desktop Notification App")
t.geometry("700x500")

# Load background image
try:
    img = Image.open("notify-label.png")
    tkimage = ImageTk.PhotoImage(img)
    img_label = Label(t, image=tkimage)
    img_label.grid()
except Exception as e:
    print(f"Error loading background image: {e}")

# Title label
label = Label(t, text="SET NOTIFICATION NOW", font=("Times New Roman", 15, 'bold'),
              foreground="#000", width=60, border=5, background="#ebc554")
label.place(x=0, y=0, height=40)

# Title input
t_label = Label(t, text="Title to Notification", font=("Times New Roman", 12, 'bold'),
                foreground="#000", width=20, border=5, background="#ebc554")
t_label.place(x=50, y=49, height=30)

title = Text(t, width=25, font=("Times New Roman", 12), background="#d1cbb2")
title.place(x=250, y=49, height=35)

# Message input
m_label = Label(t, text="Display Message", font=("Times New Roman", 12, 'bold'),
                foreground="#000", width=20, border=5, background="#ebc554")
m_label.place(x=50, y=100, height=30)

msg = Text(t, width=50, font=("Times New Roman", 12), background='#d1cbb2')
msg.place(x=250, y=100, height=80)

# Time input
time_label = Label(t, text="Set Time", font=("Times New Roman", 12, 'bold'),
                   foreground="#000", width=15, border=5, background="#ebc554")
time_label.place(x=85, y=240, height=30)

time1 = Entry(t, width="18", font=("Times New Roman", 12), background='#d1cbb2', relief="groove")
time1.place(x=250, y=240, height=30)

time_min_label = Label(t, text="(in min)", font=("Times New Roman", 12, 'bold'),
                       foreground="#000", width=15, border=5, background="#ebc554")
time_min_label.place(x=370, y=240, height=30)

# Clear function
def clear_text():
    title.delete(1.0, END)
    msg.delete(1.0, END)
    time1.delete(0, END)
    audio_label.config(text="Selected audio: None")
    logo_label.config(text="Selected logo: None")

# Labels to display selected files
audio_label = Label(t, text="Selected audio: None", font=("Times New Roman", 10), background="#ebc554")
audio_label.place(x=50, y=300, height=30)

logo_label = Label(t, text="Selected logo: None", font=("Times New Roman", 10), background="#ebc554")
logo_label.place(x=50, y=330, height=30)

# Buttons
button_frame = Frame(t)
button_frame.place(x=50, y=380)

but = Button(button_frame, text="Set Notification", font=("Times New Roman", 12, 'bold'),
             fg="#fff", background="#a34ca6",
             cursor="hand2", relief="groove", command=get_details)
but.pack(side=LEFT, padx=5)

select_audio_button = Button(button_frame, text="Select Audio", font=("Times New Roman", 12, 'bold'),
                             fg="#fff", background="#a34ca6",
                             cursor="hand2", relief="groove", command=select_audio)
select_audio_button.pack(side=LEFT, padx=5)

select_logo_button = Button(button_frame, text="Select Logo", font=("Times New Roman", 12, 'bold'),
                            fg="#fff", background="#a34ca6",
                            cursor="hand2", relief="groove", command=select_logo)
select_logo_button.pack(side=LEFT, padx=5)

clear = Button(button_frame, text="Clear", font=("Times New Roman", 12, 'bold'),
               fg="#fff", cursor="hand2", bg="#a34ca6",
               command=clear_text, relief="groove")
clear.pack(side=LEFT, padx=5)

ext = Button(button_frame, text="Exit", font=("Times New Roman", 12, 'bold'),
             fg="#fff", cursor="hand2", bg="#a34ca6",
             command=t.destroy, relief="groove")
ext.pack(side=LEFT, padx=5)

t.resizable(0, 0)
t.mainloop()
