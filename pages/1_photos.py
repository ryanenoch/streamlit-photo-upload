import streamlit as st
from PIL import Image
from streamlit.elements.image import image_to_url, MAXIMUM_CONTENT_WIDTH


st.write('Local image')

img = Image.open('./IMG/doge.jpeg')
st.image(img,width=400)

st.write(img)

width, height = img.size  # width is needed for image_to_url()
if width > MAXIMUM_CONTENT_WIDTH:
    width = MAXIMUM_CONTENT_WIDTH 

img_url = image_to_url(
    image=img,
    width=width,
    clamp=False,
    channels="RGB",
    output_format=img.type,
    image_id=img.id,  # each uploaded file has a file.id
  )
  
st.write(img_url)