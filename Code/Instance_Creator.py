import uuid
from Classes import Song, Album, Playlist, Listener, Musician
import User_Menu
import json
import Algorithms

#Verifica que el id para cualquier adición (cancion, album, playlist, usuario) sea unica y diferente del resto
def play_songs(album, user):
        with open("songs.txt") as file:
            file_content = json.load(file)
        for song in album.tracklist:
            playing_song = Song(song, file_content[song]["name"], file_content[song]["duration"], file_content[song]["link"], file_content[song]["album"], file_content[song]["artist"], file_content[song]["likes"], file_content[song]["reproduction"])
            if User_Menu.menu_with_songs(user, playing_song) == False:
                break
        album.reproductions += 1
    
def id_validation(direction):
    with open(direction) as file:
        file_content = json.load(file)
    while True:
        random_id = uuid.uuid4()
        if file_content.get(random_id) is None:
            return random_id

def create_new_playlist(user):
    random_id = id_validation("playlists.txt")
    name = input("Ingrese el nombre")
    description = input("Ingrese una descripción")
    tracklist = []
    while True:
        print("""¿Desea ingresar una canción?
1. Sí
2. No""")
        answer = input("")
        if answer == "1":
            answer = input("Ingrese el nombre de la canción")
            found_song = create_song(name=answer)
            if found_song is None:
                print("Canción no encontrada")
                continue
            else:
                tracklist.append(found_song.id)
        elif answer == "2":
            break
    created_playlist = Playlist(random_id, name, description, tracklist, user.id)
    user.playlists_created.append(created_playlist.id)
    created_playlist.delete_instance()

def create_new_song(user, album_id):
    random_id = id_validation("songs.txt")
    name = input("Ingrese el nombre de la canción")
    duration = input("Ingrese la duración de la canción")
    link = input("Ingrese un link a la canción")
    new_song = Song(random_id, name, duration, link, album_id, user.id)
    new_song.delete_instance()
    return random_id

def create_new_album(user):
    random_id = id_validation("albums.txt")
    name = input("Ingrese el nombre del album:")
    description = input("Ingrese una descripción:")
    cover = input("Coloque el link a un cover: ")
    published = input("Indique el tiempo de salida del albúm: ")
    genre = input("indique el género")
    songs = []
    while True:
        print("""Desea agregar una nueva canción
1. Sí
2. No""")
        answer = input("")
        if answer == "1":
            songs.append(create_new_song(user, random_id))
        if answer == "2":
            break
    new_album = Album(random_id, name, description, cover, published, genre, songs, user.id)
    user.created_albums.append(new_album.id)
    new_album.delete_instance()

def create_new_user():
    name = input("Ingrese su nombre: ")
    username = input("ingrese su nombre de usuario: ")
    email = input("Ingrese un email válido: ")
    random_id = id_validation("users.txt")
    while True:
        user_type = input("""Ingrese su tipo de usuario:
1. Escucha
2. Músico""")
        if user_type == "1" or user_type == "2":
            break
        print("Respuesta inválida")
    if user_type == "1":
        return Listener(random_id, name, email, username)
    else:
        return Musician(random_id, name, email, username)
    
def create_user(name=None, user_id=None):
    if user_id is None:
        user_id = sort_possible_users(name)
    if user_id is None:
        return None
    with open("users.txt") as file:
        users_loaded = json.load(file)
        user_data = users_loaded[user_id]
        if user_data["type"] == "listener":
            return Listener(user_id, user_data["name"], user_data["email"], user_data["username"], user_data["liked_songs"], user_data["liked_playlists"], user_data["created_playlists"])
        elif user_data["type"] == "musician":
            return Musician(user_id, user_data["name"], user_data["email"], user_data["username"], user_data["created_albums"])

