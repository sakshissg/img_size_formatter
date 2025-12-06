# 📁 Image Resizer with Hierarchical ZIP Output

This project provides a simple yet powerful script that:

- ✅ Takes a hierarchical folder path as input  
- ✅ Recursively finds all images inside all sub-folders  
- ✅ Converts every image to a fixed size  
- ✅ Preserves the exact same folder hierarchy in the output  
- ✅ Creates a ZIP file containing all resized images  

---

## 🚀 Features

- **Recursive folder scanning:** Automatically detects all images inside nested folders.  
- **Fixed-size image conversion:** Resizes images to user-defined dimensions.  
- **Hierarchy preservation:** Output ZIP mirrors the same folder structure as the input.  
- **Supports common image formats:** JPG, PNG, JPEG, WebP, BMP, TIFF, etc.  
- **Fast and lightweight:** Built using Python and Pillow.  

---

## 📂 Example

**Input Folder Structure:**
```
input_folder/
├── site1/
│   ├── front.jpg
│   └── back.png
├── site2/
│   └── subfolder/
│       └── abc.jpeg
└── xyz.png
```

**Output (inside the ZIP):**
```
output.zip
└── resized/
    ├── site1/
    │   ├── front.jpg
    │   └── back.png
    ├── site2/
    │   └── subfolder/
    │       └── abc.jpeg
    └── xyz.png
```

---

## 🛠️ How It Works

1. You provide the path of the input folder.  
2. The script recursively scans all files.  
3. Every valid image is:
   - Opened  
   - Resized to a fixed width × height  
   - Saved to a temporary output directory with the same folder structure.  
4. Finally, the script compresses everything into a ZIP file.  

---

## 📦 Requirements

Install dependencies:
```
pip install pillow
```

---

## ▶️ Usage

Run the Script:
```
python image_resizer.py <input_folder_path> <width> <height>
```

**Example:**
```
python image_resizer.py "C:/users/project/images" 512 512
```

This will:

- Resize all images to 512×512  
- Generate a ZIP file named `output_images.zip` in the project directory  

---

## 🧩 Supported Image Formats

- JPEG / JPG  
- PNG  
- BMP  
- TIFF  
- WebP  

---

## 📘 Notes

- Non-image files are safely ignored.  
- If an image fails to process, the script continues without stopping the entire run.  
- Output directory is auto-generated and cleaned before ZIP creation.  

---

## 📝 License

This project is provided under the **MIT License**.
```
