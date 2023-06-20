import streamlit as sl
from PIL import Image
from io import BytesIO
import os

def main():

    sl.title("JPG,JPEG to PNG")

    data = sl.file_uploader("Please upload the JPG file")

    if data is not None:
        try:
            bytes_data = data.getvalue()

            image_data = bytes_data
            image = Image.open(BytesIO(image_data))

            img_type = image_checker(data.name)

            if img_type == "png":
                sl.write("PNG Image type has already uploaded")
            
            else:
                image_name, image_type = data.name.split('.')
                file_name = image_name + ".png"

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


def image_checker(image_name):
    if "." in image_name:
        image_name, image_type = image_name.split(".")

        image_type_list = ["jpg", "png", "jpeg", "jfif"]
        counter = 0

        for i in image_type_list:
            if i == image_type:
                return (image_type)
                #break

            else:
                counter = counter + 1
                if counter == len(image_type_list):
                    return ("invalid")
                else:
                    continue
    else:
        return("invalid")
    
main()
