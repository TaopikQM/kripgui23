import streamlit as st
from PIL import Image

# Fungsi untuk menyimpan gambar
def save_image(image, path):
    image.save(path)

# Fungsi untuk menampilkan gambar
def display_image(image):
    st.image(image, caption='Processed Image', use_column_width=True)

# Fungsi untuk menampilkan tautan unduh gambar
def get_image_download_link(img_path, text):
    with open(img_path, 'rb') as f:
        image = f.read()
    b64_image = base64.b64encode(image).decode()
    href = f'<a href="data:image/png;base64,{b64_image}" download="{img_path}">{text}</a>'
    return href

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
                    decrypted_image = Image.open("decrypted_image.png")  # Ganti dengan path gambar terdekripsi
                    display_image(decrypted_image)
                    st.markdown(get_image_download_link('decrypted_image.png', 'Download Decrypted Image'), unsafe_allow_html=True)
                else:
                    # Panggil metode encrypt di sini
                    st.write("Encryption process...")
                    encrypted_image = Image.open("encrypted_image.png")  # Ganti dengan path gambar terenkripsi
                    display_image(encrypted_image)
                    st.markdown(get_image_download_link('encrypted_image.png', 'Download Encrypted Image'), unsafe_allow_html=True)
        else:
            st.write("Error: minimum password length: 8")

if __name__ == '__main__':
    main()
