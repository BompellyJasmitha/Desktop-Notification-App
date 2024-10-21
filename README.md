###    Desktop Notification App
A simple GUI application built with Python's Tkinter library that allows users to set notifications with customizable titles, messages, and sound alerts.

# Table of Contents
1. Features
2. Requirements
3. Installation
4. Usage
5. How It Works
6. File Formats Supported
7. License

# Features
Set custom notification titles and messages.
Choose audio alerts from .mp3 or .wav files.
Select a logo for the notification in .ico format.
Notifications can be set to appear after a specified delay in minutes.
Clear input fields easily.

# Requirements
To run this application, ensure you have the following installed:

1. Python 3.x
2. Pip (Python package installer)

# Libraries
You need to install the following Python libraries:

tkinter (usually included with Python)
Pillow (for image handling)
plyer (for cross-platform notifications)
pygame (for audio playback)
threading (for background tasks, part of standard library)

You can install the required libraries using pip:

##      pip install Pillow plyer pygame


# Installation
Clone this repository or download the source code.
Navigate to the project directory.
Make sure all dependencies are installed as mentioned above.


#   Usage

1. Run the application:
python app.py

2. Fill in the fields:
Title to Notification: Enter the title of your notification.
Display Message: Enter the message to be displayed.
Set Time: Specify the time (in minutes) when the notification should appear.

3. Select an audio file:
Click on Select Audio to choose a .mp3 or .wav file.

4. Select a logo:
Click on Select Logo to choose a logo image in .ico format.

5. Click Set Notification to schedule your notification.

6. You can clear all fields by clicking the Clear button or exit the application by clicking Exit.

#   How It Works

The app uses Tkinter to create the GUI and handle user interactions.
Notifications are created using the plyer library for cross-platform compatibility.
Audio alerts are played using pygame when a notification is triggered.
A background thread is used to manage notification timing without freezing the GUI.

#   File Formats Supported

# Audio Files:
.mp3
.wav

# Logo Files:
.ico (required)
Other common image formats (but will notify to choose .ico)

# License
This project is licensed under the MIT License. See the LICENSE file for details.
