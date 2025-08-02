import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
from PIL import Image, ImageTk
import random

MOODS = [
    ("Wistful", "This rock is thinking about its sedimentary past."),
    ("Existential", "Why is it a rock? Why are any of us anything?"),
    ("Playful", "It wants to skip across a lake. Right now."),
    ("Brooding", "It has secrets. Heavy, ancient secrets."),
    ("Hopeful", "It believes erosion will lead to a smoother tomorrow."),
    ("Anxiously Optimistic", "This rock has seen things, but it still believes in you."),
]

class RockMoodApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Rock Mood Detector")
        self.root.geometry("500x600")
        self.root.configure(bg="#f0f0f0")

        self.title_label = tk.Label(root, text="🪨 Rock Mood Detector", font=("Arial", 18), bg="#f0f0f0")
        self.title_label.pack(pady=10)

        self.instruction = tk.Label(root, text="Upload a picture of a rock to detect its mood.", bg="#f0f0f0")
        self.instruction.pack()

        self.upload_btn = tk.Button(root, text="Upload Rock Image", command=self.upload_image, bg="#4b8ef2", fg="white")
        self.upload_btn.pack(pady=10)

        self.image_label = tk.Label(root)
        self.image_label.pack(pady=10)

        self.mood_label = tk.Label(root, text="", font=("Arial", 14, "bold"), bg="#f0f0f0")
        self.mood_label.pack(pady=5)

        self.desc_label = tk.Label(root, text="", wraplength=400, bg="#f0f0f0")
        self.desc_label.pack(pady=5)

    def upload_image(self):
        file_path = filedialog.askopenfilename(
            filetypes=[("Image files", "*.jpg *.jpeg *.png *.gif")]
        )
        if not file_path:
            return

        try:
            image = Image.open(file_path)
            image.thumbnail((300, 300))
            self.photo = ImageTk.PhotoImage(image)
            self.image_label.config(image=self.photo)

            title, desc = random.choice(MOODS)
            self.mood_label.config(text=f"Mood: {title}")
            self.desc_label.config(text=desc)

        except Exception as e:
            messagebox.showerror("Error", f"Could not open image:\n{e}")

if __name__ == "__main__":
    root = tk.Tk()
    app = RockMoodApp(root)
    root.mainloop()
