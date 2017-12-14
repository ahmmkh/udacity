####### Start Of  a Class ######
class Movie(object):
# defining the constructor with the movie attributes 
	def __init__(self,title,trailer_youtube_url,poster_image_url ):
		# these are the important attirbutes that shold a movie have when we first costruct them 
		# we can add more later using functiosn like Set_year of relase of relaese 
		self.trailer_youtube_url = trailer_youtube_url
		self.title = title	
		self.poster_image_url = poster_image_url
	############# Setter and Getters ####################	
	def setDate(self,year):
		self.year = year
	def setNewTrailer(self,newUrl):
		self.trailer_youtube_url =newUrl
	def setNewPoster(self,NewPUrl):
		self.poster_image_url =NewPUrl
	########## getters #######################
	def getDate(self):
		return self.year 
	def getNewTrailer(self):
		return self.trailer_youtube_url
	def getNewPoster(self):
		return self.poster_image_url
	######## End Of Class #######
			
