import tkinter as tk

import keyboard
import openai
import pyperclip
from plyer import notification

openai.api_key = "YOUR-API-KEY"


def generate_response(prompt):
    completions = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )

    message = completions.choices[0].text
    return message


def show_popup():
    popup_window = tk.Tk()
    popup_window.geometry("400x175")
    popup_window.wm_title("AI Buddy")
    left_label2 = tk.Label(popup_window, text=" \n")
    left_label2.grid(row=1, column=0, sticky='w')
    left_label1 = tk.Label(popup_window, text=" \n")
    left_label1.grid(row=1, column=1, sticky='w')
    left_label4 = tk.Label(popup_window, text=" Paste your query in the below box for Chat GPT to answer")
    left_label4.grid(row=0, column=1, sticky='w')
    left_label5 = tk.Label(popup_window, text="\n")
    left_label5.grid(row=2, column=1, sticky='w')
    label = tk.Label(popup_window, text="Query:")
    label.grid(row=2, column=0, sticky="w")
    text = tk.Text(popup_window, width=45, height=1)
    text.grid(row=2, column=1)
    left_label6 = tk.Label(popup_window, text="\n")
    left_label6.grid(row=4, column=1, sticky='w')
    button = tk.Button(popup_window, text="Submit", command=lambda: submit(text, popup_window))
    button.grid(row=5, column=1)
    popup_window.mainloop()


def submit(text, popup_window):
    user_input = text.get("1.0", "end-1c")

    out = generate_response(user_input)
    print(f"User entered: {user_input}")
    print(f"Response: {out}")
    popup_window.destroy()
    pyperclip.copy(out)
    if len(out) <= 256: notification_output = out
    notification.notify(
        title="Response copied!",
        message=f"{notification_output}",
        app_name="Ai_Buddy",
        timeout=5
    )


keyboard.add_hotkey('ctrl+alt+a', show_popup)
keyboard.wait()
