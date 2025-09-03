class Song:
    # Class attributes (shared across all songs)
    count = 0
    artists = []
    genres = []
    artist_count = {}
    genre_count = {}

    def __init__(self, name, artist, genre):
        # Instance attributes (unique per song)
        self.name = name
        self.artist = artist
        self.genre = genre

        # Update class-level trackers
        self.add_song_to_count()
        self.add_to_artists(artist)
        self.add_to_genres(genre)
        self.add_to_artist_count(artist)
        self.add_to_genre_count(genre)

    # Increment total song count
    @classmethod
    def add_song_to_count(cls):
        cls.count += 1

    # Add unique artists
    @classmethod
    def add_to_artists(cls, artist):
        if artist not in cls.artists:
            cls.artists.append(artist)

    # Add unique genres
    @classmethod
    def add_to_genres(cls, genre):
        if genre not in cls.genres:
            cls.genres.append(genre)

    # Add to artist histogram
    @classmethod
    def add_to_artist_count(cls, artist):
        if artist in cls.artist_count:
            cls.artist_count[artist] += 1
        else:
            cls.artist_count[artist] = 1

    # Add to genre histogram
    @classmethod
    def add_to_genre_count(cls, genre):
        if genre in cls.genre_count:
            cls.genre_count[genre] += 1
        else:
            cls.genre_count[genre] = 1

    # Reset everything (useful for testing)
    @classmethod
    def reset(cls):
        cls.count = 0
        cls.artists = []
        cls.genres = []
        cls.artist_count = {}
        cls.genre_count = {}

    # Make the Song easier to read when printed
    def __repr__(self):
        return f"Song(name={self.name!r}, artist={self.artist!r}, genre={self.genre!r})"


# Run this only if you directly run song.py
if __name__ == "__main__":
    s1 = Song("99 Problems", "Jay-Z", "Rap")
    s2 = Song("Halo", "Beyonce", "Pop")
    s3 = Song("God's Plan", "Drake", "Rap")
    s4 = Song("Formation", "Beyonce", "Pop")

    print("Song count:", Song.count)          # 4
    print("Artists:", Song.artists)           # ['Jay-Z', 'Beyonce', 'Drake']
    print("Genres:", Song.genres)             # ['Rap', 'Pop']
    print("Genre count:", Song.genre_count)   # {'Rap': 2, 'Pop': 2}
    print("Artist count:", Song.artist_count) # {'Jay-Z': 1, 'Beyonce': 2, 'Drake': 1}
