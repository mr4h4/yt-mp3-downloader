# 🎶 YouTube to MP3 Converter

Un script sencillo que descarga videos de YouTube y los convierte a formato `.mp3` utilizando **yt-dlp** y **ffmpeg**. Este repositorio incluye tanto el código fuente en **Python** (`.py`) como una **versión compilada para Windows** (`.exe`).

---

### 🚀 Cómo usarlo

Elige la opción que mejor se adapte a ti. ¡Ambas son muy fáciles!

#### **Opción 1: Usar la versión compilada (.exe) - Recomendado ✅**

Esta es la forma más rápida y directa. ¡No necesitas instalar absolutamente nada!

1.  Descarga los archivos `ytmp3.exe` y `links.txt` de este repositorio.
2.  Coloca ambos archivos en la misma carpeta. **¡Importante!** No cambies el nombre de `links.txt`.
3.  Abre `links.txt` y pega las URL de YouTube que quieras descargar, **una por línea**.
4.  Haz doble clic en `ytmp3.exe` para ejecutar el programa.
5.  El programa se encargará de todo. Tus canciones se guardarán automáticamente en la carpeta `/music`.

---

#### **Opción 2: Usar el script de Python (.py) 🐍**

Si prefieres usar el código fuente o estás en otro sistema operativo, sigue estos pasos.

1.  Asegúrate de tener **Python** instalado en tu sistema.
2.  Instala la librería **yt-dlp** ejecutando este comando en tu terminal:
    ```bash
    pip install yt-dlp
    ```
3.  El programa necesita **ffmpeg**, que ya viene incluido en la carpeta `/bin` de este repositorio. Asegúrate de que esta carpeta esté en la misma ruta que tu script.
4.  Abre `links.txt` y pega las URL de los videos que quieras descargar, una por línea.
5.  Ejecuta el script desde tu terminal:
    ```bash
    python ytmp3.py
    ```
6.  Las canciones se guardarán automáticamente en la carpeta `/music`.

---

### ⚠️ **Importante**

* El archivo `links.txt` debe estar siempre en la misma ubicación que el programa que ejecutes (`ytmp3.exe` o `ytmp3.py`).
* El tiempo de descarga y conversión puede variar según la cantidad de videos y tu conexión a internet.
* **¡Atención!** Una vez que el programa se esté ejecutando, **no cierres la ventana ni interactúes con ella**. Simplemente espera a que termine por completo y se cierre por sí sola.
