import pyqrcode

def generate_qr():
    link = "number: 0246557859"
    url = pyqrcode.create(link)
    url.png('mine.png', scale=6)
    print("printing qr code")
    print(url.terminal())

if __name__ == '__main__':
    generate_qr()