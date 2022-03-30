import QRCode_generator

def main():
    QR_Generator = QRCode_generator.QRCode_Generator('https://yagi-404.github.io/', 'My Website')
    QR_Generator.generate_QR_code()

    QR_Generator = QRCode_generator.QRCode_Generator('https://lapcoder.github.io/4U-Programming-language/', '4U Programming Language')
    QR_Generator.generate_QR_code()

if __name__ == '__main__':
    main()