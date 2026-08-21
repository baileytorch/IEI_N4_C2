# IEI_N4_C2
Clases de Backend con Django

<<<<<<< HEAD
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
=======
<H3>Creación Proyectos con Django</H3>
<hr>
<ol>
    <li>Creación de repositorio en <a href="https://github.com">GITHUB</a>.</li>
    <li>Vinculamos el repositorio con nuestro editor de código, idealmente VSCode.</li>
    <li>Creación de Entorno (ambiente) Virtual</li>
        <ol>
            <li>Nos situamos en el directorio principal de nuestra aplicación.</li>
            <li>Ubicados en este directorio, abrimos un terminal.</li>
            <li>Ejecutamos el comando: <code>python -m venv nombre_ambiente</code></li>
            <li>Esto crea toda la estructura de directorios necesario para nuestro proyecto y lo mantiene aislado de cualquier otro proyecto.</li>
        </ol>
    <li>Activación de Entorno Virtual</li>
        <ol>
            <li>Mediante el terminal, nos ubicamos dentro del directorio del ambiente virtual</li>
        </ol>
</ol>
>>>>>>> edc18c5b2cefaa80ce54164156134ab6a1fe47c8
