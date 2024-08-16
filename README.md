Image Compression App Using K-Means Clustering
This Streamlit app allows users to compress images by reducing the number of colors using the K-means clustering algorithm. The app provides an easy-to-use interface where users can upload an image, choose the desired number of colors (clusters), and download the compressed image. This technique effectively reduces the file size and simplifies the image by limiting the color palette.
Features
Image Upload: Users can upload any image (JPEG, PNG, etc.) from their device.
Color Reduction: Choose the number of colors to reduce the image to, using the K-means clustering algorithm.
Preview: View the original and compressed images side by side for comparison.
Download Option: Easily download the compressed image with a single click.
How It Works
1.Upload an Image: Use the upload button to select an image file from your local device.
2.Choose Number of Colors: Select the desired number of colors (clusters). Fewer colors result in more compression.
3.K-Means Clustering: The app applies the K-means clustering algorithm to group pixels into clusters and replaces each pixel's color with the centroid of its respective cluster.
4.Preview and Download: Preview the original and compressed images. If satisfied, download the compressed image.
Usage
1.Clone the repository
