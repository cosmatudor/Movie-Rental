from erori.repository_error import RepoError


class RepoFilme:

    def __init__(self):
        self.__filme = []

    def adauga_film(self, film):
        """
        adauga un film in dictionar
        :param film: Film
        :return: -
        """
        id_film = film.get_id_film()
        if id_film in self.__filme:
            raise RepoError("Film existent!")
        self.__filme.append(film)

    def sterge_film(self, id_film):
        """
        Sterge un film din dictionar dupa id-ul sau
        :param id_film: int
        :return: -
        """
        if id_film not in self.__filme:
            raise RepoError("Film inexistent!")
        del self.__filme[id_film]

    def cauta_film(self, id_film):
        """
        Cauta un film in dictionar dupa id-ul sau
        :param id_film: int
        :return: rez: Film - filmul cu id-ul id_film
        """
        if id_film not in range(0, len(self.__filme)):
            raise RepoError("Film inexistent!")
        return self.__filme[id_film]

    def modifica_film(self, film):
        """
        Modifica filmul cu id-ul id_film cu noul film film_nou
        :param film: Film
        :return: -
        """
        id_film = film.get_id_film()
        if id_film not in range(0, len(self.__filme)):
            raise RepoError("Film inexistent!")
        self.__filme[id_film] = film

    def get_all(self):
        """
        Adauga filmele din dinctionar intr-o lista
        :return: rez: list- lista de filme
        """
        lista_filme = []
        for film in self.__filme:
            lista_filme.append(film)
        return lista_filme

    def __len__(self):
        """
        Returneaza numarul total de filme din lista
        :return: rez: int - numarul total de filme
        """
        return len(self.__filme)