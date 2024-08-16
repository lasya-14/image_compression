import numpy as np
import cv2
from sklearn.cluster import KMeans
import streamlit as st
import os

import sys

sys.path.append('/Library/Frameworks/Python.framework/Versions/3.10/lib/python3.10/site-packages')

# Custom CSS to enhance the UI
st.markdown("""
    <style>
    .main {
        background-color: #6FDCE3;
    }
    .stButton button {
        background-color: #FF4E88;
        color: pink;
        border: none;
        padding: 10px 24px;
        text-align: center;
        text-decoration: underline overline;
        display: inline-block;
        font-size: 16px;
        margin: 4px 2px;
        transition-duration: 0.4s;
        cursor: pointer;
    }
    .stButton button:hover {
        background-color: pink;
        color: black;
        border: 2px solid #FF4E88;
    }
    .stSlider > div > div > div[role='slider'] {
        background-color: #FF4E88;
    }
    </style>
""", unsafe_allow_html=True)

def compress_image(image, num_clusters):
    pixels = image.reshape(-1, 3)
    kmeans = KMeans(n_clusters=num_clusters, random_state=42)
    kmeans.fit(pixels)
    compressed_pixels = kmeans.cluster_centers_[kmeans.labels_]
    compressed_pixels = np.clip(compressed_pixels.astype('uint8'), 0, 255)
    compressed_image = compressed_pixels.reshape(image.shape)
    return compressed_image

def main():
    st.title("Image Compression Using K-means Clustering")
    st.markdown("<h2 style='text-align: center; color: #E90074;'>Compress your images by reducing the number of colors</h2>", unsafe_allow_html=True)
    st.write("Upload an image and choose the number of colors to compress it.")

    uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"], key="file_uploader_main")
    num_clusters = st.slider("Number of Colors (Clusters)", min_value=1, max_value=64, value=16, key="slider_clusters_main")

    if uploaded_file is not None:
        file_bytes = np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8)
        image = cv2.imdecode(file_bytes, 1)
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

        original_size = uploaded_file.size
        compressed_image = compress_image(image, num_clusters)

        st.subheader("Original Image")
        st.image(image, use_column_width=True)
        st.write(f"Original Image Size: {original_size} bytes")

        compressed_image_bgr = cv2.cvtColor(compressed_image, cv2.COLOR_RGB2BGR)
        compressed_image_path = "compressed_image.jpg"
        cv2.imwrite(compressed_image_path, compressed_image_bgr)
        compressed_size = os.path.getsize(compressed_image_path)

        st.subheader("Compressed Image")
        st.image(compressed_image, use_column_width=True)
        st.write(f"Compressed Image Size: {compressed_size} bytes")

        compression_ratio = original_size / compressed_size
        st.write(f"Compression Ratio: {compression_ratio:.2f}")

        with open(compressed_image_path, "rb") as file:
            btn = st.download_button(
                label="Download Compressed Image",
                data=file,
                file_name="compressed_image.jpg",
                mime="image/jpg"
            )

if __name__ == "__main__":
    main()