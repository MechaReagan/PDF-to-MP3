import tkinter as tk
import random

window = tk.Tk()
window.title("Disappearing Text Writing App")
window.config(background="#ADD8E6")
window.geometry("600x800")

prompts = ["Set your story in an oracle or a fortune teller’s parlor.",
           "Set your story in a world where the currency isn’t money — or at least not money as we understand it.",
           "Start your story with someone emerging from the sea, and end it with them looking up at the stars.",
           "Write about a character who’s had their future foretold from birth — but isn’t sure if they believe it.",
           "One day, the sun rose in the west and set in the east."]
chosen_prompt = random.choice(prompts)

prompt_frame = tk.Frame(height=200, width=550)
prompt_frame.place(x=300, y=150, anchor="center")

prompt = tk.Label(prompt_frame, text=chosen_prompt, wraplength=500, font=("Arial", 14))
prompt.place(x=275, y=100, anchor="center")

writing_box = tk.Text(height=25, width=60, wrap="word" )
writing_box.place(x=300, y=550, anchor="center")
writing_box.focus()
entry = writing_box.get("1.0", "end-1c")


def check_progress():
    global entry
    if entry != writing_box.get("1.0", "end-1c"):
        entry = writing_box.get("1.0", "end-1c")
    else:
        writing_box.delete('1.0', "end")
    window.after(6000, check_progress)


window.update()
check_progress()

window.mainloop()


