import json
from Classes import Song, Album, Playlist, Listener, Musician
import Instance_Creator



def show_likes(user):
    while True:
        print("""¿Qué likes desea ver?
1. Canciones
2. Albumes
3. Playlists
4. Playlists Creados
5. Salir""")
        answer = input("")
        if answer == "1":
            show_songs_from_artist(user, user.liked_songs)
            break
        elif answer == "2":
            show_albums_from_artist(user, user.liked_albums)
            break
        elif answer == "3":
            show_playlists_from_artist(user, user.liked_playlists)
            break
        elif answer == "4":
            show_playlists_from_artist(user, user.created_playlists)
            break
        elif answer == "5":
            break
    

def changing_user_data(user):
    while True:
        print("""¿Qué dato desea cambiar?
1. Nombre
2. Correo
3. Atrás""")
        answer = input("")
        if answer == "1":
            answer = input("Ingrese su nombre")
            user.set_name(answer)
        elif answer == "2":
            answer = input("Ingrese un email válido (que termine en @unimet.edu.ve):")
            user.set_email(answer)
        elif answer == "3":
            break
        else:
            print("Respuesta invalida")


def search_engine(user):
    while True:
        print("""¿Qué desea buscar?
1. Perfil
2. Albúm
3. Canción
4. Playlist
5. Atrás""")
        answer = input("")
        if answer == "1":
            answer = input("Ingrese el nombre de usuario")
            found_user = Instance_Creator.create_user(name=answer)
            if found_user is None:
                print("Usuario no encontrado")
                continue
            elif found_user is Listener:
                listener_menu(user, found_user)
                break
            elif found_user is Musician:
                menu_musician(user, found_user)
                break
        elif answer == "2":
            answer = input("Ingrese el nombre del Álbum")
            found_album = Instance_Creator.create_album(name=answer)
            if found_album is None:
                print("Álbum no encontrado")
                continue
            else:
                menu_album(user, found_album)
                break
        elif answer == "3":
            answer = input("Ingrese el nombre de la canción")
            found_song = Instance_Creator.create_song(name=answer)
            if found_song is None:
                print("Canción no encontrada")
                continue
            else:
                menu_with_songs(user, found_song)
                break
        elif answer == "4":
            answer = input("Ingrese el nombre de la playlist")
            found_playlist = Instance_Creator.create_playlist(name=answer)
            if found_playlist is None:
                print("Playlist no encontrada")
                continue
            else:
                menu_playlists(user, found_playlist)
                break
        elif answer == "5":
            break



def listener_menu(user, listener_user):
    while True:
        print("""Bienvenido al perfil de {}, ¿Qué desea hacer?
1. Ver albumes con likes
2. Ver canciones con likes
3. Ver playlists creados 
4. Ver playlists con likes
5. Salir""")
        answer = input("")
        if answer == "1":
            albums = listener_user.liked_albums
            show_albums_from_artist(user, albums)
            break
        elif answer == "2":
            songs = listener_user.liked_songs
            show_songs_from_artist(user, songs)
            break
        elif answer == "3":
            playlists = listener_user.playlists_created
            show_playlists_from_artist(user, playlists)
            break
        elif answer == "4":
            playlists = listener_user.liked_playlists
            show_playlists_from_artist(user, playlists)
            break
        elif answer == "5":
            break
    listener_user.delete_instance()
        


def show_albums_from_artist(user, albums):
    with open("albums.txt") as file:
        album_data = json.load(file)
    count = 1
    while True:
        print("Escoja su album")
        for album in albums:
            print("{}. {}".format(count, album_data[album]["name"]))
            count += 1
        answer = input("")
        if answer < len(albums):
            desired_album = Instance_Creator.create_album(album_id=albums[answer])
            menu_album(user, desired_album)
            break
        else:
            break

def show_songs_from_artist(user, songs):
    with open("songs.txt") as file:
        song_data = json.load(file)
    count = 1
    while True:
        print("Escoja su canción")
        for song in songs:
            print("{}. {}".format(count, song_data[song]["name"]))
            count += 1
        answer = input("")
        if answer < len(songs):
            desired_song = Instance_Creator.create_song(song_id=songs[answer])
            menu_with_songs(user, desired_song)
            break
        else:
            break

