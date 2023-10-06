import shutil
import os
import tkinter as tk
from tkinter import filedialog
import random
import string
from PIL import Image, ImageTk
from tkcalendar import DateEntry  # Import DateEntry from tkcalendar

from db import mydb, new_db

def get_image_path_from_dialog():
    file_path = filedialog.askopenfilename(title="Select an image file")
    return file_path

def generate_random_string(length):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

def save_image_with_random_name(image_path, base_folder, user_name):
    try:
        if not os.path.isfile(image_path):
            print("The specified file does not exist.")
            return

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
        return save_path

    except Exception as e:
        print(f"An error occurred: {str(e)}")
        return None

def submit_user_data():
    user_name = name_entry.get()
    user_firstname = firstname_entry.get()
    user_lastname = lastname_entry.get()
    user_email = email_entry.get()
    user_phone = phone_entry.get()
    user_gender = gender_var.get()
    user_dob = dob_entry.get_date()
    user_occupation = occupation_entry.get()
    user_city = city_entry.get()

    # Insert user data into your database tables here
    # You can use the variables above to insert data into 'users' and 'accounts' tables

    # Create a folder for the user's avatar
    base_folder = "avatar"
    user_folder = os.path.join(base_folder, user_name)
    if not os.path.exists(user_folder):
        os.makedirs(user_folder)

    image_file_path = get_image_path_from_dialog()
    image_path = save_image_with_random_name(image_file_path, user_folder, user_name)

    print("User data submitted")


def update_uploaded_image():
    image_path = get_image_path_from_dialog()
    if image_path:
        img = Image.open(image_path)
        img.thumbnail((150, 150))
        img = ImageTk.PhotoImage(img)
        image_label.config(image=img)
        image_label.image = img

def transaction_selection():
    name_label.pack_forget()
    name_entry.pack_forget()
    firstname_label.pack_forget()
    firstname_entry.pack_forget()
    lastname_label.pack_forget()
    lastname_entry.pack_forget()
    email_label.pack_forget()
    email_entry.pack_forget()
    phone_label.pack_forget()
    phone_entry.pack_forget()
    gender_label.pack_forget()
    gender_menu.pack_forget()
    dob_label.pack_forget()
    dob_entry.pack_forget()
    occupation_label.pack_forget()
    occupation_entry.pack_forget()
    city_label.pack_forget()
    city_entry.pack_forget()
    image_label.pack_forget()
    image_button.pack_forget()
    submit_button.pack_forget()
    
    # Create a transaction selection page
    selection_label = tk.Label(root, text="Select Transaction:")
    selection_label.pack()
    
    transaction_options = ["Deposit", "Withdraw", "Transfer", "Block"]
    transaction_var = tk.StringVar()
    transaction_var.set(transaction_options[0])  # Default value
    transaction_menu = tk.OptionMenu(root, transaction_var, *transaction_options)
    transaction_menu.pack()
    
    # Create a button to proceed with the selected transaction
    proceed_button = tk.Button(root, text="Proceed", command=lambda: show_transaction_form(transaction_var.get()))
    proceed_button.pack()

def show_transaction_form(selected_transaction):
    # Create a form for the selected transaction
    transaction_form_label = tk.Label(root, text=f"{selected_transaction} Transaction Form:")
    transaction_form_label.pack()
    
    # Add form fields based on the selected transaction
    if selected_transaction == "Deposit":
        amount_label = tk.Label(root, text="Amount:")
        amount_label.pack()
        amount_entry = tk.Entry(root)
        amount_entry.pack()
        
    elif selected_transaction == "Withdraw":
        amount_label = tk.Label(root, text="Amount:")
        amount_label.pack()
        amount_entry = tk.Entry(root)
        amount_entry.pack()
        
    elif selected_transaction == "Transfer":
        pass
        
    elif selected_transaction == "Block":
        pass
    
    transaction_submit_button = tk.Button(root, text="Submit Transaction", command=lambda: submit_transaction(selected_transaction))
    transaction_submit_button.pack()

def submit_transaction(selected_transaction):
    if selected_transaction == "Deposit":
        pass
        
    elif selected_transaction == "Withdraw":
        pass
        
    elif selected_transaction == "Transfer":
        pass
        
    elif selected_transaction == "Block":
        pass

# Create a Tkinter window
root = tk.Tk()
root.title("Banking App")

name_label = tk.Label(root, text="Userame:")
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
gender_var.set("Male")
gender_options = ["Male", "Female", "Prefer not to say"]
gender_menu = tk.OptionMenu(root, gender_var, *gender_options)
gender_menu.pack()

# Create the DateEntry widget for DOB
dob_label = tk.Label(root, text="Date of Birth:")
dob_label.pack()
dob_entry = DateEntry(root, date_pattern="yyyy-mm-dd")  # Specify the date pattern
dob_entry.pack()

occupation_label = tk.Label(root, text="Occupation:")
occupation_label.pack()
occupation_entry = tk.Entry(root)
occupation_entry.pack()

city_label = tk.Label(root, text="City:")
city_label.pack()
city_entry = tk.Entry(root)
city_entry.pack()

# Create an image label to display the uploaded image
image_label = tk.Label(root)
image_label.pack()

image_button = tk.Button(root, text="Upload Image", command=update_uploaded_image)
image_button.pack()

submit_button = tk.Button(root, text="Submit User Data", command=submit_user_data)
submit_button.pack()

root.mainloop()