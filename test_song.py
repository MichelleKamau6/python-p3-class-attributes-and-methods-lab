import unittest
from song import Song

class TestSong(unittest.TestCase):

    def setUp(self):
        Song.reset()  # reset before each test

    def test_song_creation(self):
        s1 = Song("99 Problems", "Jay-Z", "Rap")
        self.assertEqual(s1.name, "99 Problems")
        self.assertEqual(s1.artist, "Jay-Z")
        self.assertEqual(s1.genre, "Rap")

    def test_count_increases(self):
        Song("99 Problems", "Jay-Z", "Rap")
        Song("Halo", "Beyonce", "Pop")
        self.assertEqual(Song.count, 2)

    def test_unique_artists_and_genres(self):
        Song("99 Problems", "Jay-Z", "Rap")
        Song("Encore", "Jay-Z", "Rap")
        Song("Halo", "Beyonce", "Pop")
        self.assertEqual(set(Song.artists), {"Jay-Z", "Beyonce"})
        self.assertEqual(set(Song.genres), {"Rap", "Pop"})

    def test_genre_count(self):
        Song("99 Problems", "Jay-Z", "Rap")
        Song("Encore", "Jay-Z", "Rap")
        Song("Halo", "Beyonce", "Pop")
        self.assertEqual(Song.genre_count, {"Rap": 2, "Pop": 1})

    def test_artist_count(self):
        Song("99 Problems", "Jay-Z", "Rap")
        Song("Encore", "Jay-Z", "Rap")
        Song("Halo", "Beyonce", "Pop")
        self.assertEqual(Song.artist_count, {"Jay-Z": 2, "Beyonce": 1})

if __name__ == "__main__":
    unittest.main()
