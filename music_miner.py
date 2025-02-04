import streamlit as st

import hashlib

import matplotlib.pyplot as plt

import qrcode
st.write("music")
# Path to the MP3 file
mp3_path = "THX.mp3"
# Play MP3 file when button is pressed

if st.button('Play Sound'):

    audio_file = open(mp3_path, 'rb')

    audio_bytes = audio_file.read()

    st.audio(audio_bytes, format='audio/mp3')

 
from PIL import Image, ImageDraw

from io import BytesIO

import math
import hashlib

import matplotlib.pyplot as plt

import qrcode

from PIL import Image, ImageDraw

from io import BytesIO

import math
 

def calculate_hash(file_content):

    # Calculate the hash of the file content

    hash_object = hashlib.sha256(file_content)

    return hash_object.hexdigest()

 

def generate_barcode(hash_str):

    # Generate a bar code of the hash

    plt.bar(range(len(hash_str)), [int(x, 16) for x in hash_str], color='blue')

    plt.xlabel('Byte Index')

    plt.ylabel('Byte Value')

    plt.title('Hash Bar Code')

    return plt

 

def generate_qr_code(hash_str):

    # Generate a QR code of the hash

    qr = qrcode.QRCode(

        version=1,

        error_correction=qrcode.constants.ERROR_CORRECT_L,

        box_size=10,

        border=4,

    )

    qr.add_data(hash_str)

    qr.make(fit=True)

 

    img = qr.make_image(fill_color="black", back_color="white")

    return img

 

def convert_to_polygon_nft(qr_img):

    # Convert QR code image to a polygon NFT-like image

    img = qr_img.convert("RGBA")

    width, height = img.size

 

    # Create a new image with white background

    nft_img = Image.new("RGBA", (width, height), (255, 255, 255, 255))

    draw = ImageDraw.Draw(nft_img)

 

    # Draw a polygon (hexagon) around the QR code

    num_sides = 6

    radius = min(width, height) // 2

    center = (width // 2, height // 2)

    angle = 360 / num_sides

 

    polygon = [

        (

            center[0] + radius * math.cos(math.radians(angle * i)),

            center[1] + radius * math.sin(math.radians(angle * i)),

        )

        for i in range(num_sides)

    ]

 

    draw.polygon(polygon, outline="black", width=3)

 

    # Paste the QR code onto the NFT image

    nft_img.paste(img, (0, 0), img)

 

    return nft_img

 

def main():

    st.title("MP3 File Hash, Barcode, and QR Code Generator")

    st.write("Upload an MP3 file to calculate its SHA-256 hash and generate a bar code and QR code of the hash.")

 

    uploaded_file = st.file_uploader("Choose an MP3 file", type="mp3")

 

    if uploaded_file is not None:

        file_content = uploaded_file.read()

        st.write(f"File Name: {uploaded_file.name}")

        st.write(f"File Size: {len(file_content)} bytes")

 

        hash_str = calculate_hash(file_content)

        st.write(f"SHA-256 Hash: {hash_str}")

 

        barcode_plot = generate_barcode(hash_str)

        st.pyplot(barcode_plot)

 

        qr_img = generate_qr_code(hash_str)

        buffer = BytesIO()

        qr_img.save(buffer, format="PNG")

        buffer.seek(0)

        st.image(buffer, caption="QR Code of the Hash")

 

        nft_checkbox = st.checkbox("Convert QR Code to Polygon NFT")

 

        if nft_checkbox:

            nft_img = convert_to_polygon_nft(qr_img)

            nft_buffer = BytesIO()

            nft_img.save(nft_buffer, format="PNG")

            nft_buffer.seek(0)

            st.image(nft_buffer, caption="Polygon NFT Image")

 

if __name__ == "__main__":

    main(http://localhost:8501/)