# 🖼️ Image Resizer Tool

A simple Python script to **resize and convert images in batch** using the [Pillow](https://pillow.readthedocs.io/) library.


## ✨ Features

- 📁 Batch process images from a folder
- 📐 Resize to fixed dimensions
- 🔄 Convert image formats (JPG, PNG, WEBP, etc.)
- ⚙️ Easy to configure and extend


## 📦 Requirements

- Python 3.x
- Pillow (Install with pip)

```bash
pip install pillow
```

## 🗂️ Folder Structure

```bash
folder_name/
├── resize_images.py       # Main script
├── README.md
├── input_images/          # Place your images here
└── output_images/         # Resized images will be saved here
```

## ⚙️ Configuration

Inside `resize_images.py`:

```bash
new_size = (800, 800)           # Resize dimension (Width, Height)
output_format = "JPEG"          # Output image format
```
