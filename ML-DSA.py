import oqs  # Importa la biblioteca Open Quantum Safe (OQS) para operaciones criptográficas
import time  # Importa el módulo time para medir el tiempo de ejecución
import matplotlib.pyplot as plt  # Importa la biblioteca matplotlib para graficar los resultados

def realizar_firma_y_verificacion():
    """
    Simula un proceso sencillo de firma y verificación de un mensaje usando la biblioteca OQS.

    Esta función genera una firma para un mensaje dado utilizando el algoritmo de firma Dilithium3,
    y luego verifica la firma usando el mismo algoritmo y la clave pública del firmante.

    Retorna:
        None
    """

    # Simula un mensaje simple en lugar de leerlo desde un archivo
    mensaje_claro = "Este es un mensaje de prueba."  # Mensaje de prueba
    mensaje = mensaje_claro.encode()  # Convierte el mensaje a bytes

    # Crea instancias de firma tanto para el firmante como para el verificador
    sigalg = "Dilithium3"  # Algoritmo de firma post-cuántica Dilithium3
    with oqs.Signature(sigalg) as firmante:  # Crea una instancia del firmante
        with oqs.Signature(sigalg) as verificador:  # Crea una instancia del verificador
            # El firmante genera su par de claves
            clave_publica_firmante = firmante.generate_keypair()  # Genera el par de claves del firmante

            # El firmante firma el mensaje
            inicio_firma = time.time()  # Registra el tiempo de inicio de la firma
            firma = firmante.sign(mensaje)  # Firma el mensaje
            fin_firma = time.time()  # Registra el tiempo de finalización de la firma

            # El verificador verifica la firma utilizando el mensaje, la firma y la clave pública del firmante
            inicio_verificacion = time.time()  # Registra el tiempo de inicio de la verificación
            es_valida = verificador.verify(mensaje, firma, clave_publica_firmante)  # Verifica la firma
            fin_verificacion = time.time()  # Registra el tiempo de finalización de la verificación

            # Calcula los tiempos
            tiempo_firma = (fin_firma - inicio_firma) * 1000  # Convertido a milisegundos
            tiempo_verificacion = (fin_verificacion - inicio_verificacion) * 1000  # Convertido a milisegundos
            tiempo_total = tiempo_firma + tiempo_verificacion  # Calcula el tiempo total

            # Prepara los datos para el gráfico
            tareas = ['Firmado', 'Verificación']  # Define las etiquetas para las barras del gráfico
            tiempos = [tiempo_firma, tiempo_verificacion]  # Define los tiempos para las barras del gráfico

            # Crea el gráfico de barras
            plt.bar(tareas, tiempos, color=['blue', 'green'])  # Crea un gráfico de barras con las etiquetas y tiempos dados
            plt.xlabel('Tarea')  # Etiqueta del eje x
            plt.ylabel('Tiempo (ms)')  # Etiqueta del eje y
            plt.title('Rendimiento de Firmado y Verificación')  # Título del gráfico
            # Guarda el gráfico en un archivo PNG antes de mostrarlo
            plt.savefig('ML-DSA.png')
            plt.show()  # Muestra el gráfico

            # Imprime resultados
            print(f"\nEl tiempo para la generación de la firma es: {tiempo_firma} [ms]")  # Imprime el tiempo de firma
            print(f"\nEl tiempo para la verificación de la firma es: {tiempo_verificacion} [ms]")  # Imprime el tiempo de verificación
            print(f"\nEl tiempo total: firmado + verificación de firma es: {tiempo_total} [ms]")  # Imprime el tiempo total

            # Muestra la firma y determina si es válida o no
            print(f"\nFirma: {firma}")  # Imprime la firma generada
            print(f"\n¿La firma es válida?\n{es_valida}")  # Imprime si la firma es válida o no

# Ejecuta la función para realizar la firma y verificación
realizar_firma_y_verificacion()