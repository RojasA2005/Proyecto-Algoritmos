from Classes import Song, Album, Playlist, Listener, Musician
import Instance_Creator
import User_Menu
import API_Decoder

def safe_boot():
    try:
        with open("albums.txt") as file:
            pass
        with open("songs.txt") as file:
            pass
        with open("playlists.txt") as file:
            pass
        with open("users.txt") as file:
            pass
        with open("album_search.txt") as file:
            pass
        with open("playlist_search.txt") as file:
            pass
        with open("song_search.txt") as file:
            pass
        with open("user_search.txt") as file:
            pass
    except:
        API_Decoder.album_convertion()
        API_Decoder.playlists_conversion()
        API_Decoder.songs_convertion()
        API_Decoder.users_convertion()

def listener_menu(user):
    while True:
        print("""Hola, {}, elija que desea hacer:
1. Cambiar datos de perfil
2. Busqueda
3. Ver mis likes
4. Crear Playlist
5. Salirse de la cuenta
6. Borrar la cuenta""".format(user.get_name()))
        answer = input("")
        if answer == "1":
            User_Menu.changing_user_data(user)
        elif answer == "2":
            User_Menu.search_engine(user)
        elif answer == "3":
            User_Menu.show_likes(user)
        elif answer == "4":
            Instance_Creator.create_new_playlist(user)
        elif answer == "5":
            user.delete_instance()
            break
        elif answer == "6":
            user.delete_listener()
            break

def musician_menu(user):
    while True:
        print("""Bienvenido, {}, elija que desea hacer
1. Cambiar datos de perfil
2. Crear albúm
3. Salirse de la cuenta
4. Borrar cuenta""".format(user.get_name()))
        answer = input("")
        if answer == "1":
            User_Menu.changing_user_data(user)
        elif answer == "2":
            Instance_Creator.create_new_album(user)
        elif answer == "3":
            user.delete_instance()
            break
        elif answer == "4":
            user.delete_musician()
            break


def user_managing(user):
    if type(user) == Listener:
        listener_menu(user)
    else:
        musician_menu(user)


def main():
    while True:
        print("""Bienvenido a Metrotify:
1. Iniciar sesión
2. Crear Usuario Nuevo
3. Salir""")
        answer = input("")
        if answer == "1":
            while True:
                answer = input("Ingrese el nombre de su usario (0 para devolverse)")
                if answer == "0":
                    break
                principal_user = Instance_Creator.create_user(answer)
                if principal_user == None:
                    print("Usuario no encontrado.")
                else:
                    user_managing(principal_user)
                    break
        elif answer == "2":
            principal_user = Instance_Creator.create_new_user()
            user_managing(principal_user)
        elif answer == "3":
            break

safe_boot()
main()
