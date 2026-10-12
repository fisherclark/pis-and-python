import random

class Song:
	def __init__(self, title, artist, duration):
		self.title = title
		self.artist = artist
		self.duration = duration
class Playlist:
	songs = []
	def __init__(self, name):
		self.name = name
	def add_song(self, song):
		self.songs.append(song)
	def get_total_duration(self):
		total = 0
		for i in self.songs:
			total += i.duration
		minutes = str(total//60)
		seconds = str(total%60)
		while len(minutes) < 2:
			minutes = "0" + minutes
		while len(seconds) < 2:
			seconds = "0" + seconds
		print(f"{minutes}:{seconds}")
		return(f"{minutes}:{seconds}")
	def find_by_artist(self, artist_name):
		artist_songs = []
		artists = []
		for i in self.songs:
			artists.append(i.artist.strip().lower())
		if not artist_name.strip().lower() in artists:
			print(f"{artist_name} is not in playlist")
			return artist_songs
		for i in self.songs:
			if i.artist.strip().lower() == artist_name.strip().lower():
				artist_songs.append(i)
		print(f"\nSongs by {artist_name}\n-----------------------")
		for i in artist_songs:
			print(f"{i.title}")
	def print_playlist(self):
		print(f"{self.name.upper().strip()}\n-----------------")
		for i in self.songs:
			print(f"{i.title}, {i.artist}")
	def load_songs(self, filename):
		with open(filename, "r") as file:
			lines = file.readlines()
		for i in lines:
			values = i.strip("\n").split(",")
			if not values[2].isnumeric():
				continue
			self.songs.append(Song(values[0], values[1], int(values[2])))
	def shuffle(self):
		for i in range(len(self.songs)-1, 0, -1):
			j = random.randint(0, i)
			self.songs[i], self.songs[j] = self.songs[j], self.songs[i]
def main():
    playlist = Playlist("My Playlist")
    playlist.load_songs("songs.csv")
    playlist.add_song(Song("My Fav Song", "Megabytes", 250))
    playlist.shuffle()
    playlist.print_playlist()
    playlist.get_total_duration()
    playlist.find_by_artist("Null Pointer")
main()

