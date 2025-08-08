import yt_dlp 
import os

def download_mp3(link):
    current_script_path = os.path.dirname(os.path.abspath(__file__))
    ffmpeg_bin_path = os.path.join(current_script_path, 'bin')
    # Agrega la carpeta 'bin' al PATH del entorno de ejecución de Python.
    # Esto le dice a yt-dlp dónde encontrar ffmpeg.
    os.environ["PATH"] = os.pathsep.join([ffmpeg_bin_path] + os.environ.get("PATH", "").split(os.pathsep))

    ydl_opts = {
        'verbose': False,
        'quiet': True,
        'no_warnings': True,    
        'ignoreerrors': True,
        'ignore_fragment_erros': True,
        #'progress_hooks': [],
        #'logger': None, 
        'format': 'bestaudio/best',
        'noplaylist': True,
        'extractaudio': True,
        'audioformat': 'mp3',
        'outtmpl': 'music/%(title)s.%(ext)s',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(link, download=True)
            title = info.get('title', 'Unknown Title')

            ydl.download([link])
            print(f"{title} | descargado con exito.")
    except Exception as e:
        print(f"Error durante la descarga: {e}")

# Usar archivo de texto para obtener los enlaces
with open("links.txt", "r") as archivo:
    links = [line.strip() for line in archivo if line.strip()]

downloaded_links = 0
for link in links:
    download_mp3(link)
    downloaded_links += 1
print(f"¡DESCARGA COMPLETADA! | Se han descargado {downloaded_links} arhivos MP3. ✅")
    