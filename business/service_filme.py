from domeniu.film import Film


class ServiceFilme:

    def __init__(self, validator_film, repo_filme):
        self.__validator_film = validator_film
        self.__repo_filme = repo_filme

    def adauga_film(self, id_film, titlu, descriere, gen):
        """
        Creeaza un film de tip Film, il valideaza si daca este valid, il adauga in lista de clienti
        :param id_film: int
        :param titlu: string
        :param descriere: string
        :param gen: string
        :return: -
        """
        film = Film(id_film, titlu, descriere, gen)
        self.__validator_film.valideaza(film)
        self.__repo_filme.adauga_film(film)


    def modifica_film(self, id_film, noul_titlu, noua_desciere, noul_gen):
        """
        Valideaza si modifica cu noul_titlu, noua_desciere si noul_gen, titlul, descrierea si genul filmului de tip
        Film cu id_ul id_film
        :param id_film:
        :param noul_titlu:
        :param noua_desciere:
        :param noul_gen:
        :return:
        """
        film = Film(id_film, noul_titlu, noua_desciere, noul_gen)
        self.__validator_film.valideaza(film)
        self.__repo_filme.modifica_film(film)


    def cauta_film(self, id_film):
        """
        Cauta filmul de tip Film dupa id-ul sau, daca exista
        :param id_film: int
        :return: rez: Film - filmul cu id-ul id_film
        """
        return self.__repo_filme.cauta_film(id_film)

    def get_all_filme(self):
        """
         Adauga filmele din dinctionar intr-o lista
        :return: rez: list - lista de filme
        """
        return self.__repo_filme.get_all()

    def get_len(self):
        """
        Returneaza numarul total de filme din lista
        :return: rez: int - numarul total de filme
        """
        return self.__repo_filme.__len__()
