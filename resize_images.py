import os
from PIL import Image

# === Settings for input, output, size, output ===
input_folder = "input_images"
output_folder = "output_images"
new_size = (800, 800)  # (width, height) in pixels
output_format = "JPEG"  # Options: JPEG, PNG, WEBP, etc.

# === Create output folder if it doesn't exist ===
os.makedirs(output_folder, exist_ok=True)

for filename in os.listdir(input_folder):
    if filename.lower().endswith((".png", ".jpg", ".jpeg", ".webp")):
        input_path = os.path.join(input_folder, filename)

        # Open image
        with Image.open(input_path) as img:
            # Resize image
            resized_img = img.resize(new_size)

            # Build output path with format conversion (optional)
            base_name = os.path.splitext(filename)[0]
            output_path = os.path.join(output_folder, f"{base_name}.{output_format.lower()}")

            # Save resized image
            resized_img.save(output_path, output_format)

            print(f"Resized and saved: {output_path}")

print("Resizing complete!")
