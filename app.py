import streamlit as st
import getpass
import os
import random
import sys
from datetime import datetime
from itertools import cycle
try:
    import numpy as np
    from PIL import Image
except ModuleNotFoundError:
    st.write('Enter the command: pip install numpy pillow')
    sys.exit()

class ImageCrypt():
    def __init__(self, password):
        self.password = password

    # Sisipkan metode lain di sini seperti yang ditentukan dalam kode sebelumnya

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
                else:
                    # Panggil metode encrypt di sini
                    st.write("Encryption process...")
        else:
            st.write("Error: minimum password length: 8")

if __name__ == '__main__':
    main()
