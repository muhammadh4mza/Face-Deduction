import cv2
import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk

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

# Create a button to select an image
button = tk.Button(root, text="Select Image", command=select_image)
button.pack(pady=20)

# Label to display the image
label = tk.Label(root)
label.pack()

# Run the application
root.mainloop()