import os
import shutil

def organize_desktop():
    desktop = os.path.join(os.path.expanduser("~"), "Desktop")

    file_types = {
        "Images": [".png", ".jpg", ".jpeg", ".gif"],
        "Documents": [".pdf", ".docx", ".txt", ".pptx"],
        "Videos": [".mp4", ".mov", ".mkv"],
        "Audio": [".mp3", ".wav"],
        "Code": [".py", ".cpp", ".java", ".html", ".css", ".js"],
        "Compressed": [".zip", ".rar", ".7z"]
    }

    other_folder = os.path.join(desktop, "Others")
    os.makedirs(other_folder, exist_ok=True)

    for filename in os.listdir(desktop):
        file_path = os.path.join(desktop, filename)

        if os.path.isfile(file_path):
            ext = os.path.splitext(filename)[1].lower()

            moved = False
            for folder, extensions in file_types.items():
                if ext in extensions:
                    dest = os.path.join(desktop, folder)
                    os.makedirs(dest, exist_ok=True)
                    shutil.move(file_path, os.path.join(dest, filename))
                    print(f"Moved → {filename} → {folder}")
                    moved = True
                    break

            if not moved:
                shutil.move(file_path, os.path.join(other_folder, filename))
                print(f"Moved → {filename} → Others")

if __name__ == "__main__":
    print("✨ Desktop Organizer Running...")
    organize_desktop()
    print("🎉 Done! Your desktop is now clean and organized.")
