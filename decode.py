from pyzbar.pyzbar import decode
from PIL import Image
import hashlib
import qrcode

def get_key(val, dict):
    for key, value in dict.items():
        if val == value:
            return key
    return "se ha alterado el bloque"

class Prod:
    def __init__(self, producto, productor, fecha_cosecha, picking):
        self.producto = producto
        self.productor = productor
        self.fecha_cosecha = fecha_cosecha
        self.picking = picking
        self.info = producto + ";" + productor + ";" + fecha_cosecha + ";" + picking

dict = {
    "Chillán - Ñuble - Chile": str(hashlib.sha256("empresa".encode()).hexdigest()),
    "picking": str(hashlib.sha256("picking".encode()).hexdigest())  
}

qr = decode(Image.open('QR.png'))

print(qr[0].data)

decoded_item = str(qr[0].data).split(";")

productor = get_key(decoded_item[1], dict)
picking = get_key(decoded_item[3], dict)

prod_item = Prod(decoded_item[0], productor, decoded_item[2], decoded_item[3])

print("Producto: " + prod_item.producto + "\n")
print("Producto: " + prod_item.productor + "\n")
print("Fecha de cosecha: " + prod_item.fecha_cosecha + "\n")


qr_code = qrcode.QRCode(
        version = 1,
        error_correction= qrcode.constants.ERROR_CORRECT_M,
        box_size=3

)

qr_code.add_data("Información del producto" + "\n Tipo: " + prod_item.producto + "\n Lugar: " 
                 + prod_item.productor + "\n Fecha Elab. " + prod_item.fecha_cosecha + 
                 "\n código picking: " + prod_item.picking)

embedded_data = (prod_item.producto + ";" + prod_item.productor + ";" + prod_item.fecha_cosecha + ";" + 
                 prod_item.picking)

print("Embedding QR: \n" + embedded_data + "\n")

qr_code.make(fit=True)
img = qr_code.make_image(fill_color=(0,0,0), back_color=(255,255,255))
img.save("QRdecode.png")
