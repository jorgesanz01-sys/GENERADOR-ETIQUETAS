# impresion.py
from config import DB_PRODUCTOS # Importamos las constantes del otro fichero [cite: 478]

def obtener_etiqueta(referencia, lote):
    # Verificamos si la referencia existe en nuestro diccionario [cite: 1879]
    if referencia in DB_PRODUCTOS:
        datos = DB_PRODUCTOS[referencia]
        # Devolvemos un diccionario con la combinación final [cite: 1830, 2097]
        return {
            "descripcion": datos["desc"],
            "lote": lote,
            "codigo": datos["ean"]
        }
    return None