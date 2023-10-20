import streamlit as st
from PIL import Image

# Menyimpan gambar
def save_image(image, path):
    image.save(path)

# Menampilkan gambar
def display_image(image):
    st.image(image, caption='Processed Image', use_column_width=True)

def main():
    st.title("Image Encryption and Decryption")

    uploaded_file = st.file_uploader("Upload Image", type=["png", "jpg"])
    if uploaded_file is not None:
        file_details = {"FileName": uploaded_file.name, "FileType": uploaded_file.type}
        st.write(file_details)

        password = st.text_input("Enter password:", value="", type="password")
        if len(password) >= 8:
            mode = st.selectbox("Choose mode:", ("Encrypt", "Decrypt"))
            if st.button("Run"):
                if mode == "Decrypt":
                    # Panggil metode decrypt di sini
                    st.write("Decryption process...")
                    decrypted_image = Image.open("path_to_your_decrypted_image.png")  # Ganti dengan path gambar terdekripsi
                    display_image(decrypted_image)
                    save_image(decrypted_image, 'decrypted_image.png')
                else:
                    # Panggil metode encrypt di sini
                    st.write("Encryption process...")
                    encrypted_image = Image.open("path_to_your_encrypted_image.png")  # Ganti dengan path gambar terenkripsi
                    display_image(encrypted_image)
                    save_image(encrypted_image, 'encrypted_image.png')
        else:
            st.write("Error: minimum password length: 8")

if __name__ == '__main__':
    main()
