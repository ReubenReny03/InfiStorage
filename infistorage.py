import base64
import requests
from supabase import create_client, Client
from datetime import datetime, timezone
import tkinter as tk
from tkinter import filedialog, messagebox
from tkinterdnd2 import TkinterDnD, DND_FILES  # Import for drag-and-drop functionality

# GitHub credentials
GITHUB_TOKEN = "XXXXXXXXXXXX"  # Replace with your GitHub Personal Access Token
GITHUB_REPO = "XXXXX/XXXXXXX"  # Replace with your GitHub repository (e.g., "user/repo")
GITHUB_BRANCH = "main"  # Replace with the branch you want to upload to

# Supabase credentials
SUPABASE_URL = "XXXXXXXXXXXXXXXXXXXX"  # Replace with your Supabase URL
SUPABASE_KEY = "XXXXXXXXXXXXXXXXXXXXXXXX"  # Replace with your Supabase Anon Key

# Initialize Supabase client
supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

def upload_image_to_github(image_path, target_path):
    with open(image_path, "rb") as file:
        image_content = file.read()

    base64_content = base64.b64encode(image_content).decode("utf-8")

    github_api_url = f"https://api.github.com/repos/{GITHUB_REPO}/contents/{target_path}"

    payload = {
        "message": f"Upload {target_path}",
        "content": base64_content,
        "branch": GITHUB_BRANCH,
    }

    headers = {
        "Authorization": f"token {GITHUB_TOKEN}",
        "Content-Type": "application/json",
    }

    response = requests.put(github_api_url, json=payload, headers=headers)

    if response.status_code in [201, 200]:
        raw_url = f"https://raw.githubusercontent.com/{GITHUB_REPO}/{GITHUB_BRANCH}/{target_path}"
        return raw_url
    else:
        return None

def save_metadata_to_supabase(title, description, image_url):
    data = {
        "title": title,
        "description": description,
        "image_url": image_url,
        "uploaded_at": datetime.now(timezone.utc).isoformat(),
    }

    response = supabase.table("images").insert(data).execute()
    return response

def handle_upload(image_path):
    title = title_entry.get()
    description = description_entry.get()

    if not title or not description:
        messagebox.showerror("Missing Information", "Please provide a title and description.")
        return

    target_path = f"images/image_{datetime.now(timezone.utc).isoformat()}.jpg"

    raw_url = upload_image_to_github(image_path, target_path)
    if raw_url:
        response = save_metadata_to_supabase(title, description, raw_url)
        messagebox.showinfo(str(response))
    else:
        messagebox.showerror("GitHub Error", "Failed to upload the image to GitHub.")

def on_drop(event):
    image_path = event.data.strip()  # Get the file path
    handle_upload(image_path)

# Tkinter GUI setup with Drag-and-Drop
root = TkinterDnD.Tk()  # Initialize TkinterDnD
root.title("Image Upload Tool with Drag-and-Drop")

frame = tk.Frame(root, padx=10, pady=10)
frame.pack(pady=20)

tk.Label(frame, text="Title:").grid(row=0, column=0, sticky="e")
title_entry = tk.Entry(frame, width=40)
title_entry.grid(row=0, column=1, pady=5)

tk.Label(frame, text="Description:").grid(row=1, column=0, sticky="e")
description_entry = tk.Entry(frame, width=40)
description_entry.grid(row=1, column=1, pady=5)

drag_drop_label = tk.Label(root, text="Drag and drop your image file here", width=50, height=5, relief="ridge", bg="lightgrey")
drag_drop_label.pack(pady=20)

drag_drop_label.drop_target_register(DND_FILES)
drag_drop_label.dnd_bind('<<Drop>>', on_drop)

upload_button = tk.Button(frame, text="Browse File", command=lambda: handle_upload(filedialog.askopenfilename(filetypes=[("Image files", "*.png;*.jpg;*.jpeg")])))
upload_button.grid(row=2, columnspan=2, pady=10)

root.mainloop()
