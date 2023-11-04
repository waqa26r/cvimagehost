import streamlit as st
import cv2
import numpy as np
from PIL import Image

# Translation
def translate_image(image, x, y):
    rows, cols = image.shape[:2]
    M = np.float32([[1, 0, x], [0, 1, y]])
    translated_image = cv2.warpAffine(image, M, (cols, rows))
    return translated_image

# Rotation
def rotate_image(image, angle):
    rows, cols = image.shape[:2]
    M = cv2.getRotationMatrix2D((cols / 2, rows / 2), angle, 1)
    rotated_image = cv2.warpAffine(image, M, (cols, rows))
    return rotated_image

# Scaling
def scale_image(image, scale_factor):
    scaled_image = cv2.resize(image, None, fx=scale_factor, fy=scale_factor, interpolation=cv2.INTER_LINEAR)
    return scaled_image

# Shearing
def shear_image(image, shear_factor):
    rows, cols = image.shape[:2]
    M = np.float32([[1, shear_factor, 0], [0, 1, 0]])
    sheared_image = cv2.warpAffine(image, M, (cols, rows))
    return sheared_image

st.title('Image Transformation App')

uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "png"])

if uploaded_file is not None:
    file_bytes = np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8)
    image = cv2.imdecode(file_bytes, cv2.IMREAD_COLOR)

    st.image(image, caption='Uploaded Image', use_column_width=True)

    transformation = st.sidebar.selectbox(
        'Choose Transformation',
        ('Translation', 'Rotation', 'Scaling', 'Shearing')
    )

    if transformation == 'Translation':
        x = st.sidebar.slider('X', -100, 100, 0)
        y = st.sidebar.slider('Y', -100, 100, 0)
        transformed_image = translate_image(image, x, y)
        st.image(transformed_image, caption='Translated Image', use_column_width=True)

    elif transformation == 'Rotation':
        angle = st.sidebar.slider('Angle', -180, 180, 0)
        transformed_image = rotate_image(image, angle)
        st.image(transformed_image, caption='Rotated Image', use_column_width=True)

    elif transformation == 'Scaling':
        scale_factor = st.sidebar.slider('Scale Factor', 0.1, 3.0, 1.0)
        transformed_image = scale_image(image, scale_factor)
        st.image(transformed_image, caption='Scaled Image', use_column_width=True)

    elif transformation == 'Shearing':
        shear_factor = st.sidebar.slider('Shear Factor', -1.0, 1.0, 0.0)
        transformed_image = shear_image(image, shear_factor)
        st.image(transformed_image, caption='Sheared Image', use_column_width=True)
