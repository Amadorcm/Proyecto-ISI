import requests
from bs4 import BeautifulSoup

def buscar_pelicula_filmaffinity(nombre_pelicula):
    # Construir la URL de búsqueda
    nombre_pelicula=nombre_pelicula.replace(" ", "+")
    url_busqueda = f'https://www.filmaffinity.com/es/search.php?stext={nombre_pelicula}'

    # Realizar la solicitud GET a la página de búsqueda
    response = requests.get(url_busqueda)
    print(url_busqueda)
    # Comprobar si la solicitud fue exitosa
    if response.status_code == 200:
        # Obtener el contenido HTML de la página de búsqueda
        html = response.text
        
        # Crear un objeto BeautifulSoup para analizar el HTML
        soup = BeautifulSoup(html, 'html.parser')
        
        # Buscar el primer resultado de la búsqueda
        resultado = soup.find('div', class_='movie-card')
        
        if resultado:
            # Extraer el enlace, la imagen y el rating de la película
            enlace = resultado.find('a')['href']
            imagen = resultado.find('img')['src']
            rating = resultado.find('div', class_='avgrat-box').text.strip()
            titulo = resultado.find('a')['title']
            
            return enlace, imagen, rating, titulo
        else:
            print('No se encontraron resultados para la película.')
    else:
        print('No se pudo acceder a la página de búsqueda.')

# Ejemplo de uso
"""nombre_pelicula = input('Ingrese el nombre de la película: ')
resultado = buscar_pelicula_filmaffinity(nombre_pelicula)
if resultado:
    enlace, imagen, rating, titulo = resultado
    print('Enlace:', enlace)
    print('Imagen:', imagen)
    print('Rating:', rating)
    print('Título:', titulo)

"""

