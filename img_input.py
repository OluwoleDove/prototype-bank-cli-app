import shutil
import os
import tkinter as tk
from tkinter import filedialog
import random
import string

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

if __name__ == "__main__":
    user_name = input("Enter your name: ")
    image_path = get_image_path_from_dialog()
    base_folder = "avatar"

    save_image_with_random_name(image_path, base_folder, user_name)
