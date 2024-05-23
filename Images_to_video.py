import cv2
import os

# Path to the directory containing images
input_folder = "D:\\IndeVFX\\pythonProject\\Python_scripts_for_tasks\\Plates"

# Get a list of image file names in the directory
image_files = [f for f in os.listdir(input_folder) if f.endswith('.png')]

# Sort image files to ensure they are processed in order
image_files.sort()

# Get the dimensions of the first image (assumes all images have the same dimensions)
first_image_path = os.path.join(input_folder, image_files[0])
first_image = cv2.imread(first_image_path)
height, width, layers = first_image.shape

# Define the output video filename and path
output_video = 'output_video.avi'
output_path = os.path.join("D:\\IndeVFX\\pythonProject\\Python_scripts_for_tasks\\Plates\\", output_video)  # Change 'output_folder' to your desired path


# Initialize the VideoWriter
fourcc = cv2.VideoWriter_fourcc(*'XVID')  # Specify the codec
video = cv2.VideoWriter(output_path, fourcc, 24.0, (width, height))  # 24.0 frames per second

# Loop through each image and write it to the video
for image_file in image_files:
    image_path = os.path.join(input_folder, image_file)
    frame = cv2.imread(image_path)
    video.write(frame)

# Release the VideoWriter
video.release()

print(f"Video saved as '{output_video}'")
