from pathlib import Path
import shutil

CATEGORIES = {
    "Images": [".jpg", ".png", ".jpeg"],
    "Documents": [".pdf", ".docx", ".txt"],
    "Videos": [".mp4", ".mkv"],
    "Music": [".mp3", ".wav"],
    "Code": [".py"],
}

def organize_folder(folder_path):
    base = Path(folder_path)

    # create folders
    for name in CATEGORIES:
        (base / name).mkdir(exist_ok=True)
    (base / "Others").mkdir(exist_ok=True)

    for file in base.iterdir():
        if file.is_file():
            moved = False
            for folder, extensions in CATEGORIES.items():
                if file.suffix.lower() in extensions:
                    shutil.move(str(file), base / folder / file.name)
                    moved = True
                    break

            if not moved:
                shutil.move(str(file), base / "Others" / file.name)

if __name__ == "__main__":
    path = input("Enter folder path: ")
    organize_folder(path)

