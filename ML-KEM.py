import time  # Importa el módulo time para medir el tiempo de ejecución
import matplotlib.pyplot as plt  # Importa la biblioteca matplotlib para graficar los resultados
import oqs  # Importa la biblioteca Open Quantum Safe (OQS) para operaciones criptográficas

def perform_key_encapsulation():
    """
    Realiza el encapsulamiento y desencapsulamiento de un mensaje utilizando el algoritmo de criptografía post-cuántica Kyber768.
    Mide el tiempo de encapsulamiento y desencapsulamiento, y muestra los resultados en un gráfico de barras.
    Compara los secretos compartidos del remitente y el destinatario para verificar si coinciden.
    """

    # Selecciona el mecanismo de KEM "Kyber768" y crea instancias para el remitente y el destinatario
    kemalg = "Kyber768"  # Algoritmo de criptografía post-cuántica Kyber768
    with oqs.KeyEncapsulation(kemalg) as sender:  # Crea una instancia del remitente
        with oqs.KeyEncapsulation(kemalg) as receiver:  # Crea una instancia del destinatario

            # El remitente genera su par de claves
            public_key_sender = sender.generate_keypair()  # Genera el par de claves del remitente
            
            # El destinatario encapsula su mensaje utilizando la clave pública del remitente
            inicio_destinatario = time.time()  # Registra el tiempo de inicio de encapsulamiento
            encrypted_message, shared_secret_receiver = receiver.encap_secret(public_key_sender)  # Encapsula el mensaje del destinatario
            fin_destinatario = time.time()  # Registra el tiempo de finalización de encapsulamiento

            # El remitente desencapsula el mensaje cifrado del destinatario para obtener el secreto compartido
            inicio_remitente = time.time()  # Registra el tiempo de inicio de desencapsulamiento
            shared_secret_sender = sender.decap_secret(encrypted_message)  # Desencapsula el mensaje cifrado del destinatario
            fin_remitente = time.time()  # Registra el tiempo de finalización de desencapsulamiento

            # Calcula los tiempos
            tiempo_encapsulamiento = (fin_destinatario - inicio_destinatario) * 1000  # Calcula el tiempo de encapsulamiento en milisegundos
            tiempo_desencapsulamiento = (fin_remitente - inicio_remitente) * 1000  # Calcula el tiempo de desencapsulamiento en milisegundos
            tiempo_total = tiempo_encapsulamiento + tiempo_desencapsulamiento  # Calcula el tiempo total

            # Prepara los datos para el gráfico
            tareas = ['Encapsulamiento', 'Desencapsulamiento']  # Define las etiquetas para las barras del gráfico
            tiempos = [tiempo_encapsulamiento, tiempo_desencapsulamiento]  # Define los tiempos para las barras del gráfico

            # Crea el gráfico de barras
            plt.bar(tareas, tiempos, color=['blue', 'green'])  # Crea un gráfico de barras con las etiquetas y tiempos dados
            plt.xlabel('Tarea')  # Etiqueta del eje x
            plt.ylabel('Tiempo (ms)')  # Etiqueta del eje y
            plt.title('Tiempo de Encapsulamiento y Desencapsulamiento')  # Título del gráfico
            plt.show()  # Muestra el gráfico

            # Imprime resultados
            print(f"\nTiempo de encapsulamiento del mensaje del destinatario con la clave del remitente: {tiempo_encapsulamiento} [ms]")  # Imprime el tiempo de encapsulamiento
            print(f"\nTiempo de desencapsulamiento del mensaje del destinatario utilizando la clave del remitente: {tiempo_desencapsulamiento} [ms]")  # Imprime el tiempo de desencapsulamiento
            print(f"\nTiempo total: encapsulamiento + desencapsulamiento = {tiempo_total} [ms]")  # Imprime el tiempo total

            # Muestra los secretos compartidos y confirma que coinciden
            print(f"\nSecreto compartido del remitente: {shared_secret_sender}")  # Imprime el secreto compartido del remitente
            print(f"Secreto compartido del destinatario: {shared_secret_receiver}")  # Imprime el secreto compartido del destinatario
            if shared_secret_sender == shared_secret_receiver:  # Verifica si los secretos compartidos coinciden
                print("Los secretos compartidos coinciden.")  # Imprime si los secretos compartidos coinciden
            else:
                print("Los secretos compartidos no coinciden.")  # Imprime si los secretos compartidos no coinciden

perform_key_encapsulation()  # Llama a la función perform_key_encapsulation() para realizar el encapsulamiento y desencapsulamiento de un mensaje