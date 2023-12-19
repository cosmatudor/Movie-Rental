class Film:

    def __init__(self, id_film, titlu, descriere, gen):
        """

        :param id_film:
        :param titlu:
        :param descriere:
        :param gen:
        """
        self.__id_film = id_film
        self.__titlu = titlu
        self.__descriere = descriere
        self.__gen = gen

    # id_film
    def get_id_film(self):
        """
        Returneaza id-ul filmului de tip Film
        :return: rez: int - idul filmului
        """
        return self.__id_film

    # titlu
    def get_titlu(self):
        """
        Returneaza titlul filmului de tip Film
        :return: rez: string - titul filmului
        """
        return self.__titlu

    def set_titlu(self, titlu_nou):
        """
        Seteaza titlul filmului la noul titlu_nou
        :param titlu: string
        :return: -
        """
        self.__titlu = titlu_nou

    # descriere
    def get_descriere(self):
        """
        Returneaza descrierea filmului de tip Film
        :return: rez: string - descrierea filmului
        """
        return self.__descriere

    def set_descriere(self , descriere_noua):
        """
        Seteaza descrierea filmului la noua descriere descriere_noua
        :param descriere: string
        :return: -
        """
        self.__descriere = descriere_noua

    # gen
    def get_gen(self):
        """
        Returneaza genul filmului de tip Film
        :return: rez: string - genul filmului
        """
        return self.__gen

    def set_gen(self, gen_nou):
        """
        Seteaza genul filmului la noul gen gen_nou
        :param gen: string
        :return: -
        """
        self.__gen = gen_nou

    # Verificare egaliate de 2 obiecte
    def __eq__(self, other):
        """
        Returneaza True daca cele 2 obiecte sunt egale
                   False, altfel
        :param other:
        :return: rez: bool - True or Fals
        """
        return self.__id_film == other.__id_film

    # Pretty Printuire
    def __str__(self):
        """
        Afiseaza instantele obiectului Client in maniera dorita
        :return: -
        """
        return f"{self.__id_film}. Titlu: {self.__titlu}, Descriere: {self.__descriere}, Gen: {self.__gen}"