from business.service_clienti import ServiceClienti
from business.service_filme import ServiceFilme
from domeniu.client import Client
from domeniu.film import Film
from erori.validation_error import ValidError
from infrastructura.repo_clienti import RepoCleinti
from infrastructura.repo_filme import RepoFilme
from validare.validare_client import ValidatorClient
from validare.validare_film import ValidatorFilm


class TesteFilm:

    def __init__(self):
        self.__id_film = 0
        self.__titlu = "Titanic"
        self.__descriere = "Super"
        self.__gen = "Drama"
        self.__film = Film(self.__id_film, self.__titlu, self.__descriere, self.__gen)

    def __ruleaza_teste_domain(self):
        assert (self.__film.get_id_film() == self.__id_film)
        assert (self.__film.get_titlu() == self.__titlu)
        assert (self.__film.get_descriere() == self.__descriere)
        assert (self.__film.get_gen() == self.__gen)

        self.__titlu_nou = "Spider-Man"
        self.__film.set_titlu(self.__titlu_nou)
        assert (self.__film.get_titlu() == self.__titlu_nou)

        self.__descriere_noua = "Decent"
        self.__film.set_descriere(self.__descriere_noua)
        assert (self.__film.get_descriere() == self.__descriere_noua)

        self.__gen_nou = "Actiune"
        self.__film.set_gen(self.__gen_nou)
        assert (self.__film.get_gen() == self.__gen_nou)


    def __ruleaza_teste_validator(self):
        self.__id_film_gresit = -1
        self.__titlu_gresit = ""
        self.__descriere_gresit = ""
        self.__gen_gresit = ""
        self.__film_gresit = Film(self.__id_film_gresit, self.__titlu_gresit, self.__descriere_gresit, self.__gen_gresit)

        try:
            ValidatorFilm().valideaza(self.__film_gresit)
            assert False
        except ValidError as ve:
            assert (str(ve) == "id invalid!\ntitlu invalid!\ndescriere invalida!\ngen invalid!\n")


    def __ruleaza_teste_infrastructura(self):
        assert (RepoFilme().__len__() == 0)
        RepoFilme().adauga_film(self.__film)


    def __ruleaza_teste_business(self):
        service_filme = ServiceFilme(ValidatorFilm(), RepoFilme())
        assert service_filme.get_len() == 0

        id_film = 0
        titlu = "Titanic"
        descriere = "Super"
        gen = "Drama"
        service_filme.adauga_film(id_film, titlu, descriere, gen)
        assert service_filme.get_len() == 1

        titlu_nou = "Spider-man"
        descriere_noua = "Super tare"
        gen_nou = "Acriune"
        service_filme.modifica_film(id_film, titlu_nou, descriere_noua, gen_nou)

        film = service_filme.cauta_film(id_film)
        assert film.get_titlu() == titlu_nou
        assert film.get_descriere() == descriere_noua
        assert film.get_gen() == gen_nou


    def ruleaza_toate_testele(self):
        self.__ruleaza_teste_domain()
        self.__ruleaza_teste_validator()
        self.__ruleaza_teste_infrastructura()
        self.__ruleaza_teste_business()
        print("Teste pentru Filme rulate cu succes!")


class TesteClient:
    def __init__(self):
        self.__id_client = 0
        self.__nume = "Tudor"
        self.__cnp = "5031105014672"
        self.__client = Client(self.__id_client, self.__nume, self.__cnp)


    def __ruleaza_teste_domain(self):
        assert (self.__client.get_id_client() == self.__id_client)
        assert (self.__client.get_nume() == self.__nume)
        assert (self.__client.get_cnp() == self.__cnp)

        self.__nume_nou = "Darius"
        self.__client.set_nume(self.__nume_nou)
        assert (self.__client.get_nume() == self.__nume_nou)

        self.__cnp_nou = "00000000000"
        self.__client.set_cnp(self.__cnp_nou)
        assert (self.__client.get_cnp() == self.__cnp_nou)


    def __ruleaza_teste_validator(self):
        self.__id_client_gresit = -2
        self.__nume_gresit = ""
        self.__cnp_gresit = ""
        self.__client_gresit = Client(self.__id_client_gresit, self.__nume_gresit, self.__cnp_gresit)

        try:
            ValidatorClient().valideaza(self.__client_gresit)
            assert False
        except ValidError as ve:
            assert (str(ve) == "id invalid!\nnume invalid!\nCNP invalid!\n")


    def __ruleaza_teste_infrastructura(self):
        assert (RepoCleinti().__len__() == 0)
        RepoCleinti().adauga_client(self.__client)

        repo_clienti = RepoCleinti()
        id_client = 0
        nume = "Tudor"
        cnp = "5031105014672"
        client = Client(id_client, nume, cnp)
        repo_clienti.adauga_client(client)
        assert repo_clienti.__len__() == 1

        nume_nou = "Darius"
        client_nou = Client(id_client, nume_nou, cnp)
        repo_clienti.modifica_client(client_nou)

        client_gasit = repo_clienti.cauta_client(id_client)
        assert client_gasit.get_nume() == nume_nou


    def __ruleaza_teste_business(self):
        service_clienti = ServiceClienti(ValidatorClient(), RepoCleinti())
        assert service_clienti.get_len() == 0

        id_client = 0
        nume = "Tudor"
        cnp = "5031105014672"
        service_clienti.adauga_client(id_client, nume, cnp)
        assert service_clienti.get_len() == 1

        nume_nou = "Darius"
        service_clienti.modifica_client(id_client, nume_nou)

        client = service_clienti.cauta_client(id_client)
        assert client.get_nume() == nume_nou


    def ruleaza_toate_testele(self):
        self.__ruleaza_teste_domain()
        self.__ruleaza_teste_validator()
        self.__ruleaza_teste_infrastructura()
        self.__ruleaza_teste_business()
        print("Teste pentru Client rulate cu succes!")