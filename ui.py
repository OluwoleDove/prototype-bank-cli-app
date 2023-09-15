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
    user_firstname = firstname_entry.get()
    user_lastname = lastname_entry.get()
    user_email = email_entry.get()
    user_phone = phone_entry.get()
    user_gender = gender_var.get()
    user_dob = dob_entry.get()
    user_occupation = occupation_entry.get()
    user_city = city_entry.get()
    
    # Insert user data into your database tables here
    # You can use the variables above to insert data into 'users' and 'accounts' tables

    image_path = get_image_path_from_dialog()
    base_folder = "avatar"
    save_image_with_random_name(image_path, base_folder, user_name)

# Create a Tkinter window
root = tk.Tk()
root.title("Banking App")

# Create labels and entry fields for user input
name_label = tk.Label(root, text="Full Name:")
name_label.pack()
name_entry = tk.Entry(root)
name_entry.pack()

firstname_label = tk.Label(root, text="First Name:")
firstname_label.pack()
firstname_entry = tk.Entry(root)
firstname_entry.pack()

lastname_label = tk.Label(root, text="Last Name:")
lastname_label.pack()
lastname_entry = tk.Entry(root)
lastname_entry.pack()

email_label = tk.Label(root, text="Email:")
email_label.pack()
email_entry = tk.Entry(root)
email_entry.pack()

phone_label = tk.Label(root, text="Phone:")
phone_label.pack()
phone_entry = tk.Entry(root)
phone_entry.pack()

gender_label = tk.Label(root, text="Gender:")
gender_label.pack()
gender_var = tk.StringVar()
gender_var.set("Male")  # Default value
gender_options = ["Male", "Female", "Prefer not to say"]
gender_menu = tk.OptionMenu(root, gender_var, *gender_options)
gender_menu.pack()

dob_label = tk.Label(root, text="Date of Birth (YYYY-MM-DD):")
dob_label.pack()
dob_entry = tk.Entry(root)
dob_entry.pack()

occupation_label = tk.Label(root, text="Occupation:")
occupation_label.pack()
occupation_entry = tk.Entry(root)
occupation_entry.pack()

city_label = tk.Label(root, text="City:")
city_label.pack()
city_entry = tk.Entry(root)
city_entry.pack()

# Create a button to select an image
image_button = tk.Button(root, text="Select an image", command=get_image_path_from_dialog)
image_button.pack()

# Create a button to create an account
create_account_button = tk.Button(root, text="Create Account", command=create_account)
create_account_button.pack()

# Start the Tkinter main loop
root.mainloop()
