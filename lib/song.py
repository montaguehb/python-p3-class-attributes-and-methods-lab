class Song:
    count = 0
    genres = []
    artists = []
    genre_count = {}
    artist_count = {}

    def __init__(self, name, artist, genre):
        self.name = name
        self.artist = artist
        self.genre = genre
        Song.inc_count()
        Song.track_genres(genre)
        Song.track_artists(artist)

    @classmethod
    def inc_count(cls):
        cls.count += 1

    @classmethod
    def track_genres(cls, genre):
        if genre not in cls.genres:
            cls.genres.append(genre)
            cls.genre_count[genre] = 0
        cls.genre_count[genre] += 1

    @classmethod
    def track_artists(cls, artist):
        if artist not in cls.artists:
            cls.artists.append(artist)
            cls.artist_count[artist] = 0
        cls.artist_count[artist] += 1