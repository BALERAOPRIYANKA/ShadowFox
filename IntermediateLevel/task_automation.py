import os
import shutil

source_folder = "source_images"
destination_folder = "moved_images"

os.makedirs(destination_folder, exist_ok=True)

if not os.path.exists(source_folder):
    os.makedirs(source_folder)
    print("Created source_images folder.")
    print("Add some .jpg files and run the script again.")
else:
    moved = 0
    for file in os.listdir(source_folder):
        if file.lower().endswith(".jpg"):
            shutil.move(
                os.path.join(source_folder, file),
                os.path.join(destination_folder, file)
            )
            moved += 1

    print(f"{moved} JPG file(s) moved successfully.")
