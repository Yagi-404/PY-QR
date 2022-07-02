import QRCode_generator

def main():
    url = input("Enter the URL: ")
    filename = input("Enter the name of the file: ")

    QR = QRCode_generator.QRCode_Generator(url, filename)
    QR.generate_QR_code()

if __name__ == '__main__':
    main()