def show_playlists_from_artist(user, playlists):
    with open("songs.txt") as file:
        playlist_data = json.load(file)
    count = 1
    while True:
        print("Escoja su playlist")
        for playlist in playlists:
            print("{}. {}".format(count, playlist_data[playlist]["name"]))
            count += 1
        answer = input("")
        if answer < len(playlists):
            desired_playlist = Instance_Creator.create_playlist(playlist_id=playlists[answer])
            menu_playlists(user, desired_playlist)
            break
        else:
            break

def menu_album(user, album):
    while True:
        print("""Ha entrado al album {}. ¿Qué desea hacer?
1. Reproducir albúm
2. Dar like
3. Remover like
4. Ir al perfil del músico
5. Salir""")
        answer = input("")
        if answer == "1":
            Instance_Creator.play_songs(album, user)
            break
        elif answer == "2":
            if user.give_like_album(album) == True:
                print("Like agregado")
            else:
                print("Ya le ha dado like a este elemento")
        elif answer == "3":
            if user.remove_like_album(album) == True:
                print("Like removido")
            else:
                print("No le había dado like a este álbum")
        elif answer == "4":
            user_musician = Instance_Creator.create_user(user_id=album.get_artist_id)
            menu_musician(user, user_musician)
            break
        elif answer == "5":
            break
    album.delete_instance()

def menu_playlists(user, playlist):
    while True:
        print("""Ha entrado al playlist {}. ¿Qué desea hacer?
1. Reproducir playlist
2. Dar like
3. Remover like
4. Ir al perfil del usuario
5. Salir""")
        answer = input("")
        if answer == "1":
            Instance_Creator.play_songs(playlist, user)
            break
        elif answer == "2":
            if user.give_like_playlist(playlist) == True:
                print("Like agregado")
            else:
                print("Ya le ha dado like a este elemento")
        elif answer == "3":
            if user.remove_like_playlist(playlist) == True:
                print("Like removido")
            else:
                print("No le había dado like a este álbum")
        elif answer == "4":
            user_listener = Instance_Creator.create_user(user_id=playlist.get_artist_id)
            listener_menu(user, user_listener)
            break
        elif answer == "5":
            break
    playlist.delete_instance()

        
        
def menu_musician(user, musician):
    while True:
        print("""Ha entrado al perfil de {}. ¿Qué desea hacer?
1. Dar like
2. Remover like
3. Ver albums
4. Ver estadísticas
5. Atrás""")
        answer = input("")
        if answer == "1":
            if user.give_like_artist(musician) == True:
                print("Like agregado!")
            else:
                print("Ya le dió like a este perfil")
        elif answer == "2":
            if user.remove_like_artist(musician) == True:
                print("Like removido")
            else:
                print("No le había dado like a este usuario")
        elif answer == "3":
            albums = musician.get_albums()
            show_albums_from_artist(user, albums)
            break
        elif answer == "4":
            top_ten, total_reproductions = musician.get_statistics()
            count = 1
            for song in top_ten:
                print("{}. {} con {} reproducciones".format(count, song[0], song[1]))
                count += 1
            print("Tiene un total de {} reproducciones".format(total_reproductions))
        elif answer == "5":
            break
    musician.delete_instance()
        

def menu_with_songs(user, song):
    while True:
        print("""Canción: {}, ¿Qué desea hacer?
1. Reproducir la canción
2. Dar like
3. Remover like
4. Ir al perfil del músico
5. Ir al album
6. Siguiente (en albúm)
7. Salir""")
        answer = input("")
        if answer == "1":
            song.reproduce_song()
        elif answer == "2":
            if user.give_like_song(song) == True:
                print("Like agregado!")
            else:
                print("Ya le dió like a esta canción")
        elif answer == "3":
            if user.remove_like_song(song) == True:
                print("Like removido")
            else:
                print("No le había dado like a esta canción")
        elif answer == "4":
            musician_artist = Instance_Creator.create_user(user_id=song.get_artist_id)
            menu_musician(user, musician_artist)
            break
        elif answer == "5":
            album_id = song.album
            album = Instance_Creator.create_album(album_id)
            menu_album(user, album)
            break
        elif answer == "6":
            song.delete_instance()
            return True
        elif answer == "7":
            break
    song.delete_instance()
    return False