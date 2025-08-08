
# 🎶 YouTube to MP3 Converter

Un script sencillo que descarga videos de YouTube y los convierte a formato `.mp3` utilizando **yt-dlp** y **ffmpeg**. Este proyecto incluye tanto el código fuente en **Python** (`.py`) como una **versión compilada para Windows** (`.exe`).

---

## 📥 Descargas
### Clona este repositorio:
  ```bash
  git clone https://github.com/mr4h4/yt-mp3-downloader
  ```

### Versión compilada (no necesita ffmpeg):  Recomendado para Windows ✅
Para la versión compilada solo necesitas descargar el ejecutable y meterlo dentro de la carpeta del repositorio: 
* `ytmp3.exe`: Haz clic [aquí para descargar](https://www.mediafire.com/file/xqdqyd5qlepdlge/ytmp3.exe/file).

### Versión python (necesita ffmpeg)
El programa necesita **ffmpeg** para convertir los videos a MP3. Tienes dos opciones para obtenerlo:

* **Opción A (Recomendada):** Descarga el archivo `bin.zip` [desde aquí](https://www.mediafire.com/file/jgcedis47l4qn4l/bin.zip/file). Solo tienes que descomprimirlo y colocar la carpeta `/bin` junto a tu script. Esta opción es la más sencilla porque no requiere ninguna configuración adicional.

* **Opción B (Avanzada):** Si ya tienes **ffmpeg** instalado o prefieres gestionarlo tú mismo, puedes descargarlo de la página oficial [desde aquí](https://www.gyan.dev/ffmpeg/builds/). En este caso, deberás asegurarte de que la carpeta `/bin` de **ffmpeg** esté añadida a las **variables de entorno (PATH)** de tu sistema para que el programa la encuentre automáticamente.

---

### 📂 Estructura del proyecto

Para que el programa funcione correctamente, la estructura de tu proyecto debe ser la siguiente:

```

yt-mp3-downloader
│   links.txt (Aquí pegarás las URL de Youtube)
│   README.md
│   ytmp3.exe
│   ytmp3.py
│
├───bin (Opción A)
│   │   ffmpeg.exe
│   │   ffplay.exe
│   │   ffprobe.exe
│
└───music (Aquí se guardarán las canciones una vez descargadas)

````

---

### 🚀 Cómo usarlo

Elige la versión que mejor se adapte a ti. ¡Ambas son muy fáciles!

#### **Opción 1: Usar la versión compilada (.exe) - Recomendado para Windows ✅**

Esta es la forma más rápida y directa. ¡No necesitas instalar absolutamente nada!

1.  **Descarga el archivo ejecutable** `ytmp3.exe` desde la sección de **"Descargas"** que se encuentra arriba.
2.  **Organiza la estructura de archivos**:
    * Coloca el archivo `ytmp3.exe` en la carpeta de este repositorio, junto con el archivo `links.txt`.
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
3.  El programa necesita **ffmpeg** para la conversión de audio. Tienes dos opciones para conseguirlo:
    * **Opción A (Recomendada):** Obtén `bin.zip` desde la sección de **"Descargas"** y descomprímelo en el mismo directorio que tu script `ytmp3.py`.
    * **Opción B:** Instala `ffmpeg` de forma global en tu sistema. Puedes descargar los binarios desde [Gyan.dev](https://www.gyan.dev/ffmpeg/builds/) y añadir la ruta de la carpeta `/bin` a las variables de entorno (PATH) de tu sistema operativo.
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
* **¡Atención!** Una vez que el programa se esté ejecutando, **no cierres la ventana ni interactúes con ella**. Simplemente espera a que termine por completo o se cierre por sí sola.
