
from googleapiclient.discovery import build

def obtener_trailer(nombre_pelicula):
    # Crea una instancia de la API de YouTube
    youtube_api = build('youtube', 'v3', developerKey='')
    
    # Realiza una búsqueda en YouTube con el nombre de la película y el término "trailer"
    resultado_busqueda = youtube_api.search().list(q=f'{nombre_pelicula} trailer', part='id', maxResults=1).execute()
        
    # Obtiene el ID del video del primer resultado de la búsqueda
    if resultado_busqueda['items']:
        video_id = resultado_busqueda['items'][0]['id']['videoId']
        return f'https://www.youtube.com/watch?v={video_id}'
    else:
        return 'No se encontró ningún trailer para esa película'
"""
# Ejemplo de uso
nombre_pelicula = input('Ingresa el nombre de la película: ')
trailer_url = obtener_trailer(nombre_pelicula)
print(f'Trailer de "{nombre_pelicula}": {trailer_url}')
"""
