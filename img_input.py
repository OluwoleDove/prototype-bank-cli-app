import shutil
import os
import tkinter as tk
from tkinter import filedialog

def get_image_path_from_dialog():
    root = tk.Tk()
    root.withdraw()
    file_path = filedialog.askopenfilename(title="Select an image file")
    return file_path

def save_image_to_folder(image_path, save_folder):
    try:
        if not os.path.isfile(image_path):
            print("The specified file does not exist.")
            return

        if not os.path.exists(save_folder):
            os.makedirs(save_folder)

        image_name = os.path.basename(image_path)
        save_path = os.path.join(save_folder, image_name)

        shutil.copyfile(image_path, save_path)
        print(f"Image saved to {save_path}")

    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    image_path = get_image_path_from_dialog()
    save_folder = "avatar"

    save_image_to_folder(image_path, save_folder)