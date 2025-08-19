import tkinter as tk
from tkinter import scrolledtext

# ----------------------- Predefined Responses -----------------------
responses = {
    "hello": "Hello! 👋 How can I help you today?",
    "hi": "Hi there! 😊 How are you?",
    "how are you": "I'm just a chatbot, but I'm functioning perfectly! 🤖",
    "bye": "Goodbye! Have a great day! 🌟",
    "default": "Sorry, I didn't understand that. Try saying 'hello' or 'bye'."
}

# ----------------------- Functions -----------------------
def send_message():
    user_msg = user_entry.get().strip()
    if user_msg == "":
        return
    chat_area.config(state='normal')
    chat_area.insert(tk.END, f"You: {user_msg}\n")
    user_entry.delete(0, tk.END)

    # Get chatbot response
    response = responses.get(user_msg.lower(), responses["default"])
    chat_area.insert(tk.END, f"Bot: {response}\n\n")
    chat_area.config(state='disabled')
    chat_area.yview(tk.END)

# ----------------------- GUI Setup -----------------------
root = tk.Tk()
root.title("🤖 Basic Chatbot")
root.geometry("500x500")
root.config(bg="#1e1e1e")

title = tk.Label(root, text="Basic Chatbot", font=("Arial Rounded MT Bold", 18), bg="#1e1e1e", fg="#FF0000")
title.pack(pady=10)

# Chat area
chat_area = scrolledtext.ScrolledText(root, wrap=tk.WORD, state='disabled', width=60, height=20, font=("Arial", 12), bg="#000000", fg="#FFFFFF")
chat_area.pack(pady=10)

# User entry
entry_frame = tk.Frame(root, bg="#1e1e1e")
entry_frame.pack(pady=10)

user_entry = tk.Entry(entry_frame, width=40, font=("Arial", 12))
user_entry.grid(row=0, column=0, padx=5)

send_btn = tk.Button(entry_frame, text="Send", bg="#FF0000", fg="white", font=("Arial", 12, "bold"), command=send_message)
send_btn.grid(row=0, column=1, padx=5)

# Run GUI
root.mainloop()
