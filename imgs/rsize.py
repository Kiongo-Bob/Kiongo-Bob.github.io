import cv2

# Read the image
image = cv2.imread('yt/imgs/work3.jpg')

# Define the new dimensions
new_width = 500
new_height = 500

# Resize the image
resized_image = cv2.resize(image, (new_width, new_height))

# Save the resized image
cv2.imwrite('./work3.jpg', resized_image)

# Display the original and resized images
cv2.imshow('Resized Image', resized_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
