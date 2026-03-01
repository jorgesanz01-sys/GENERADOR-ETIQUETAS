# main.py actualizado
import impresion
import log_logistica # Importamos el nuevo módulo de registro

print("--- SISTEMA DE ETIQUETADO GRB ---")
ref = input("Escanee Referencia: ")
lote = input("Introduzca Lote: ")

resultado = impresion.preparar_etiqueta(ref, lote)

if resultado["OK"]:
    datos = resultado["DATOS"]
    print(f"\n✅ LISTO PARA IMPRIMIR EN {datos['CLIENTE']}:")
    print(f"Producto: {datos['DESC']}")
    
    # REGISTRAMOS LA OPERACIÓN
    log_logistica.registrar_impresion(ref, datos['DESC'], lote)
else:
    print(f"\n❌ ERROR: {resultado['MSG']}")