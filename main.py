#https://discuss.streamlit.io/t/how-streamlit-stores-media/13881/2

import streamlit as st
from streamlit.elements.image import image_to_url, MAXIMUM_CONTENT_WIDTH
from PIL import Image
import os.path

def main():
  img = st.file_uploader("upload image", type=["jpg", "png", "jpeg"])
  st.write(img)

  if img:
    test = Image.open(img)
    width, height = test.size  # width is needed for image_to_url()
    if width > MAXIMUM_CONTENT_WIDTH:
      width = MAXIMUM_CONTENT_WIDTH  # width is capped at 2*730 https://github.com/streamlit/streamlit/blob/949d97f37bde0948b57a0f4cab7644b61166f98d/lib/streamlit/elements/image.py#L39
    st.write('Uploaded Image')
    st.image(img)

    img_url = image_to_url(
      image=img,
      width=width,
      clamp=False,
      channels="RGB",
      output_format=img.type,
      image_id=img.id,  # each uploaded file has a file.id
      )
  
    st.write(img_url)

    #1st example as a file uploader? feed filedata to csv??

    #saves image file to directory
    with open(os.path.join("IMG",img.name),"wb") as f: 
        f.write(img.getbuffer())    
  

    #img2 = "IMGDIR/test.jpg"
    #st.write('Local Image')
    #st.image(img2)
  
if __name__ == "__main__":
    main()  
