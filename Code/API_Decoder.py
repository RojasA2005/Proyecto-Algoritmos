from Algorithms import selection_sort
import json

def uploading_search_items(direction, data):
    with open(direction, "w") as file:
        selection_sort(data)
        json.dump(data, file)

def album_convertion():
    with open("api-proyecto-main/albums.json") as file:
        file_content = json.load(file)
        album_search_list = []
        album_dictionary = {}
        for album in file_content:
            album_dictionary[album["id"]] = {"name": album["name"],
                                             "description": album["description"],
                                             "cover": album["cover"],
                                             "published": album["published"],
                                             "genre": album["genre"],
                                             "artist": album["artist"],
                                             "likes": 0,
                                             "reproductions": 0,
                                             "tracklist": [song_id["id"] for song_id in album["tracklist"]]}
            album_search_list.append([album["id"], album["name"]])
    with open("albums.txt", "w") as album:
        json.dump(album_dictionary, album)
    uploading_search_items("album_search.txt", album_search_list)

def songs_convertion():
    with open("api-proyecto-main/albums.json") as file:
        file_content = json.load(file)
        song_dictionary = {}
        song_search_list = []
        for album in file_content:
            for song in album["tracklist"]:
                song_dictionary[song["id"]] = {"name": song["name"],
                                               "duration": song["duration"],
                                               "link": song["link"],
                                               "album": album["id"],
                                               "artist": album["artist"],
                                               "likes": 0,
                                               "reproductions": 0}
                song_search_list.append([song["id"], song["name"]])
    with open("songs.txt", "w") as songs:
        json.dump(song_dictionary, songs)
    uploading_search_items("song_search.txt", song_search_list)

def users_convertion():
    created_albums = {}
    created_playlists = {}
    with open("api-proyecto-main/albums.json") as file:
        file_content = json.load(file)
        for album in file_content:
            if created_albums.get(album["artist"]) is None:
                created_albums[album["artist"]] = []
            created_albums[album["artist"]].append(album["id"])
    with open("api-proyecto-main/playlists.json") as file:
        file_content = json.load(file)
        for playlist in file_content:
            if created_playlists.get(playlist["creator"]) is None:
                created_playlists[playlist["creator"]] = []
            created_playlists[playlist["creator"]].append(playlist["id"])
    with open("api-proyecto-main/users.json", encoding="utf-8") as file:
        file_content = json.load(file)
        users_dictionary = {}
        users_search_list = []
        for user in file_content:
            if user["type"] == "listener":
                users_dictionary[user["id"]] = {"name": user["name"],
                                                "email": user["email"],
                                                "username": user["username"],
                                                "type": user["type"],
                                                "liked_songs": [],
                                                "liked_albums": [],
                                                "liked_playlists": [],
                                                "liked_artists": [],
                                                "created_playlists": created_playlists.get(user["id"], [])}
            else:
                users_dictionary[user["id"]] = {"name": user["name"],
                                                "email": user["email"],
                                                "username": user["username"],
                                                "type": user["type"],
                                                "likes": 0,
                                                "created_albums": created_albums.get(user["id"], []),}
            users_search_list.append([user["id"], user["username"]])
        with open("users.txt", "w") as users:
            json.dump(users_dictionary, users)
        uploading_search_items("user_search.txt", users_search_list)

def playlists_conversion():
    with open("api-proyecto-main/playlists.json") as file:
        file_content = json.load(file)
        playlist_dictionary = {}
        playlist_search_list = []
        for playlist in file_content:
            playlist_dictionary[playlist["id"]] = {"name": playlist["name"],
                                                   "description": playlist["description"],
                                                   "creator": playlist["creator"],
                                                   "tracks": playlist["tracks"],
                                                   "likes": 0,
                                                   "reproductions": 0}
            playlist_search_list.append([playlist["id"], playlist["name"]])
    with open("playlists.txt", "w") as playlists:
        json.dump(playlist_dictionary, playlists)
    uploading_search_items("playlist_search", playlist_search_list)


users_convertion()
playlists_conversion()
songs_convertion()
album_convertion()