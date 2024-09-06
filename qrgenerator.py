# Import the QR code library to allow to actually do this
import qrcode
# Import os so we can access the file system
import os

# Define the URL you want to use to create the QR code
URL = "https://github.com/JayLovesProgramming"

# Create the QR code instance
qr = qrcode.QRCode(
    version = 1,
    error_correction = qrcode.constants.ERROR_CORRECT_L,
    box_size = 10,
    border = 4
)

# Add the URL to the code
qr.add_data(URL)
qr.make(fit = True)

# Create an image from the QR code instance
img = qr.make_image(fill = "black", back_color = "white")

def get_unique_fileame(base_name, extension):
    counter = 1
    new_name = f"{base_name}.{extension}"
    while os.path.exists(new_name):
        new_name = f"{base_name}_{counter}.{extension}"
        counter += 1
    return new_name

# Define the base name and extension
base_name = "qr"
extension = "png"

# Generate a unique filename
filename = get_unique_fileame(base_name, extension)

# Save the image
img.save(filename)

# Prints/logs after qr code image has been saved
print(f"QR Code generated and saved as '{filename}'")