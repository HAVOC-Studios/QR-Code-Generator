import qrcode # Import the qr code library to allow to actually do this

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

# Save the image
img.save("qrcode.png")

# Prints/logs after qr code image has been saved
print("QR Code generated and saved as 'qrcode.png'")