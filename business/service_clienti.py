from domeniu.client import Client
import random
import string

class ServiceClienti:

    def __init__(self, validator_client, repo_clienti):
        self.__validator_client = validator_client
        self.__repo_clienti = repo_clienti

    def adauga_client(self, id_client, nume, cnp):
        """
        Creeaza un client de tip Client, il valideaza si daca este valid, il adauga in lista de clienti
        :param id_client: int
        :param nume: string
        :param cnp: string
        :return: -
        """
        client = Client(id_client, nume, cnp)
        self.__validator_client.valideaza(client)
        self.__repo_clienti.adauga_client(client)


    def modifica_client(self, id_client, nume_nou):
        """
        Valideaza si modifica cu noul nume nume_nou, numele clientului de tip Client cu id_ul id_client
        :param id_client: int
        :param nume_nou: string
        :return: -
        """
        client_vechi = self.__repo_clienti.cauta_client(id_client)
        client = Client(id_client, nume_nou, client_vechi.get_cnp())
        self.__validator_client.valideaza(client)
        self.__repo_clienti.modifica_client(client)


    def cauta_client(self, id_client):
        """
        Cauta clientul de tip Client dupa id-ul sau, daca exista
        :param id_client: inr
        :return: rez: Client- clientul cu id-ul id_client
        """
        return self.__repo_clienti.cauta_client(id_client)

    def get_all_clienti(self):
        """
        Adauga clienti din dinctionar intr-o lista
        :return: rez: list - lista de clienti
        """
        return self.__repo_clienti.get_all()

    def get_len(self):
        """
        Returneaza numarul total de clienti din lista
        :return: rez: int - numarul total de clienti
        """
        return self.__repo_clienti.__len__()

    def create_random_id(self):
        '''
        creaza un id random
        :return: -
        '''
        return random.randint(1, 100000000000000000)

    def generate_nume(self,size):
        """
        genereaza un nume random
        :param size:
        :return:
        """
        chars = string.ascii_lowercase
        return "".join(random.choice(chars) for _ in range(size))
