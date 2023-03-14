import tkinter as tk  # Imports the tkinter library for creating GUIs
import tkinter.scrolledtext as tkst  # Import a scrolled text widget from tkinter

import video_library as lib  # Imports a video library module
import font_manager as fonts  # Imports a font manager module


def set_text(text_area, content):  # Defines a function to set the text of a given text area
    text_area.delete("1.0", tk.END)  # Deletes the current contents of the text area
    text_area.insert(1.0, content)  # Insert new content into the text area


# Defines a class to create the main GUI window
class CheckVideos():
    def __init__(self, window):
        window.geometry("750x350")  # Sets the size of the window to be 750x350 pixels
        window.title("Check Videos")

        # Create a button to list all videos, and assign it to the top left corner of the window
        list_videos_btn = tk.Button(window, text="List All Videos", command=self.list_videos_clicked)
        list_videos_btn.grid(row=0, column=0, padx=10, pady=10)

        # Create a label to prompt the user to enter a video number, and assign it to the top center of the window
        enter_lbl = tk.Label(window, text="Enter Video Number")
        enter_lbl.grid(row=0, column=1, padx=10, pady=10)

        # Create an input field for the user to enter a video number, and assign it to the top right corner of the window
        self.input_txt = tk.Entry(window, width=3)
        self.input_txt.grid(row=0, column=2, padx=10, pady=10)

        # Create a button to check the details of a selected video, and assign it to the top right of the window
        check_video_btn = tk.Button(window, text="Check Video", command=self.check_video_clicked)
        check_video_btn.grid(row=0, column=3, padx=10, pady=10)

        # Create a scrolling text box to display the video list, and assign it to the middle left of the window
        self.list_txt = tkst.ScrolledText(window, width=48, height=12, wrap="none")
        self.list_txt.grid(row=1, column=0, columnspan=3, sticky="W", padx=10, pady=10)

        # Create a text box to display the details of a selected video, and assign it to the middle right of the window
        self.video_txt = tk.Text(window, width=24, height=4, wrap="none")
        self.video_txt.grid(row=1, column=3, sticky="NW", padx=10, pady=10)

        # Create a label to display status messages, and assign it to the bottom left of the window
        self.status_lbl = tk.Label(window, text="", font=("Helvetica", 10))
        self.status_lbl.grid(row=2, column=0, columnspan=4, sticky="W", padx=10, pady=10)

        self.list_videos_clicked()  # Call the list_videos_clicked method to initially display the video list

    def check_video_clicked(self): #defines a function
        key = self.input_txt.get()
        name = lib.get_name(key)
        if name is not None:
            director = lib.get_director(key)
            rating = lib.get_rating(key)
            play_count = lib.get_play_count(key)
            video_details = f"{name}\n{director}\nrating: {rating}\nplays: {play_count}"
            set_text(self.video_txt, video_details)
        else:
            set_text(self.video_txt, f"Video {key} not found")
        self.status_lbl.configure(text="Check Video button was clicked!")

    def list_videos_clicked(self):
        video_list = lib.list_all()
        set_text(self.list_txt, video_list)
        self.status_lbl.configure(text="List Videos button was clicked!")


if __name__ == "__main__":  # only runs when this file is run as a standalone
    window = tk.Tk()  # create a TK object
    fonts.configure()  # configure the fonts
    CheckVideos(window)  # open the CheckVideo GUI
    window.mainloop()  # run the window main loop, reacting to button presses, etc
