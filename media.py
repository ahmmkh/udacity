"""class movie to be imported and used in the website """
class Movie(object):
    """ this is a movie class
    attributes : title , poster url , trailer url
    """
# defining the constructor with the movie attributes
    def __init__(self, title, trailer_youtube_url, poster_image_url,):
        # these are the important attirbutes that shold a movie have when we first costruct them
        # we can add more later using functiosn like Set_year of relase of relaese
        self.trailer_youtube_url = trailer_youtube_url
        self.title = title
        self.poster_image_url = poster_image_url
        self.year = 0 #indicating its not set
    ############# Setter and Getters ###################
    def set_date(self, year):
        """Set the year relase"""
        self.year = year
    def set_new_trailer(self, new_url):
        """update the trailer url"""
        self.trailer_youtube_url = new_url
    def set_new_poster(self, new_p_url):
        """update poster url """
        self.poster_image_url = new_p_url
    ########## getters #######################
    def get_date(self):
        """get the relase year"""
        return self.year
    def get_new_trailer(self):
        """ get trailer url"""
        return self.trailer_youtube_url
    def get_poster(self):
        """ get poster url"""
        return self.poster_image_url
    ######## End Of Class #######
