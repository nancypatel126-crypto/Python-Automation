
import os
import shutil


# File categories
FILE_TYPES = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".webp"],
    "Documents": [".pdf", ".doc", ".docx", ".txt", ".xlsx", ".pptx"],
    "Videos": [".mp4", ".mkv", ".avi", ".mov"],
    "Audio": [".mp3", ".wav", ".aac"],
    "Programs": [".py", ".java", ".cpp", ".exe"],
    "Archives": [".zip", ".rar", ".7z"]
}


def organize_files(folder_path):

    if not os.path.isdir(folder_path):
        print("Error: Folder does not exist!")
        return

    moved_count = 0

    for file_name in os.listdir(folder_path):

        source_path = os.path.join(folder_path, file_name)

        # Skip folders
        if not os.path.isfile(source_path):
            continue

        extension = os.path.splitext(file_name)[1].lower()

        category = "Others"

        # Find file category
        for folder_name, extensions in FILE_TYPES.items():
            if extension in extensions:
                category = folder_name
                break

        destination_folder = os.path.join(
            folder_path, category
        )

        try:
            os.makedirs(destination_folder, exist_ok=True)

            destination_path = os.path.join(
                destination_folder, file_name
            )

            # Avoid overwriting existing files
            if os.path.exists(destination_path):
                print(f"Skipped duplicate file: {file_name}")
                continue

            shutil.move(source_path, destination_path)

            print(f"Moved: {file_name} -> {category}")
            moved_count += 1

        except OSError as error:
            print(f"Could not move {file_name}: {error}")

    print("\nFile Organization Completed!")
    print("Total files moved:", moved_count)


def main():

    print("=" * 40)
    print("       AUTOMATIC FILE ORGANIZER")
    print("=" * 40)

    folder_path = input(
        "Enter folder path to organize: "
    ).strip().strip('"')

    organize_files(folder_path)


if __name__ == "__main__":
    main()
