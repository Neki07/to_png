import streamlit as sl
from PIL import Image
from io import BytesIO
import os


sl.title("JPG,JPEG to PNG")

data = sl.file_uploader("Please upload the JPG file")

if data is not None:
    try:
        bytes_data = data.getvalue()

        image_data = bytes_data
        image = Image.open(BytesIO(image_data))
    
        file_name = data.name + ".png"

        image.save(file_name)

        sl.write("File Name is ", file_name)

        with open(file_name, "rb") as file:
            btn = sl.download_button(
                label="Download image",
                data=file,
                file_name=file_name,
                mime="image/png"
            )

        os.remove(file_name)

    except Image.UnidentifiedImageError:
        sl.write("Please upload the correct format")