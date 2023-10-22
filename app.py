import streamlit as st
from PIL import Image
import os

# Path penyimpanan file sementara
UPLOAD_DIR = "uploads"

# Fungsi untuk mengenkripsi gambar
def encrypt_image(image_path):
    image = Image.open(image_path)  # Membuka gambar dari path

    # Mendapatkan data piksel dari gambar
    pixels = image.load()
    width, height = image.size

    # Proses enkripsi untuk setiap piksel
    for i in range(width):
        for j in range(height):
            r, g, b = pixels[i, j]  # Mendapatkan nilai warna RGB
            # Contoh proses enkripsi dengan mengubah nilai piksel
            r = (r + 100) % 256
            g = (g + 50) % 256
            b = (b + 150) % 256
            pixels[i, j] = (r, g, b)  # Memperbarui nilai piksel

    encrypted_image = image  # Simulasikan proses enkripsi untuk contoh ini
    return encrypted_image

# Fungsi untuk mendekripsi gambar
def decrypt_image(image_path):
    image = Image.open(image_path)  # Membuka gambar dari path

    # Mendapatkan data piksel dari gambar
    pixels = image.load()
    width, height = image.size

    # Proses dekripsi untuk setiap piksel
    for i in range(width):
        for j in range(height):
            r, g, b = pixels[i, j]  # Mendapatkan nilai warna RGB
            # Contoh proses dekripsi dengan mengubah nilai piksel
            r = (r - 100) % 256
            g = (g - 50) % 256
            b = (b - 150) % 256
            pixels[i, j] = (r, g, b)  # Memperbarui nilai piksel

    decrypted_image = image  # Simulasikan proses dekripsi untuk contoh ini
    return decrypted_image

# Fungsi utama
def main():
    st.title("Image Encryption and Decryption")

    if not os.path.exists(UPLOAD_DIR):
        os.makedirs(UPLOAD_DIR)

    uploaded_file = st.file_uploader("Upload Image", type=["png", "jpg"])
    if uploaded_file is not None:
        image_path = os.path.join(UPLOAD_DIR, uploaded_file.name)
        with open(image_path, "wb") as f:
            f.write(uploaded_file.getbuffer())

        image = Image.open(image_path)
        st.image(image, caption='Uploaded Image', use_column_width=True)

        if st.button("Encrypt"):
            encrypted_image = encrypt_image(image_path)
            st.image(encrypted_image, caption='Encrypted Image', use_column_width=True)

        if st.button("Decrypt"):
            decrypted_image = decrypt_image(image_path)
            st.image(decrypted_image, caption='Decrypted Image', use_column_width=True)

if __name__ == '__main__':
    main()
