from erori.validation_error import ValidError


class ValidatorFilm:
    def __init__(self):
        pass

    def valideaza(self, film):
        """
        Valideaza un film de tipul Film
        :param film: Film
        :return: -
        :raise: ValidError - id invalid!, daca id-ul este mai mic decat 0
                           - titlu invalid!, daca titlul introdus este sir vid
                           - descriere invalida!, daca descrierea introdusa este sir vid
                           - gen invalid!, daca genul introdus este sir vid
        """
        erori = ""
        if film.get_id_film() < 0:
            erori += "id invalid!\n"
        if film.get_titlu() == "":
            erori += "titlu invalid!\n"
        if film.get_descriere() == "":
            erori += "descriere invalida!\n"
        if film.get_gen() == "":
            erori += "gen invalid!\n"

        if len(erori) > 0:
            raise ValidError(erori)