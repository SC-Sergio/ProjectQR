import hashlib
from datetime import datetime

class ProdBlock:
    def __init__(self, info, hash_previo, transaccion):
        self.info = info
        self.transaccion = transaccion
        self.hash_previo = hash_previo
        string_to_hash = "".join(transaccion) + hash_previo
        self.block_hash = hashlib.sha256(string_to_hash.encode()).hexdigest()


class picking_class:
    def __init__(self, picking, fecha_picking):
        self.piking = picking
        self.fecha_picking = fecha_picking
        self.info = picking + ";" + fecha_picking


picking = (hashlib.sha256("packing".encode()).hexdigest())
fecha_picking = str(datetime.now())

item_picking = picking_class(picking, fecha_picking)

print("Picking:\n", item_picking.info)

embedded_data_picking = (item_picking.info)