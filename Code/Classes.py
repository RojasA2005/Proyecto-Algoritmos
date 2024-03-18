import json
import Algorithms
class Song:
    def __init__(self, id, name, duration, link, album, artist, likes=0, reproductions=0):
        self.id = id
        self.name = name
        self.duration = duration
        self.link = link
        self.album = album
        self.artist = artist
        self.likes = likes
        self.reproductions = reproductions

    def delete_instance(self):
        with open("songs.txt") as file:
            file_content = json.load(file)
        if file_content.get(self.id) is None:
            Algorithms.insertion("song_search.txt", self.id, self.name)
        file_content[self.id] = {"name": self.name,
                                 "duration": self.duration,
                                 "link": self.link,
                                 "album": self.album,
                                 "artist": self.artist,
                                 "likes": self.likes,
                                 "reproductions": self.reproductions}
        with open("songs.txt", "w") as file:
            json.dump(file_content, file)

    def reproduce_song(self):
        print("Now playing: {}".format(self.name))
        self.reproductions += 1

    def get_artist_id(self):
        return self.artist
    

    def add_like(self):
        self.likes += 1

    def remove_like(self):
        self.likes -= 1

class Song_collection:
    def __init__(self, id, name, description, tracklist, creator, likes=0, reproductions=0):
        self.id = id
        self.name = name
        self.description = description
        self.tracklist = tracklist
        self.creator = creator
        self.likes = likes
        self.reproductions = reproductions

    def get_artist_id(self):
        return self.creator
    
    def add_like(self):
        self.likes += 1

    def remove_like(self):
        self.likes -= 1

class Playlist(Song_collection):
    def __init__(self, id, name, description, tracks, creator, likes=0, reproductions=0):
        super().__init__(id, name, description, tracks, creator, likes, reproductions)

#Guarda los cambios que pudieron ocurrir en cada instancia del objeto, asi como su instancia en loa archivos de busqueda

    def delete_instance(self):
        with open("playlists.txt") as file:
            file_content = json.load(file)
        if file_content.get(self.id) is None:
            Algorithms.insertion("playlist_search.txt", self.id, self.name)
        file_content[self.id] = {"name": self.name,
                                 "description": self.description,
                                 "creator": self.creator,
                                 "tracks": self.tracklist,
                                 "likes": self.likes,
                                 "reproductions": self.reproductions}
        with open("playlists.txt", "w") as file:
            json.dump(file_content, file)
        del self


class Album(Song_collection):
    def __init__(self, id, name, description, cover, published, genre, tracklist, creator, likes=0, reproductions=0):
        super().__init__(id, name, description, tracklist, creator, likes, reproductions)
        self.cover = cover
        self.published_date = published
        self.genre = genre

#Guarda los cambios que pudieron ocurrir en cada instancia del objeto, asi como su instancia en loa archivos de busqueda

    def delete_instance(self):
        with open("albums.txt") as file:
            file_content = json.load(file)
        if file_content.get(self.id) is None:
            Algorithms.insertion("album_search.txt", self.id, self.name)
        file_content[self.id] = {"name": self.name,
                                 "description": self.description,
                                 "cover": self.cover,
                                 "published": self.published_date,
                                 "genre": self.genre,
                                 "artist": self.creator,
                                 "likes": self.likes,
                                 "reproductions": self.reproductions,
                                 "tracklist": self.tracklist}
        with open("albums.txt", "w") as file:
            json.dump(file_content, file)

class User:
    def __init__(self, id, name, email, username):
        self.id = id
        self.name = name
        self.set_email(email)
        self.username = username

    def check_email(self, email):
        email_split = email.split("@")
        if email_split[-1] == "unimet.edu.ve":
            return True
        return False
            
    def set_email(self, email):
        while self.check_email(email) == False:
            email = input("Ingrese una dirección de correo válida (Que termine en @unimet.edu.ve): ")
        self.email = email

    def set_name(self, name):
        self.name = name

    def get_email(self):
        return self.email
    
    def get_name(self):
        return self.name
    
    def delete_user(self):
        with open("users.txt") as file:
            file_content = json.load(file)
        del file_content[self.id]
        with open("users.txt", "w") as file:
            json.dump(file_content, file)
        del self


