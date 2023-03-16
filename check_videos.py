import tkinter as tk
import tkinter.scrolledtext as tkst

import video_library as lib
import font_manager as fonts

class VideoList(tk.Frame):
    def __init__(self, master=None, **kwargs):
        super().__init__(master, **kwargs)
        self.grid(sticky="W", padx=10, pady=10)

        self.scrolled_text = tkst.ScrolledText(self, width=48, height=12, wrap="none")
        self.scrolled_text.grid()

    def update_list(self, video_list):
        self.scrolled_text.delete("1.0", tk.END)
        self.scrolled_text.insert(1.0, video_list)

class VideoDetails(tk.Frame):
    def __init__(self, master=None, **kwargs):
        super().__init__(master, **kwargs)
        self.grid(sticky="NW", padx=10, pady=10)

        self.text_widget = tk.Text(self, width=24, height=4, wrap="none")
        self.text_widget.grid()

    def update_details(self, details):
        self.text_widget.delete("1.0", tk.END)
        self.text_widget.insert(1.0, details)
class StatusBar(tk.Frame):
    def __init__(self, master=None, **kwargs):
        super().__init__(master, **kwargs)
        self.grid(sticky="W", padx=10, pady=10)

        self.message = tk.StringVar()
        self.message_label = tk.Label(self, textvariable=self.message, font=("Helvetica", 10))
        self.message_label.grid()

    def update_status(self, status):
        self.message.set(status)

class CheckVideos(tk.Frame):
    def __init__(self, master=None, **kwargs):
        super().__init__(master, **kwargs)
        self.grid()

        self.create_widgets()
        self.list_videos_clicked()

    def create_widgets(self):
        self.list_videos_btn = tk.Button(self, text="List All Videos", command=self.list_videos_clicked)
        self.list_videos_btn.grid(row=0, column=0, padx=10, pady=10)
        self.enter_lbl = tk.Label(self, text="Enter Video Number")
        self.enter_lbl.grid(row=0, column=1, padx=10, pady=10)

        self.video_num_var = tk.StringVar()
        self.video_num_var.trace_add("write", self.update_video_details)
        self.input_txt = tk.Entry(self, width=3, textvariable=self.video_num_var)
        self.input_txt.grid(row=0, column=2, padx=10, pady=10)

        self.check_video_btn = tk.Button(self, text="Check Video", command=self.update_video_details)
        self.check_video_btn.grid(row=0, column=3, padx=10, pady=10)

        self.update_video_btn = tk.Button(self, text="Update Video", command=self.update_video)
        self.update_video_btn.grid(row=0, column=4, padx=10, pady=10)

        self.enter_lbl2 = tk.Label(self, text="Enter New Rating")
        self.enter_lbl2.grid(row=0, column=5, padx=10, pady=10)

        self.input_rating_txt = tk.Entry(self, width=3)
        self.input_rating_txt.grid(row=0, column=6, padx=10, pady=10)

        self.video_list = VideoList(master=self)
        self.video_details = VideoDetails(master=self)
        self.status_bar = StatusBar(master=self)

    def update_video_details(self, *args, **kwargs):
        key = self.video_num_var.get()
        name = lib.get_name(key)
        if name is not None:
            director = lib.get_director(key)
            rating = lib.get_rating(key)
            play_count = lib.get_play_count(key)
            video_details = f"{name}\nDirector: {director}\nRating: {rating}\nPlay Count: {play_count}"
            self.video_details.update_details(video_details)
        else:
            self.status_bar.update_status("Invalid video number")

    def list_videos_clicked(self):
        video_list = lib.list_all()
        self.video_list.update_list(video_list)

    def update_video(self):
        key = self.video_num_var.get()
        new_rating = self.input_rating_txt.get()

        try:
            new_rating = int(new_rating)
        except ValueError:
            self.status_bar.update_status("Invalid rating value")
            return

        if lib.update_rating(key, new_rating):
            self.status_bar.update_status("Video updated successfully")
            self.list_videos_clicked()  # Update the video list to reflect the change in rating
            self.update_video_details(None)
        else:
            self.status_bar.update_status("Invalid video number or rating")


if __name__ == "__main__":
    root = tk.Tk()
    root.title("Video Library")
    app = CheckVideos(master=root)
    app.mainloop()
