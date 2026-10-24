from pathlib import Path
import shutil
import tkinter as tk
from tkinter import ttk, filedialog
import os


def open_insctruction():

    guide_menu = tk.Tk()
    guide_menu.title("Guide Menu")
    guide_menu.geometry("900x300")
    guide_menu.minsize(900, 300)
    guide_menu.maxsize(900, 300)

    guide_menu.config(
        background="black")
    
    title = tk.Label(
        guide_menu,
          text="How to use this file sorter?",
            font=("impact",20, "bold"))
    title.pack(pady=30)

    faq = tk.Label(
        guide_menu,
          text="To use this file sorter you have to choose a folder you want to sort. After you chose the folder just click on ""Sort this file""",
            font=("arial black", 10))
    faq.pack(pady=(10, 0))

    faq2 = ttk.Label(
        guide_menu,
          text="After u chose a folder to sort, you have to choose folder you want to create a foldera where will be all your sorted files ",
            font=("arial black", 10))
    faq2.pack(pady=(1, 10))



    guide_menu.mainloop()


#Start of main function
def open_window():

    window = tk.Tk()
    style = ttk.Style()


    style.configure(
        "Big.TButton",
        font=("arial black", 12),
        padding=(15,8)
    )

    
    window.title("File sorter")
    window.geometry("500x500")
    window.minsize(500, 500)

    selected_folder = ""
    selected_home_folder = ""

    title = ttk.Label(
        window,
          text= "File sorter",
            font=("impact", 30, "bold"))
    title.pack(pady=(50, 30))

    folder_label = ttk.Label(
        window,
          text="No folder chose",
            font=("arial black", 11, "bold"))
    folder_label.pack(pady=(10, 1))

    home_folder_label = ttk.Label(
        window,
          text="no home folder chose",
            font=("arial black", 11, "bold"))
    home_folder_label.pack(pady=(2,10))


    
    def choose_home_folder():

        nonlocal selected_home_folder

        home_folder = filedialog.askdirectory()
        if home_folder :
            selected_home_folder = home_folder
            home_folder_label.config(
                text=
                f"Home folder: {home_folder}")
            return selected_home_folder



    def choose_folder():

        nonlocal selected_folder

        folder = filedialog.askdirectory()
        if folder:
            selected_folder = folder
            folder_label.config(
                text=
                f"Folder to sort: {folder}")
            return selected_folder


        
    def sort_folder():

        if not selected_folder :
            folder_label.config(
                text="Choose a folder to sort!!!")
            return
        
        if not selected_home_folder :
            home_folder_label.config(
                text="Choose a home folder!!!")
            return
        
        folder = Path(selected_folder)
        home_folder = Path(selected_home_folder)

        moved_count = 0
        for file in folder.iterdir():
            if file.is_file():
                if is_protecdet_file(file):
                    continue
                category = get_category(file)
                destination = get_destination(home_folder, category)
                new_path = get_unique_path(destination, file)
                shutil.move(str(file) , str(new_path))
                moved_count += 1
                description.config(
                    text=
                    f"Sorting complete | Moved files:{moved_count}")



    sort_button = ttk.Button(
        window,
          text="Sort this file",
            style="Big.TButton",
              command=
              lambda:sort_folder())
    sort_button.pack(pady=(15, 3))

    choose_button = ttk.Button(
        window,
          text="Choose a folder",
            style="Big.TButton",
              command=
              lambda: choose_folder())
    choose_button.pack(pady=3)

    home_folder = ttk.Button(
        window,
          text="Choose home folder",
            style="Big.TButton",
              command=
              lambda:choose_home_folder())
    home_folder.pack(pady=3)

    insctruction_button = ttk.Button(
        window,
          text= "Guide",
            style="Big.TButton",
              command=
              lambda: open_insctruction())
    insctruction_button.pack(pady=(3, 3))

    description = ttk.Label(window,
                             text="",
                               font=("arial black", 15),
                                 wraplength=1000)
    description.pack(pady=(15, 0))



    window.mainloop()
# End of main function



def get_destination(home_folder, category):

    destination = home_folder / category
    destination.mkdir(exist_ok=True)
    return destination



def get_unique_path(destination, file):
    new_path = destination/file.name
    counter = 1

    while new_path.exists():

        new_name = f"{file.stem} ({counter}){file.suffix}"
        new_path = destination / new_name
        counter += 1

    return new_path



def get_category(file):
    extension = file.suffix.lower()
    if extension in [
        ".jpg", ".jpeg", ".png", ".webp"] :
        return "Images"
    
    elif extension in [
        ".docx", ".txt", ".log", ".pptx", ".pdf"] :
        return "Documents"
    
    elif extension in [".exe", ".msi"] :
        return "Applications"
    
    else:
        return "Other"


    
def is_protecdet_file(file):
   
    protected_extensions = [
        ".dll", ".sys", ".drv", ".ocx", ".bat", ".cmd", ".ps1", ".reg"]
    if file.suffix.lower() in protected_extensions:
        return True
    
    return False



if 10 == 10:
    open_window()



