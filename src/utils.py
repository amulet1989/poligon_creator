import tkinter as tk
from tkinter import filedialog
import cv2

# Conversor de coordenadas custom
def convertir_coord(x, y, xmax=1024, ymax=1024, escala=89.1):
    xout = x / escala
    yout = (ymax - y) / escala

    return (xout, yout), (x, ymax - y)


# Función para cargar la imagen
def cargar_imagen():
    root = tk.Tk()
    root.withdraw()  # Oculta la ventana principal de tkinter
    file_path = filedialog.askopenfilename(
        title="Seleccionar una imagen",
        filetypes=[("Archivos de imagen", ["*.jpg", "*.jpeg"])],
    )
    return file_path if file_path else None

def seleccionar_directorio():
    root = tk.Tk()
    root.withdraw()  # Oculta la ventana principal de tkinter

    file_path = filedialog.askdirectory(
        title="Seleccionar directorio",
    )

    if file_path:
        return file_path
    else:
        return None
    
def seleccionar_video():
    root = tk.Tk()
    root.withdraw()  # Oculta la ventana principal de tkinter

    file_path = filedialog.askopenfilename(
        title="Seleccionar una imagen",
        filetypes=[("Archivos de video", "*.mp4 *.avi")],
    )

    if file_path:
        return file_path
    else:
        return None
    
def cargar_imagen_o_video():
    root = tk.Tk()
    root.withdraw()  # Oculta la ventana principal de tkinter
    file_path = filedialog.askopenfilename(
        title="Seleccionar una imagen o video",
        filetypes=[("Archivos de imagen", ["*.jpg", "*.jpeg", "*.mp4", "*.avi"])],
    )
    return file_path if file_path else None

# obtener el frame n de un video y guardarlo como una imagen jpg
def get_frame_from_video(video_path, frame_number, width=None, height=None):
    video = cv2.VideoCapture(video_path)
    # obtener el frame n del video
    video.set(cv2.CAP_PROP_POS_FRAMES, frame_number)
    ret, frame = video.read()
    # guardar la imagen como un archivo jpg
    # cv2.imwrite(f"frame_{frame_number}.jpg", frame)
    # redimensionar la imagen
    if width and height:
        resized_frame = cv2.resize(frame, (width, height))
    else:
        resized_frame = frame
    return resized_frame