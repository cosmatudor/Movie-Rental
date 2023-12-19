from erori.repository_error import RepoError


class RepoCleinti:

    def __init__(self):
        self.__clienti = []

    def adauga_client(self, client):
        """
        adauga un client in dictionar
        :param client: Client
        :return: -
        """
        id_client = client.get_id_client()
        if id_client in self.__clienti:
            raise RepoError("Client existent!")
        self.__clienti.append(client)

    def sterge_client(self, id_client):
        """
        Sterge un client din dictionar dupa id-ul sau
        :param id_client: int
        :return: -
        """
        if id_client not in self.__clienti:
            raise RepoError("Client inexistent!")
        del self.__clienti[id_client]

    def cauta_client(self, id_client):
        """
        Cauta un client in dictionar dupa id-ul sau
        :param id_client: int
        :return: rez: Client - clientul cu id-ul id_client
        """
        if id_client not in range(0, len(self.__clienti)):
            raise RepoError("Client inexistent!")
        return self.__clienti[id_client]

    def modifica_client(self, client_nou):
        """
        Modifica clientul cu id-ul id_client cu noul client client_nou
        :param client_nou: Client
        :return: -
        """
        id_client = client_nou.get_id_client()
        if id_client not in range(0, len(self.__clienti)):
            raise RepoError("Client inexistent!")
        self.__clienti[id_client] = client_nou

    def get_all(self):
        """
        Adauga clienti din dinctionar intr-o lista
        :return: rez: list - lista de clienti
        """
        lista_clienti = []
        for client in self.__clienti:
            lista_clienti.append(client)
        return lista_clienti

    def __len__(self):
        """
        Returneaza numarul total de clienti din lista
        :return: rez: int - numarul total de clienti
        """
        return len(self.__clienti)