import qrcode

# Function to generate QR code from input data
def generate_qr_code(data):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)

    # Create an image from the QR Code instance
    img = qr.make_image(fill_color="black", back_color="white")

    # Save the image to a file (e.g., qrcode.png)
    img.save("qrcode.png")

if __name__ == "__main__":
    # Example data
    data = {
        "name": "Javier",
        "id": "12345",
        "job": "Gerente",
        "date": "2024-01-20",
        "uid": "98765"
    }

    # Generate QR code from the example data
    generate_qr_code(str(data))