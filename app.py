from PIL import Image
import os
import zipfile

def resize_images_to_inches(input_folder='input_images', output_folder='output_images', 
                            width_inches=0.90000165, height_inches=0.6030709, dpi=1200):
    
    # Convert inches to pixels
    width_px = int(width_inches * dpi)
    height_px = int(height_inches * dpi)
    
    # Check if input folder exists
    if not os.path.exists(input_folder):
        print(f"Error: '{input_folder}' folder not found!")
        return
    
    # Supported image formats
    supported_formats = ('.png', '.jpg', '.jpeg', '.bmp', '.gif', '.tiff', '.webp')
    
    print(f"Target size: {width_inches}x{height_inches} inches ({width_px}x{height_px} pixels at {dpi} DPI)")
    print(f"Scanning folder: {input_folder}")
    print("-" * 50)
    
    # Process each image recursively
    processed_files = []
    total_images = 0
    
    # Walk through all directories and subdirectories
    for root, dirs, files in os.walk(input_folder):
        # Get relative path from input folder
        rel_path = os.path.relpath(root, input_folder)
        
        # Create corresponding output directory
        if rel_path == '.':
            output_dir = output_folder
        else:
            output_dir = os.path.join(output_folder, rel_path)
        
        # Create output directory if it doesn't exist
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)
        
        # Process each file in current directory
        for file in files:
            if file.lower().endswith(supported_formats):
                total_images += 1
                try:
                    input_path = os.path.join(root, file)
                    output_path = os.path.join(output_dir, file)
                    
                    # Get relative path for display
                    display_path = os.path.join(rel_path, file) if rel_path != '.' else file
                    
                    # Open and resize image
                    with Image.open(input_path) as img:
                        # Convert to RGB if necessary (for PNG with transparency, etc.)
                        if img.mode in ('RGBA', 'LA', 'P'):
                            rgb_img = Image.new('RGB', img.size, (255, 255, 255))
                            if img.mode == 'P':
                                img = img.convert('RGBA')
                            rgb_img.paste(img, mask=img.split()[-1] if img.mode in ('RGBA', 'LA') else None)
                            img = rgb_img
                        
                        # Resize image to exact dimensions
                        resized_img = img.resize((width_px, height_px), Image.Resampling.LANCZOS)
                        
                        # Save with DPI information
                        resized_img.save(output_path, dpi=(dpi, dpi), quality=95)
                        
                    processed_files.append(output_path)
                    print(f"✓ Processed: {display_path}")
                    
                except Exception as e:
                    print(f"✗ Error processing {display_path}: {str(e)}")
    
    if total_images == 0:
        print(f"No images found in '{input_folder}' or its subfolders!")
        return 0
    
    print("-" * 50)
    print(f"Successfully processed {len(processed_files)} out of {total_images} images")
    
    # Create zip file of entire output folder
    if processed_files:
        zip_filename = f'{output_folder}.zip'
        print(f"\nCreating zip file: {zip_filename}")
        
        with zipfile.ZipFile(zip_filename, 'w', zipfile.ZIP_DEFLATED) as zipf:
            # Walk through output folder and add all files
            for root, dirs, files in os.walk(output_folder):
                for file in files:
                    file_path = os.path.join(root, file)
                    # Get path relative to output folder for zip archive
                    arcname = os.path.relpath(file_path, os.path.dirname(output_folder))
                    zipf.write(file_path, arcname)
        
        print(f"✓ Created zip file: {zip_filename}")
        print(f"✓ Output folder: {output_folder}")
    
    return len(processed_files)

if __name__ == "__main__":
    # Run the function
    resize_images_to_inches(
        input_folder='input_images',
        output_folder='output_images',
        width_inches=0.86000165,
        height_inches=0.6030709,
        dpi=1200  
    )
