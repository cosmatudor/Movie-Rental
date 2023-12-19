class Client:

    def __init__(self, id_client, nume, cnp):
        """

        :param id_client: int
        :param nume: string
        :param cnp: string
        """
        self.__id_client = id_client
        self.__nume = nume
        self.__cnp = cnp

    # id_client
    def get_id_client(self):
        """
        Returneaza id-ul clientului de tip Client
        :return: rez: int - idul clientului
        """
        return self.__id_client

    # nume
    def get_nume(self):
        """
        Returneaza numele clientului de tip Client
        :return: rez: string - numele clientului
        """
        return self.__nume

    def set_nume(self, nume_nou):
        """
        Seteaza numele clientului de tip Client la nume_nou
        :param nume: string
        :return: -
        """
        self.__nume = nume_nou

    # cnp
    def get_cnp(self):
        """
        Returneaza CNP-ul clientului de tip Client
        :return: rez: string - CNP-ul clientului
        """
        return self.__cnp

    def set_cnp(self, cnp_nou):
        """
        Seteaza CNP-ul clientului de tip Client la cnp_nou
        :param cnp:
        :return: -
        """
        self.__cnp = cnp_nou

    # Verificare egaliate de 2 obiecte
    def __eq__(self, other):
        """
        Returneaza True daca cele 2 obiecte sunt egale
                   False, altfel
        :param other:
        :return: rez: bool - True or Fals
        """
        return self.__id_client == other.__id_client

    # Pretty Printuire
    def __str__(self):
        """
        Afiseaza instantele obiectului Client in maniera dorita
        :return: -
        """
        return f"{self.__id_client}. Nume: {self.__nume}, CNP: {self.__cnp}"