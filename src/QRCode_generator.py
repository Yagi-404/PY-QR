import qrcode

class QRCode_Generator:
    def __init__(self, data, filename):
        self.data = data
        self.filename = filename

    def generate_QR_code(self):
        img = qrcode.make(self.data)

        # giving self.name to the name of the file
        
        img.save(f"{self.filename}.qr.png")
