import streamlit as st
from PIL import Image

# Fungsi untuk mengenkripsi gambar
def encrypt_image(image_path):
    image = Image.open(image_path)  # Membuka gambar dari path
    # Logika enkripsi
    # ...
    encrypted_image = image  # Simulasikan proses enkripsi untuk contoh ini
    return encrypted_image

# Fungsi untuk mendekripsi gambar
def decrypt_image(image_path):
    image = Image.open(image_path)  # Membuka gambar dari path
    # Logika dekripsi
    # ...
    decrypted_image = image  # Simulasikan proses dekripsi untuk contoh ini
    return decrypted_image

# Fungsi utama
def main():
    st.title("Image Encryption and Decryption")

    uploaded_file = st.file_uploader("Upload Image", type=["png", "jpg"])
    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        st.image(image, caption='Uploaded Image', use_column_width=True)

        if st.button("Encrypt"):
            encrypted_image = encrypt_image(uploaded_file)
            st.image(encrypted_image, caption='Encrypted Image', use_column_width=True)

        if st.button("Decrypt"):
            decrypted_image = decrypt_image(uploaded_file)
            st.image(decrypted_image, caption='Decrypted Image', use_column_width=True)

if __name__ == '__main__':
    main()
