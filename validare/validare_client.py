from erori.validation_error import ValidError


class ValidatorClient:
    def __init__(self):
        pass

    def valideaza(self, client):
        """
        Valideaza un client de tipul Client
        :param client: Client
        :return: -
        :raise: ValueError - id invalid!, daca id-ul este mai mic decat 0
                           - nume invalid!, daca numele este un sir vid
                           - CNP invalid!, daca CNP-ul este un sir vid
        """
        erori = ""
        if client.get_id_client() < 0:
            erori += "id invalid!\n"
        if client.get_nume() == "":
            erori += "nume invalid!\n"
        if client.get_cnp() == "":
            erori += "CNP invalid!\n"

        if len(erori) > 0:
            raise ValidError(erori)
