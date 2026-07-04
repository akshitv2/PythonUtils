import os
from PIL import Image


def remove_metadata_from_folder(folder_path):
    # Supported image extensions
    valid_extensions = ('.jpg', '.jpeg', '.png', '.webp', '.tiff')

    if not os.path.exists(folder_path):
        print(f"Error: Folder '{folder_path}' does not exist.")
        return

    for filename in os.listdir(folder_path):
        if filename.lower().endswith(valid_extensions):
            file_path = os.path.join(folder_path, filename)
            try:
                # Open image and strip metadata by rebuilding pixel data
                with Image.open(file_path) as img:
                    data = list(img.getdata())
                    clean_img = Image.new(img.mode, img.size)
                    clean_img.putdata(data)

                    # Overwrite the original file
                    clean_img.save(file_path)
                    print(f"Cleared metadata: {filename}")
            except Exception as e:
                print(f"Failed to process {filename}: {e}")


# Example Usage
if __name__ == "__main__":
    # Replace with your folder path (e.g., "C:/Users/Name/Pictures" or "images_folder")
    target_folder = "../assets/input"

    remove_metadata_from_folder(target_folder)