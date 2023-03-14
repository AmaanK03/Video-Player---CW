import tkinter as tk


def update_videos_clicked():
    # create and display new window
    new_window = tk.Toplevel()
    new_window.title("New Window")
    # add widgets and layout for the new window...


window = tk.Tk()
update_videos_btn = tk.Button(window, text="Update Videos", command=update_videos_clicked)
update_videos_btn.grid(row=1, column=2, padx=10, pady=10)
window.mainloop()
