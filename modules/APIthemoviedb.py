import requests
import json

def get_actors():
  """Obtiene una lista de todos los actores de TheMovieDatabase."""

  headers = {"Authorization": "0cf8bcf44c54573b1364140cd12ac30f"}
  response = requests.get("https://api.themoviedb.org/3/person/popular?language=es-ES", headers=headers)
  if response.status_code == 200:
    data = json.loads(response.content)
    return data
  else:
    return None

def create_actor_network():
  """Crea una red de actores a partir de la lista de actores."""

  actors = get_actors()
  if actors is not None:
    actor_network = {}
    for actor in actors:
      actor_network[actor["id"]] = actor
    for actor_a in actor_network.values():
      for actor_b in actor_network.values():
        if actor_a != actor_b:
          if actor_a["movie_credits"]["cast"].intersection(actor_b["movie_credits"]["cast"]):
            actor_network[actor_a["id"]].setdefault("links", []).append(actor_b["id"])
    return actor_network
  else:
    return None

actor_network = create_actor_network()
