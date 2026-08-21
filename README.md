# IEI_N4_C2
Clases de Backend con Django

## Creación Proyectos con Django

1. **Creación de repositorio en "https://github.com".**
    - Vinculamos el repositorio con nuestro editor de código, idealmente VSCode.
2. **Creación de Entorno (ambiente) Virtual**
    - Nos situamos en el directorio principal de nuestra aplicación.
    - Ubicados en este directorio, abrimos un terminal.
    - Ejecutamos el comando: 
    ```
    python -m venv nombre_ambiente
    ```
    - Esto crea toda la estructura de directorios necesario para nuestro proyecto y lo mantiene aislado de cualquier otro proyecto.
3. **Activación de Entorno Virtual**
    - Mediante el terminal, nos ubicamos dentro del directorio del ambiente virtual. Podemos movernos con cd y cd..
    - Estando en el directorio de nuestro ambiente virtual, ingresaremos al sub-directorio Scripts.
    - Una vez dentro de este directorio, ejecutaremos el archivo Activate, medainte el siguiente comando:
    ```
    .\Activate
    ```
    - Si la ejecución del script está bloqueada por permisos de ejecución del terminal, usaremos el siguiente comando para autorizarlo:
    ```
    Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned
    ```
    - Después de este comando, deberíamos poder ejecutar la activación del ambiente.
    - Cuando hayamos terminado de trabajar o necesitamos desactivar el ambiente, ejecutaremos en terminal el comando:
    ```
    deactivate
    ```

3. **Actualización PIP**
    - Al haber creado un nuevo proyecto, nop tenemos la seguridad de tener PIP en la última versión, por lo que lo actualizaremos.
    - Mediante terminal, ejecutamos el siguiente comando:
    ```
    python.exe -m pip install --upgrade pip
    ```

4. **Instalación de Django**
    - Django depende de la última versión de PIP, por lo que tuvimos que actualizarlo.
    - Mediante el terminal, nos ubicamos en el directorio principal del proyecto.
    - Ahora instalaremos el entorno de trabajo de Django, ejecutando el siguiente comando en el terminal:
    ```
    pip install django
    ```

5. **Creamos Nuestro Proyecto Django**

    - Crearemos la estructura de directorios de Django.
    - Mediante terminal, nos ubicamos en la carpeta raíz de nuestro proyecto.
    - Estando en esta ubicación, ejecutaremos el siguiente comando en el terminal:
    ```
    django-admin startproject proyecto_django .
    ```