class Listener(User):
    def __init__(self, id, name, email, username, liked_songs=None, liked_albums=None, liked_playlists=None, liked_artists=None, playlists_created=None):
        super().__init__(id, name, email, username)
        if liked_songs is None:
            liked_songs = []
        if liked_albums is None:
            liked_albums = []
        if liked_playlists is None:
            liked_playlists = []
        if liked_artists is None:
            liked_artists = []
        if playlists_created is None:
            playlists_created = []
        self.liked_songs = liked_songs
        self.liked_albums = liked_albums
        self.liked_playlists = liked_playlists
        self.liked_artists = liked_artists
        self.playlists_created = playlists_created

    def delete_instance(self):
        with open("users.txt") as file:
            file_content = json.load(file)
            user_dictionary = file_content
        if user_dictionary.get(self.id) is None:
            Algorithms.insertion("user_search.txt", self.id, self.username)
        user_dictionary[self.id] = {"name": self.name,
                                    "email": self.email,
                                    "username": self.username,
                                    "type": "listener",
                                    "liked_songs": self.liked_songs,
                                    "liked_albums": self.liked_albums,
                                    "liked_playlists": self.liked_playlists,
                                    "created_playlists": self.playlists_created
                                    }
        with open("users.txt", "w") as file:
            json.dump(user_dictionary, file)
        del self

    def give_like_song(self, song):
        if song.id in self.liked_songs:
            return False
        self.liked_songs.append(song.id)
        song.add_like()
        return True
    
    def give_like_albums(self, album):
        if album.id in self.liked_albums:
            return False
        self.liked_albums.append(album.id)
        album.add_like()
        return True
    
    def give_like_playlist(self, playlist):
        if playlist.id in self.liked_playlists:
            return False
        self.liked_playlists.append(playlist.id)
        playlist.add_like()
        return True
    
    def give_like_artist(self, artist):
        if artist.id in self.liked_artists:
            return False
        self.liked_artists.append(artist.id)
        artist.add_like()
        return True
    
    def remove_like_song(self, song):
        if song.id in self.liked_songs:
            self.liked_songs.remove(song.id)
            song.remove_like()
            return True
        return False
    
    def remove_like_playlist(self, playlist):
        if playlist.id in self.liked_playlists:
            self.liked_playlists.remove(playlist.id)
            playlist.remove_like()
            return True
        return False
    
    def remove_like_album(self, album):
        if album.id in self.liked_albums:
            self.liked_albums.remove(album.id)
            album.remove_like()
            return True
        return False
    
    def remove_like_artist(self, artist):
        if artist.id in self.liked_artists:
            self.liked_artists.remove(artist.id)
            artist.remove_like()
            return True
        return False
    
#Se eliminan todos los likes que dió la cuenta, así como sus playlists creadas

    def delete_listener(self):

        with open("playlists.txt") as file:
            playlists_loaded = json.load(file)
        for playlist in self.liked_playlists:
            playlists_loaded[playlist]["likes"] -= 1
        for playlist in self.playlists_created:
            del playlists_loaded[playlist]

        with open("songs.txt") as file:
            songs_loaded = json.load(file)
        for playlist in self.liked_songs:
            songs_loaded[playlist]["likes"] -= 1

        with open("albums.txt") as file:
            albums_loaded = json.load(file)
        for album in self.liked_albums:
            albums_loaded[album]["likes"] -= 1

        with open("playlists.txt", "w") as file:
            json.dump(playlists_loaded, file)
        with open("songs.txt", "w") as file:
            json.dump(songs_loaded, file)
        with open("albums.txt", "w") as file:
            json.dump(albums_loaded, file)

        with open("playlist_search.txt") as file:
            all_playlists = json.load(file)
        for playlist in self.playlists_created:
            all_playlists.remove(Algorithms.linear_search(all_playlists, playlist))

        with open("playlist_search.txt", "w") as file:
            json.dump(all_playlists, file)

        self.delete_user()

    


class Musician(User):
    def __init__(self, id, name, email, username, created_albums=None, likes=0):
        super().__init__(id, name, email, username)
        if created_albums is None:
            created_albums = []
        self.likes = likes
        self.created_albums = created_albums

    def delete_instance(self):
        with open("users.txt") as file:
            file_content = json.load(file)
            user_dictionary = file_content
        if user_dictionary.get(self.id) is None:
            Algorithms.insertion("user_search.txt", self.id, self.username)
        user_dictionary[self.id] = {"name": self.name,
                                    "email": self.email,
                                    "username": self.username,
                                    "type": "musician",
                                    "created_albums": self.created_albums,
                                    "likes": self.likes
                                    }
        with open("users.txt", "w") as file:
            json.dump(user_dictionary, file)
        del self

    def add_like(self):
        self.likes += 1

    def remove_likes(self):
        self.likes -= 0

    def delete_musician(self):
        with open("albums.txt") as file:
            file_content = json.load(file)
        songs_todelete = []
        for album in self.created_albums:
            songs_todelete.append(file_content[album]["tracklist"])
            del file_content[album]
        
        with open("songs.txt") as file:
            songs_loaded = json.load(file)
            for song in songs_todelete:
                del songs_loaded[song]

        with open("albums.txt", "w") as file:
            json.dump(file_content, file)
        with open("songs.txt", "w") as file:
            json.dump(songs_loaded, file)

        with open("song_search.txt") as file:
            all_songs = json.load(file)
        for song in songs_todelete:
            all_songs.remove(Algorithms.linear_search(all_songs, song))
        with open("album_search.txt") as file:
            all_albums = json.load(file)
        for album in self.created_albums:
            all_albums.remove(Algorithms.linear_search(all_albums, album))

        with open("song_search.txt", "w") as file:
            json.dump(all_songs, file)
        with open("album_search.txt", "w") as file:
            json.dump(all_albums, file)

        self.delete_user()

    def get_albums(self):
        return self.created_albums
    
    def get_statistics(self):
        total_reproductions = 0
        top_ten_songs = []
        with open("albums.txt") as albums:
            albums_loaded = json.load(albums)
        with open("songs.txt") as songs:
            songs_loaded = json.load(songs)
        for album in self.created_albums:
            for song in albums_loaded[album]["tracklist"]:
                top_ten_songs.append([songs_loaded[song]["name"], songs_loaded[song]["reproductions"]])
                total_reproductions += songs_loaded[song]["reproductions"]
        Algorithms.selection_sort(top_ten_songs)
        return top_ten_songs[:10], total_reproductions
