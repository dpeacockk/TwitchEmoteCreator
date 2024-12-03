import os
from PIL import Image
import shutil

# Define input and output paths
input_folder = 'IconsBeforeTransformation'
output_folder = 'Icons'
sizes = {
    'small': (28, 28),
    'medium': (56, 56),
    'large': (112, 112)
}

def resize_and_save(image_path, output_path, size):
    with Image.open(image_path) as img:
        img_resized = img.resize(size, Image.Resampling.LANCZOS)
        img_resized.save(output_path, format='PNG')
    print(f"Saved {output_path}")

def move_to_original_pictures(image_path):
    original_folder = os.path.join(output_folder, 'OriginalPictures')
    
    if not os.path.exists(original_folder):
        os.makedirs(original_folder)

    shutil.move(image_path, os.path.join(original_folder, os.path.basename(image_path)))
    print(f"Moved {image_path} to {original_folder}")

def process_images():
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for folder in sizes.keys():
        size_folder = os.path.join(output_folder, folder)
        if not os.path.exists(size_folder):
            os.makedirs(size_folder)

    original_folder = os.path.join(output_folder, 'OriginalPictures')
    if not os.path.exists(original_folder):
        os.makedirs(original_folder)

    for file_name in os.listdir(input_folder):
        input_image_path = os.path.join(input_folder, file_name)

        if not os.path.isfile(input_image_path) or not file_name.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif')):
            continue

        for folder, size in sizes.items():
            new_file_name = f"{os.path.splitext(file_name)[0]}_{size[0]}x{size[1]}.png"
            output_image_path = os.path.join(output_folder, folder, new_file_name)
            resize_and_save(input_image_path, output_image_path, size)

        move_to_original_pictures(input_image_path)

if __name__ == "__main__":
    process_images()
