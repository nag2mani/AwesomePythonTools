# pip install requests Pillow

import requests
from PIL import Image
from io import BytesIO

# Define the base URL and the range of the last digit
base_url = "https://www.bekushal.com/data/abhyas/artificial_neural_networks/mcq"
start_digit = 20
end_digit = 30

# Loop through the range of the last digit
for i in range(start_digit, end_digit + 1):
    # Construct the URL by appending the current digit to the base URL
    url = f"{base_url}{i}.png"
    
    # Send a GET request to the URL
    response = requests.get(url)
    
    # Check if the request was successful
    if response.status_code == 200:
        # Try to open the response content as an image
        try:
            image = Image.open(BytesIO(response.content))
            # Save the image to a file
            image.save(f"image_{i}.png")
            print(f"Image {i} downloaded successfully.")
        except IOError:
            print(f"Unable to download image {i}.")
    else:
        print(f"Failed to download image {i}. Status code: {response.status_code}")

print("All images downloaded.")






