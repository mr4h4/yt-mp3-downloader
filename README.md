# YouTube to MP3 Converter
Un sencillo script que descarga videos de YouTube y los convierte a formato `.mp3` usando `yt-dlp` y `ffmpeg`. Este repositorio incluye tanto el código fuente de Python como una versión compilada para Windows.

---

### 💻 Cómo usarlo

#### **Opción 1: Usar la versión compilada (.exe)**

Esta es la forma más fácil de usar el programa. No necesitas instalar nada.

1.  Descarga el archivo `ytmp3.exe` y `links.txt` de este repositorio.
2.  Coloca ambos archivos en la misma carpeta. **No cambies el nombre de `links.txt`**.
3.  Abre el archivo `links.txt` y pega las URL de los videos de YouTube que quieras descargar, una URL por línea.
4.  Haz doble clic en `ytmp3.exe` para ejecutar el programa.
5.  El programa comenzará a descargar y convertir los videos. Las canciones se guardarán en la carpeta `/music`.

---

#### **Opción 2: Usar el script de Python (.py)**

Si prefieres utilizar la versión sin compilar, necesitarás tener Python y las librerías necesarias instaladas.

1.  Asegúrate de tener Python instalado en tu sistema.
2.  Instala `yt-dlp` ejecutando el siguiente comando en tu terminal:
    ```bash
    pip install yt-dlp
    ```
3.  El programa usa `ffmpeg`, que ya está incluido en la carpeta `/bin` de este repositorio. **Asegúrate de que la carpeta `/bin` esté en la misma ruta que el script**.
4.  Abre el archivo `links.txt` y pega las URL de los videos de YouTube que quieras descargar, una URL por línea.
5.  Ejecuta el script `ytmp3.py` desde tu terminal:
    ```bash
    python ytmp3.py
    ```
6.  Las canciones descargadas se guardarán automáticamente en la carpeta `/music`.

---

### ⚠️ **Importante**

* El archivo `links.txt` debe estar en la misma ruta que el programa que ejecutes (`ytmp3.exe` o `ytmp3.py`).
* El proceso puede tardar un tiempo en función del número de videos y la velocidad de tu conexión a internet.
* **Aviso: No cierres la ventana ni toques nada mientras el programa esté en ejecución.** Espera a que termine por completo.
