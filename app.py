#%%writefile app3.py  
import streamlit as st 
import cv2
import pytesseract 
from PIL import Image  # python imaging library to open the images in streamlit because streamlit doesn't images to display directly 
pytesseract.pytesseract.tesseract_cmd = '/app/.apt/usr/bin/tesseract'
st.set_option('deprecation.showfileUploaderEncoding',False)            #this line ignores any warning that comes up 
st.title("OCR - Optical Character Recognition")                        #title for the web app
st.text("Upload the image")                                            #asking user to upload the image 

uploaded_file = st.sidebar.file_uploader("Choose an image ", type = ["jpg","jpeg","png"])  #create a file uploader option in the sidebar 
if uploaded_file is not None:   #only if a file is uploaded, then perform the below operations 
  img = Image.open(uploaded_file)   #open the uploaded file 
  st.image(img, caption='Uploaded Image', use_column_width=True) #display the image file and use the actual image width 
  st.write("")  #prints a blank space 

  if st.button('PREDICT'):  #creates a button called predict and gives the ocr output below 
    st.write("Result:")     
    info = pytesseract.image_to_string(img)  #performs ocr 
    st.write(info)                   #prints the result 
