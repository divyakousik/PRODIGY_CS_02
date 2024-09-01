from PIL import Image

def image_encrypt_decryption(ip_image_path, op_image_path, key):
    try:
        image = Image.open(ip_image_path)
        pixels = image.load()
        print(f"Processing image: {ip_image_path}")

        # Check if the image has an alpha channel (RGBA)
        for i in range(image.size[0]):
            for j in range(image.size[1]):
                pixel = pixels[i, j]
                
                if len(pixel) == 3:  # RGB image
                    r, g, b = pixel
                    pixels[i, j] = (r ^ key, g ^ key, b ^ key)
                elif len(pixel) == 4:  # RGBA image
                    r, g, b, a = pixel
                    pixels[i, j] = (r ^ key, g ^ key, b ^ key, a)  # Keep the alpha channel unchanged

        image.save(op_image_path)
        print(f"Image processed and saved as {op_image_path}")
    except Exception as e:
        print(f"Error: {e}")

def encrypt_image(input_image_path, output_image_path, key):
    print("Starting encryption...")
    image_encrypt_decryption(input_image_path, output_image_path, key)

def decrypt_image(encrypted_image_path, output_image_path, key):
    print("Starting decryption...")
    image_encrypt_decryption(encrypted_image_path, output_image_path, key)

# Define file paths and encryption key
input_image = 'images.jpg'  
encrypted_image = 'encrypted_image.png'
decrypted_image = 'decrypted_image.png'
key = 123  # Encryption/Decryption key

# Perform encryption and decryption
encrypt_image(input_image, encrypted_image, key)
decrypt_image(encrypted_image, decrypted_image, key)
