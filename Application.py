import tkinter as tk
import emojis

main_color = "wheat2"
nvy_blu = "navy blue"
dl_trq = "#03DAC6"
dl_main = "#2D2E2F"
ll_main = "gray90"
ll_pink = "#FF0266"


class Win1:
    def __init__(self, master):
        self.master = master
        self.master.geometry("600x400")
        self.frame = tk.Frame(self.master)
        self.emo_lab = tk.Label(self.frame, text=emojis.encode(f":smile::point_right:"), font=("arial", 60),
                                bg="wheat2")
        self.emo_lab.place(x=70, y=275)
        self.label = tk.Label(self.frame, text=f"WELCOME TO APP TO FIND LCM AND HCF!!!",
                              font=("comic sans", 50, "underline", "bold"),
                              wraplength=600)
        self.label.grid(row=1, column=0, columnspan=2, pady=20, padx=35, rowspan=1)
        self.label.config(fg="navy blue", bg="wheat2")
        self.button1("2", Win2)
        self.frame.config(bg="wheat2")
        self.frame.grid(ipady=20)

    def button1(self, number, _class):
        tk.Button(self.frame, text=f"NEXT", font=("comic sans", 30, "bold", "italic"), bd=5, relief="sunken",
                  fg="navy blue",
                  command=lambda: self.new_window(_class)).grid(row=2, rowspan=2, column=1, columnspan=3, ipadx=60,
                                                                ipady=10)

    def new_window(self, _class):
        self.new = tk.Toplevel(self.master)
        _class(self.new)


class Win2:
    def __init__(self, master):
        self.master = master
        self.master.geometry("390x325")
        self.frame = tk.Frame(self.master)
        self.emo_lab1 = tk.Label(self.frame, text=emojis.encode(f":point_up_2:       :point_down:"), font=("arial", 60),
                                 bg="wheat2")
        self.emo_lab1.place(x=55, y=113)
        self.label1 = tk.Label(self.frame, text=f" OR ", font=("futura", 45, "bold"))
        self.label1.grid(row=1, column=0, columnspan=2)
        self.label1.config(bg="wheat2", fg="navy blue")
        self.frame.config(bg="wheat2")
        self.button_light("3", Win_light)
        self.button_dark("4", Win_dark)
        self.frame.pack()

    def button_light(self, number, _class):
        tk.Button(self.frame, text=f"LIGHT", font=("comic sans", 30, "bold", "italic"), border=0, bg=ll_main,
                  fg="navy blue", command=lambda: self.theme_light(_class)).grid(row=0, rowspan=1, column=0,
                                                                                 columnspan=2,
                                                                                 padx=60, pady=10, ipadx=60, ipady=10)

    def button_dark(self, number, _class):
        tk.Button(self.frame, text=f"DARK", font=("comic sans", 30, "bold", "italic"), border=0, fg=dl_trq,
                  bg=dl_main,
                  command=lambda: self.theme_dark(_class)).grid(row=2, column=0, columnspan=2, padx=60,
                                                                pady=15, ipadx=60, ipady=15)

    def theme_light(self, _class):
        self.label1.config(bg="gray90")
        self.emo_lab1.config(fg="navy blue", bg="gray90")
        self.frame.config(bg="gray90")
        self.new_window(self, _class)

    def theme_dark(self, _class):
        self.label1.config(fg="#03DAC6", bg="#2D2E2F")
        self.emo_lab1.config(fg="#03DAC6", bg="#2D2E2F")
        self.frame.config(bg="#2D2E2F")
        self.new_window(self, _class)

    def new_window(self, number, _class):
        self.new = tk.Toplevel(self.master)
        _class(self.new, number)


# This is the light mode window
class Win_light:
    def __init__(self, master, number):
        self.master = master
        self.master.geometry("500x400")
        self.frame = tk.Frame(self.master)

        self.label2 = tk.Label(self.frame, text=f"Wanna find the LCM and HCF/GCD?", font=("futura", 20, "bold"), bg=ll_main)
        self.label3 = tk.Label(self.frame, text=f"Enter the numbers in the text boxes below!", font=("futura", 15), bg=ll_main)
        self.label2.pack()
        self.label3.pack()
        self.frame.config(bg=ll_main)
        self.frame.pack(fill="both")


# This is the dark mode window
class Win_dark:
    def __init__(self, master, number):
        self.master = master
        self.master.geometry("500x400")
        self.frame = tk.Frame(self.master)
        self.quit = tk.Button(self.frame, text=f"Quit this window n. 4", command=self.close_window)
        self.quit.pack()
        self.label = tk.Label(self.frame, text=f"THIS IS ONLY IN THE FOURTH WINDOW", fg=dl_trq)
        self.label.pack()
        self.frame.config(bg=dl_main)
        self.frame.pack(fill="both")

    def close_window(self):
        self.master.destroy()


root = tk.Tk()
app = Win1(root)
root.mainloop()
