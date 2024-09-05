import cv2
import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
from tkinter import font as tkfont

# Function to select an image file
def select_image():
    file_path = filedialog.askopenfilename()
    if file_path:
        detect_faces(file_path)
        
# Function to detect faces in an image
def detect_faces(image_path):
    # Load the pre-trained face detection model
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

    # Read the image
    image = cv2.imread(image_path)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Detect faces
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    # Draw rectangles around the faces
    for (x, y, w, h) in faces:
        cv2.rectangle(image, (x, y), (x+w, y+h), (255, 0, 0), 2)

        # Convert the image to RGB (OpenCV uses BGR by default)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    image = Image.fromarray(image)
    image = ImageTk.PhotoImage(image)

    # Display the image in the GUI
    label.config(image=image)
    label.image = image

# Create the main window
root = tk.Tk()
root.title("Face Detection")

# Get screen width and height
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# Set the window size to match the screen size
root.geometry(f"{screen_width}x{screen_height}")

# Load and resize the background image to the screen size
bg_image = Image.open("facerecognition.webp")
bg_image = bg_image.resize((screen_width, screen_height), Image.Resampling.LANCZOS)

# Convert the image to a Tkinter-compatible PhotoImage object
bg_photo = ImageTk.PhotoImage(bg_image)

# Create a label to display the background image
background_label = tk.Label(root, image=bg_photo)

# Place the label at the back (fill entire window)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

# Store a reference to prevent garbage collection
background_label.image = bg_photo


# Styling options
button_font = tkfont.Font(family="Helvetica", size=16, weight="bold")
button_bg = "#1e1e1e"  
button_fg = "white"    # White text color
button_active_bg = "#45a049"  # Darker green when the button is pressed
button_active_fg = "#ffffff"  # Keep white text when pressed

# Create a button to select an image with custom stylings
button = tk.Button(
    root,
    text="Select Image",
    command=select_image,
    font=button_font,     # Apply custom font
    bg=button_bg,         # Background color
    fg=button_fg,         # Foreground color (text color)
    activebackground=button_active_bg,  # Background color when clicked
    activeforeground=button_active_fg,  # Foreground color when clicked
    padx=20,              # Padding for X axis
    pady=10               # Padding for Y axis
)
button.pack(pady=20)

# Label to display the image
label = tk.Label(root)
label.pack()

# Run the application
root.mainloop()