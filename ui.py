import shutil
import os
import tkinter as tk
from tkinter import filedialog
import random
import string
from db import mydb, new_db  # Import your database-related modules here

def get_image_path_from_dialog():
    root = tk.Tk()
    root.withdraw()
    file_path = filedialog.askopenfilename(title="Select an image file")
    return file_path

def generate_random_string(length):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

def save_image_with_random_name(image_path, base_folder, user_name):
    try:
        if not os.path.isfile(image_path):
            print("The specified file does not exist.")
            return

        # Create a folder inside the base folder with the user's name
        user_folder = os.path.join(base_folder, user_name)
        if not os.path.exists(user_folder):
            os.makedirs(user_folder)

        image_name = os.path.basename(image_path)
        file_name, file_extension = os.path.splitext(image_name)

        # Generate 20 random characters
        random_chars = generate_random_string(20)

        # Customize the new file name with random characters and the image extension
        new_file_name = f"{random_chars}{file_extension}"
        save_path = os.path.join(user_folder, new_file_name)

        shutil.copyfile(image_path, save_path)
        print(f"Image saved as {new_file_name} in {user_folder}")

    except Exception as e:
        print(f"An error occurred: {str(e)}")

def create_account():
    user_name = name_entry.get()
    image_path = get_image_path_from_dialog()
    base_folder = "avatar"
    save_image_with_random_name(image_path, base_folder, user_name)
    # Now you can add code to insert the user's information into your database

# Create a Tkinter window
root = tk.Tk()
root.title("Banking App")

# Create labels and entry fields for user input
name_label = tk.Label(root, text="Enter your name:")
name_label.pack()
name_entry = tk.Entry(root)
name_entry.pack()

# Create a button to select an image
image_button = tk.Button(root, text="Select an image", command=get_image_path_from_dialog)
image_button.pack()

# Create a button to create an account
create_account_button = tk.Button(root, text="Create Account", command=create_account)
create_account_button.pack()

# Start the Tkinter main loop
root.mainloop()
