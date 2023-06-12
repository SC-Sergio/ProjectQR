import hashlib
import qrcode
from datetime import datetime

class ProdBlock:
    def __init__(self, info, hash_previo, transaccion):
        self.info = info
        self.transaccion = transaccion
        self.hash_previo = hash_previo
        string_to_hash = "".join(transaccion) + hash_previo
        self.block_hash = hashlib.sha256(string_to_hash.encode()).hexdigest()

class Prod:
    def __init__(self, producto, productor, fecha_cosecha):
        self.productor = producto
        self.producto = productor
        self.fecha_cosecha = fecha_cosecha
        self.info = producto + ";" + productor + ";" + fecha_cosecha

productor_id = hashlib.sha256("empresa".encode()).hexdigest()
first_item = Prod('Arandano', str(productor_id), str(datetime.now()))

print("Información de la cosecha:\n")

next_block1 = hashlib.sha256("primer_bloque".encode()).hexdigest()
genesis_block = ProdBlock(first_item.info, first_item.info, [str(next_block1)])
print("Item info" + genesis_block.info + "\n")
print("Primer hash")
print(genesis_block.block_hash + "\n\n")

next_block2 = hashlib.sha256("segundo_bloque".encode()).hexdigest()
segundo_block = ProdBlock(first_item.info, first_item.info, [str(next_block2)])
print("Item info" + segundo_block.info + "\n")
print("Primer hash")
print(segundo_block.block_hash + "\n\n")

qr_code = qrcode.QRCode(
            version = 4,
            error_correction = qrcode.constants.ERROR_CORRECT_H,
            box_size= 6
)

qr_code.add_data(segundo_block.info + ";" + segundo_block.block_hash)
embedded_data = segundo_block.info + ";" + segundo_block.block_hash

print('Embedding QR \n' + embedded_data + "\n")

qr_code.make(fit=True)
img = qr_code.make_image(fill_color=(0,0,0,0), back_color=(255,255,255))
img.save('QR.png')