def create_song(name=None, song_id=None):
    if song_id is None:
        song_id = sort_possible_songs(name)
    if song_id is None:
        return None
    with open("songs.txt") as file:
        songs_loaded = json.load(file)
        song_data = songs_loaded[song_id]
    return Song(song_id, song_data["name"], song_data["duration"], song_data["album"], song_data["artist"], song_data["likes"], song_data["reproductions"])

def create_album(name=None, album_id=None):
    if album_id is None:
        album_id = sort_possible_songs(name)
    if album_id is None:
        return None
    with open("albums.txt") as file:
        albums_loaded = json.load(file)
        album_data = albums_loaded[album_id]
    return Song(album_id, album_data["name"], album_data["description"], album_data["cover"], album_data["published"], album_data["genre"], album_data["artist"], album_data["likes"], album_data["reproductions"], album_data["tracklist"])    

def create_playlist(name=None, playlist_id=None):
    if playlist_id is None:
        playlist_id = sort_possible_songs(name)
    if playlist_id is None:
        return None
    with open("playlists.txt") as file:
        playlists_loaded = json.load(file)
        playlist_data = playlists_loaded[playlist_id]
    return Song(playlist_id, playlist_data["name"], playlist_data["description"], playlist_data["creator"], playlist_data["tracks"], playlist_data["likes"], playlist_data["reproductions"])    
   

def sort_possible_playlists(name):
    possible_playlists = index_finder("playlist_search.txt", name)
    if possible_playlists is None:
        return None
    with open("users.txt") as file:
        artists = json.load(file)
    with open("playlists.txt") as file:
        playlists_loaded = json.load(file)
    print("Escoja la canción (0 para salir)")
    while True:
        count = 1
        for playlist in possible_playlists:
            print("{}. Playlist {}, de {}".format(count, playlists_loaded[playlist]["name"], artists[playlists_loaded[playlist]["creator"]]["name"]))
            count += 1
        answer = int(input)
        if answer == 0:
            return None
        if answer < len(possible_playlists):
            return possible_playlists[answer-1]

def sort_possible_albums(name):
    possible_albums = index_finder("album_search.txt", name)
    if possible_albums is None:
        return None
    with open("users.txt") as file:
        artists = json.load(file)
    with open("albums.txt") as file:
        albums_loaded = json.load(file)
    print("Escoja la canción (0 para salir)")
    while True:
        count = 1
        for album in possible_albums:
            print("{}. Albúm {}, de {}".format(count, albums_loaded[album]["name"], artists[albums_loaded[album]["artist"]]["name"]))
            count += 1
        answer = int(input)
        if answer == 0:
            return None
        if answer < len(possible_albums):
            return possible_albums[answer-1]    

def sort_possible_songs(name):
    possible_songs = index_finder("song_search.txt", name)
    if possible_songs is None:
        return None
    with open("users.txt") as file:
        artists = json.load(file)
    with open("songs.txt") as file:
        songs_loaded = json.load(file)
    print("Escoja la canción (0 para salir)")
    while True:
        count = 1
        for song in possible_songs:
            print("{}. Canción {}, de {}".format(count, songs_loaded[song]["name"], artists[songs_loaded[song]["artist"]]["name"]))
            count += 1
        answer = int(input)
        if answer == 0:
            return None
        if answer < len(possible_songs):
            return possible_songs[answer-1]

def sort_possible_users(name):
    possible_users = index_finder("user_search.txt", name)
    if possible_users is None:
        return None
    with open("users.txt") as file:
        users_loaded = json.load(file)
    print("Escoja su usario (0 para salir)")
    while True:
        count = 1
        for user in possible_users:
            print("{}. Usuario {}, correo {}".format(count, users_loaded[user]["username"], users_loaded[user]["email"]))
            count += 1
        answer = int(input(""))
        if answer == 0:
            return None
        if answer < len(possible_users)+1:
            return possible_users[answer-1]

def index_finder(direction, name):
    with open(direction) as file:
        file_content = json.load(file)
        search_list = file_content
    return Algorithms.binary_search(search_list, name)

