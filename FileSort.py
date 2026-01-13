from pathlib import Path
import shutil

# --- Configuration: you can add/remove extensions here ---
CATEGORIES = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".tiff", ".webp"],
    "Documents": [".pdf", ".doc", ".docx", ".txt", ".rtf", ".xlsx", ".xls", ".ppt", ".pptx", ".csv"],
    "Videos": [".mp4", ".mkv", ".mov", ".avi", ".wmv"],
    "Music": [".mp3", ".wav", ".aac", ".flac", ".m4a"],
    "Archives": [".zip", ".rar", ".7z", ".tar", ".gz"],
    "Code": [".py", ".ipynb", ".c", ".cpp", ".java", ".js", ".ts", ".html", ".css"],
    "Others": []  # fallback bucket
}

def ensure_folders(base: Path):
    for folder in CATEGORIES.keys():
        (base / folder).mkdir(exist_ok=True)

def pick_category(ext: str) -> str:
    ext = ext.lower()
    for folder, exts in CATEGORIES.items():
        if ext in exts:
            return folder
    return "Others"

def move_with_conflict_resolution(src: Path, dest_dir: Path):
    """Move file to dest_dir. If name exists, append (1), (2), ..."""
    dest = dest_dir / src.name
    if not dest.exists():
        shutil.move(str(src), str(dest))
        return dest

    stem, suffix = src.stem, src.suffix
    i = 1
    while True:
        candidate = dest_dir / f"{stem} ({i}){suffix}"
        if not candidate.exists():
            shutil.move(str(src), str(candidate))
            return candidate
        i += 1

def main():
    print("=== File Sorter ===")
    print("Enter the FULL path of the folder you want to organize.")
    print("Examples:")
    print("  Windows:  C:\\Users\\YourName\\Downloads")
    print("  macOS:    /Users/yourname/Downloads")
    print("  Linux:    /home/yourname/Downloads")
    folder_input = input("Folder path: ").strip().strip('"').strip("'")

    base = Path(folder_input).expanduser().resolve()
    if not base.exists() or not base.is_dir():
        print(" Path not found or not a folder. Please check and try again.")
        return

    # Create category folders
    ensure_folders(base)

    moved_count = 0
    skipped_count = 0

    for item in base.iterdir():
        # Skip our own category folders
        if item.is_dir() and item.name in CATEGORIES:
            continue
        # Only move files
        if not item.is_file():
            skipped_count += 1
            continue

        category = pick_category(item.suffix)
        dest_dir = base / category
        moved_to = move_with_conflict_resolution(item, dest_dir)
        print(f"Moved: {item.name}  ➜  {dest_dir.name}/{moved_to.name}")
        moved_count += 1

    print(f"\n Done! Moved {moved_count} files. Skipped {skipped_count} items (folders/unsupported).")
    print("Check your folder to see new subfolders like Images, Documents, Videos, etc.")

if __name__ == "__main__":
    main()
