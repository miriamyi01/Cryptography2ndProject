# 🔐 Second Cryptography Project

## 🕵️‍♂️ POST-QUANTUM CRYPTOGRAPHY PROJECT

Este proyecto explora la frontera de la criptografía post-cuántica, centrándose en esquemas diseñados para resistir las capacidades computacionales de los ordenadores cuánticos. Las áreas clave de interés incluyen:

- **ML-KEM Scheme** 🧩
- **ML-DSA Signature Scheme** ✍️
- **SLH-DSA Signature Scheme** 📜

&nbsp;
## Configuración del Entorno para Proyectos de Criptografía Post-Cuántica

### Instalación de Herramientas Necesarias

1. **Instalar Docker Desktop**: Descarga e instala la aplicación de escritorio Docker desde [este enlace](https://www.docker.com/products/docker-desktop/).

2. **Instalar el Kernel de Linux**:
    - Sigue los pasos del 4 al 5 del artículo [Manual installation steps for older versions of WSL](https://learn.microsoft.com/en-us/windows/wsl/install-manual) para instalar el kernel de Linux.

### Configuración de Windows Subsystem for Linux (WSL)

#### Paso 1 - Habilitar Windows Subsystem for Linux

- Abre PowerShell como Administrador.
- Ejecuta el siguiente comando:

  ```powershell
  dism.exe /online /enable-feature /featurename:Microsoft-Windows-Subsystem-Linux /all /norestart
  ```

#### Paso 2 - Verificar los Requisitos para Ejecutar WSL 2

- Asegúrate de tener los requisitos mínimos de Windows 10.
- Verifica la versión y el número de compilación con `winver`.
- Habilita la característica de la Plataforma de Máquina Virtual con PowerShell:

  ```powershell
  dism.exe /online /enable-feature /featurename:VirtualMachinePlatform /all /norestart
  ```

#### Paso 3 - Descargar el Paquete de Actualización del Kernel de Linux

- Descarga el paquete de actualización del kernel de Linux adecuado para tu máquina:
  - [Paquete de actualización del kernel de Linux para máquinas x64](https://wslstorestorage.blob.core.windows.net/wslblob/wsl_update_x64.msi)

#### Paso 4 - Configurar WSL 2 como Versión Predeterminada
- Abre PowerShell y ejecuta el siguiente comando:
  ```powershell
  wsl --set-default-version 2
  ```

#### Paso 5 - Instalar la Distribución de Linux de tu Preferencia

- Abre la Microsoft Store y selecciona tu distribución de Linux favorita.

  ##### Vista de Distribuciones de Linux en la Microsoft Store:

  - [Ubuntu 18.04 LTS](https://www.microsoft.com/store/apps/9N9TNGVNDL3Q)
  - [Ubuntu 20.04 LTS](https://www.microsoft.com/store/apps/9N6SVWS3RX71)
  - [Ubuntu 22.04 LTS](https://www.microsoft.com/store/apps/9PN20MSR04DW)
  - [openSUSE Leap 15.1](https://www.microsoft.com/store/apps/9NJFZK00FGKV)
  - [SUSE Linux Enterprise Server 12 SP5](https://www.microsoft.com/store/apps/9MZ0DJ7V4R0)
  - [SUSE Linux Enterprise Server 15 SP1](https://www.microsoft.com/store/apps/9NQVQDNF98Z7)
  - [Kali Linux](https://www.microsoft.com/store/apps/9PKR34TNCV07)
  - [Debian GNU/Linux](https://www.microsoft.com/store/apps/9MSVKQC78PK6)
  - [Fedora Remix for WSL](https://www.microsoft.com/store/apps/9N6GDM4K2HN1)
  - [Pengwin](https://www.microsoft.com/store/apps/9NV1GV1PXZ6P)
  - [Pengwin Enterprise](https://www.microsoft.com/store/apps/9NPXTS9K1FXP)
  - [Alpine WSL](https://www.microsoft.com/store/apps/9P804CRF0395)
  - [Raft (Free Trial)](https://www.microsoft.com/store/apps/9NSL5B1C5B8G)
  - [Alma Linux](https://www.microsoft.com/store/apps/9N3T9C7MSXG4)
  
  Desde la página de la distribución, selecciona "Obtener" (Get).
  
  La primera vez que lances una nueva distribución de Linux instalada, se abrirá una ventana de consola y se te pedirá que esperes un minuto o dos para que los archivos se descompriman y se almacenen en tu PC. Todos los futuros lanzamientos deberían tomar menos de un segundo.
  
  Luego, necesitarás crear una cuenta de usuario y una contraseña para tu nueva distribución de Linux.
  
### Instalación de liboqs en Docker
1. **Crear el Dockerfile**
  Abre un editor de texto (como `vi`) y crea un archivo llamado `Dockerfile`. Usa el comando `:wq` para guardar y salir.

    ```bash
    vi Dockerfile
    ```

    Agrega el siguiente contenido al Dockerfile:

    ```Dockerfile
    FROM ubuntu:latest

    # Instalar dependencias
    RUN apt-get -y update && \
        apt-get install -y build-essential git cmake libssl-dev golang

    # Obtener liboqs
    RUN git clone --depth 1 --branch main https://github.com/open-quantum-safe/liboqs

    # Instalar liboqs
    RUN cmake -S liboqs -B liboqs/build -DBUILD_SHARED_LIBS=ON && \
        cmake --build liboqs/build --parallel 4 && \
        cmake --build liboqs/build --target install

    # Habilitar un usuario normal
    RUN useradd -m -c "Open Quantum Safe" oqs
    USER oqs
    WORKDIR /home/oqs

    # Obtener liboqs-go
    RUN git clone --depth 1 --branch main https://github.com/open-quantum-safe/liboqs-go.git

    # Configurar liboqs-go
    ENV PKG_CONFIG_PATH=$PKG_CONFIG_PATH:/home/oqs/liboqs-go/.config
    ENV LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/usr/local/lib
    ```

2. **Construir la Imagen Docker**

    ```bash
    docker build -t oqs-go .
    ```

3. **Ejecutar la Imagen Docker y Utilizar liboqs-go**

    - Ejemplo de ejecución del programa de encapsulación de claves:

      ```bash
      docker run -it oqs-go sh -c "cd liboqs-go && go run examples/kem/kem.go"
      ```

    - Ejecutar pruebas unitarias:

      ```bash
      docker run -it oqs-go sh -c "cd liboqs-go && go test -v ./oqstests"
      ```

### Uso del Entorno Docker para Desarrollo

1. Si deseas utilizar el contenedor Docker como un entorno de desarrollo, monta tu proyecto actual en el contenedor Docker con el siguiente comando:

      ```bash
      docker run --rm -it --workdir=/app -v ${PWD}:/app oqs-go /bin/bash
      ```

2. Una vez ejecutado el comando anterior, para ejecutar programas Python, utiliza el siguiente comando:

    ```bash
    python3 ML-KEM.py
    python3 ML-DSA.py
    python3 SLH-DSA.py
    ```

   *NOTA: Asegúrate de estar en la carpeta correcta donde se encuentran los programas necesarios antes de ejecutar los comandos.*
