# 🔐 Second Cryptography Project

## 🕵️‍♂️ POST-QUANTUM CRYPTOGRAPHY PROJECT

Este proyecto explora la frontera de la criptografía post-cuántica, centrándose en esquemas diseñados para resistir las capacidades computacionales de los ordenadores cuánticos. Las áreas clave de interés incluyen:

- **ML-KEM Scheme** 🧩
- **ML-DSA Signature Scheme** ✍️
- **SLH-DSA Signature Scheme** 📜

&nbsp;
## Configuración del Entorno la ejecución del proyecto en Windows
### Creación y activación del entorno virtual
1. Abre una consola Powershell como Administrador e introduce los siguientes comandos
   
    ```powershell
    python -m venv venv
    venv\Scripts\activate.ps1
    python -m ensurepip --upgrade
    ```

2. Clona el repositorio dentro del venv y reúne los requerimientos de pip
   
    ```powershell
    cd .\venv\
    git clone --depth=1 https://github.com/miriamyi01/Cryptography2ndProject Cryptography2ndProject
    cd .\Cryptography2ndProject\
    pip install -r requirements.txt
    ```

4. Clona el repositorio de la biblioteca de bindings liboqs-python y agrégalo a pip
   
    ```powershell
    cd ..
    git clone --depth=1 https://github.com/open-quantum-safe/liboqs-python liboqs-python
    cd liboqs-python
    pip install .
    ```

6. Ejecuta los ejemplos de la librería para que se instale automáticamente la biblioteca necesaria en C
   
    ```powershell
    python examples/kem.py
    ```
