class RepoError(Exception):

    def __init__(self, erori):
        self.__erori = erori