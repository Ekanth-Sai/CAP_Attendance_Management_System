import streamlit as st
from PIL import Image
import io
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
from firebase_admin import storage

if not firebase_admin._apps:
    cred = credentials.Certificate("serviceAccountKey.json")
    firebase_admin.initialize_app(cred, {
    'databaseURL': "https://attendance-management-sy-127ee-default-rtdb.asia-southeast1.firebasedatabase.app/",
    'storageBucket': "attendance-management-sy-127ee.appspot.com"
    })

def conv_png(image):
    img = Image.open(image)
    img_png = img.convert("RGB")
    img_stream = io.BytesIO()
    img_png.save(img_stream, format="PNG")
    img_stream.seek(0)
    return img_stream

def resize(image, size=(216, 216)):
    resized_image = image.resize(size)
    return resized_image

def add_db(name, branch, GPA, DoJ, year, image_url):
    ref = db.reference("Students")
    new_students_ref = ref.push()
    new_students_ref.set({
        "name": name, 
        "branch": branch,
        "GPA": GPA,
        "DoJ": DoJ,
        "Year": year,
        "image_url": image_url
    })

st.title("Enter the student details")
name = st.text_input("Enter the name of the student: ")
branch = st.selectbox(
    "Choose branch:",
    ("CSE", "CSE-AIML", "CSE-DS", "CSE-BS", "IT", "ECE", "EEE", "ME", "CE")
)
GPA = st.text_input("Enter the GPA: ")
DoJ = st.date_input("Enter the date of join: ")
year = st.radio("Select the year:", ("1", "2", "3", "4"))

st.title("Resizing and conversion")
uploaded_image = st.file_uploader("Upload image", type = ["jpg", "jpeg", "png"])
#debug
image = Image.open(uploaded_image)
st.write("Image Format:", image.format)
#st.write("flag trigger")


try:

    st.image(uploaded_image, caption = "Original image", use_column_width = True)   
    resized_image = resize(uploaded_image)
    png_stream = conv_png(uploaded_image)
    st.image(png_stream, caption = "Converted to png and resized", use_column_width = True)

    bucket = storage.bucket()
    blob = bucket.blob(f"Images/{name}.png")
    blob.upload_from_string(png_stream.getvalue(), content_type = "Image/png")
    image_url = blob.public_url

    add_db(name, branch, GPA, DoJ, year, image_url)
    st.success("Details have been succesfully added")

except:
    st.warning("Unsuccessful")
