
import media
# storing names and reletated data of the movie in lists
import fresh_tomatoes
NAMES = [
	   "The Shawshank Redemption",
	   "The Godfather",
	   "One Flew Over the Cuckoo's Nest",
	   "Se7en",
	   "The Silence of the Lambs",
	   "The Departed",
	   "Whiplash "
]

POSTER = [
	   "https://images-na.ssl-images-amazon.com/images/M/MV5BMDFkYTc0MGEtZmNhMC00ZDIzLWFmNTEtODM1ZmRlYWMwMWFmXkEyXkFqcGdeQXVyMTMxODk2OTU@._V1_UX182_CR0,0,182,268_AL_.jpg",
	   "https://images-na.ssl-images-amazon.com/images/M/MV5BY2Q2NzQ3ZDUtNWU5OC00Yjc0LThlYmEtNWM3NTFmM2JiY2VhXkEyXkFqcGdeQXVyNzkwMjQ5NzM@._V1_UY268_CR3,0,182,268_AL_.jpg",
	   "https://images-na.ssl-images-amazon.com/images/M/MV5BZjA0OWVhOTAtYWQxNi00YzNhLWI4ZjYtNjFjZTEyYjJlNDVlL2ltYWdlL2ltYWdlXkEyXkFqcGdeQXVyMTQxNzMzNDI@._V1_UX182_CR0,0,182,268_AL_.jpg",
	   "https://images-na.ssl-images-amazon.com/images/M/MV5BOTUwODM5MTctZjczMi00OTk4LTg3NWUtNmVhMTAzNTNjYjcyXkEyXkFqcGdeQXVyNjU0OTQ0OTY@._V1_UX182_CR0,0,182,268_AL_.jpg",
	   "https://images-na.ssl-images-amazon.com/images/M/MV5BNjNhZTk0ZmEtNjJhMi00YzFlLWE1MmEtYzM1M2ZmMGMwMTU4XkEyXkFqcGdeQXVyNjU0OTQ0OTY@._V1_UX182_CR0,0,182,268_AL_.jpg",
	   "https://images-na.ssl-images-amazon.com/images/M/MV5BMTI1MTY2OTIxNV5BMl5BanBnXkFtZTYwNjQ4NjY3._V1_UX182_CR0,0,182,268_AL_.jpg",
	   "https://images-na.ssl-images-amazon.com/images/M/MV5BOTVhMWQ5MDktMGE3OS00MjVlLWExZWYtMzY2MTg4ZGFiZDQ5L2ltYWdlXkEyXkFqcGdeQXVyNjU0OTQ0OTY@._V1_UX182_CR0,0,182,268_AL_.jpg"
]

YOUTUBE = [
	   "https://www.youtube.com/watch?v=6hB3S9bIaco",
	   "https://www.youtube.com/watch?v=sY1S34973zA",
	   "https://www.youtube.com/watch?v=OXrcDonY-B8",
	   "https://www.youtube.com/watch?v=znmZoVkCjpI",
	   "https://www.youtube.com/watch?v=RuX2MQeb8UM",
	   "https://www.youtube.com/watch?v=iojhqm0JTW4",
	   "https://www.youtube.com/watch?v=7d_jQycdQGo"
]
# this is  single line for loop used to fill a list with movie objects in movies
MOVIES = [media.Movie(NAMES[i], YOUTUBE[i], POSTER[i]) for i in xrange(len(NAMES))]
# we added fresh_tomatoes function in here to view the page
fresh_tomatoes.open_movies_page(MOVIES)
