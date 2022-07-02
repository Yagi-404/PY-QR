import qrcode

class QRCode_Generator:
    def __init__(self, url, filename):
        self.url = url
        self.filename = filename

    def generate_QR_code(self):
        img = qrcode.make(self.url)

        # giving self.name to the name of the file
        
        img.save(f"{self.filename}.qr.png")
