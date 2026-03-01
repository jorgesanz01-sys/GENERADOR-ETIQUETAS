# log_logistica.py
from datetime import datetime

def registrar_impresion(referencia, descripcion, lote):
    """Guarda un registro de cada etiqueta generada en un archivo de texto."""
    fecha_actual = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    # Creamos la línea del log
    linea_registro = f"[{fecha_actual}] REF: {referencia} | DESC: {descripcion} | LOTE: {lote}\n"
    
    # Abrimos el archivo en modo 'append' (a) para añadir sin borrar lo anterior
    with open("historial_etiquetas.txt", "a", encoding="utf-8") as archivo:
        archivo.write(linea_registro)
    
    print("📝 Registro guardado en historial_etiquetas.txt")