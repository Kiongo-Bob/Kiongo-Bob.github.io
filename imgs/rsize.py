import cv2

# Read the image
image = cv2.imread('/home/kiongobob/Project Based Learning/Kiongo-Bob.github.io/imgs/Me1.jpg')

# Define the new dimensions
new_width = 600
new_height = 800

# Resize the image
resized_image = cv2.resize(image, (new_width, new_height))

# Save the resized image
cv2.imwrite('/home/kiongobob/Project Based Learning/Kiongo-Bob.github.io/imgs/Me2.jpg', resized_image)

# Display the original and resized images
cv2.imshow('Resized Image', resized_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
