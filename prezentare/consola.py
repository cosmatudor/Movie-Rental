import random
class UI:

    def __init__(self, service_clienti, service_filme):
        self.__service_clienti = service_clienti
        self.__service_filme = service_filme


    # ---------------------- PRINTARE ----------------------
    def __print_filme(self):
        """
        Printeaza toate filmele din dictionarul de filme
        :return:
        """
        lista_filme = self.__service_filme.get_all_filme()
        if len(lista_filme) == 0:
            print("Lista de filme este goala!")
        else:
            for film in lista_filme:
                print(film)

    def __print_clienti(self):
        """
        Printeaza toti clienti din dictionarul de clienti
        :return:
        """
        lista_clienti = self.__service_clienti.get_all_clienti()
        if len(lista_clienti) == 0:
            print("Lista de clienti este goala!")
        else:
            for client in lista_clienti:
                print(client)

    # ---------------------- ADAUGARE ----------------------
    def __adauga_film(self, id_film, titlu, descriere, gen):
        """
        Adauga un film in dictionarul de filme iar apoi printeaza toate filmele
        :param id_film: int
        :param titlu: string
        :param descriere: string
        :param gen: string
        :return: -
        """
        self.__service_filme.adauga_film(id_film, titlu, descriere, gen)
        self.__print_filme()
        print("\n")

    def __adauga_client(self, id_client, nume, cnp):
        """
        Adauga un client in dictionarul de clienti iar apoi printeaza toti clientii
        :param id_client: int
        :param nume: string
        :param cnp: string
        :return: -
        """
        self.__service_clienti.adauga_client(id_client, nume, cnp)
        self.__print_clienti()
        print("\n")

    # ---------------------- STERGERE ----------------------
    def __sterge_film(self):
        print("\n")

    def __sterge_client(self):
        print("\n")

    # ---------------------- MODIFICARE ----------------------
    def __modifica_film(self, id_film, titlu, descriere, gen):
        """
        Modifica titlul, descrierea si genul filmului cu id-ul id_film
        :param id_film: int
        :param titlu: string
        :param descriere: string
        :param gen: string
        :return: -
        """
        self.__service_filme.modifica_film(id_film, titlu, descriere, gen)
        self.__print_filme()
        print("\n")

    def __modifica_client(self, id_client, nume):
        """
        Modifica numele clientului cu id-ul id_client
        :param id_client: int
        :param nume: string
        :return: -
        """
        self.__service_clienti.modifica_client(id_client, nume)
        self.__print_clienti()
        print("\n")

    # ---------------------- CAUTA ----------------------

    def __cauta_film(self, id_film):
        print(self.__service_filme.cauta_film(id_film))
        print("\n")

    def __cauta_client(self, id_client):
        print(self.__service_clienti.cauta_client(id_client))
        print("\n")


    # ---------------------- MENIU ----------------------
    def run(self):
        """
        Ruleaza meniul principal
        """
        while True:
            comanda = int(input("1. Adaugare\n2. Stergere\n3. Modifica\n4. Cauta\n5. Random\n0. Exit\n"))

            if comanda != 0 and comanda != 1 and comanda != 2 and comanda != 3 and comanda != 4 and comanda != 5:
                print("Va rugam alegeti o optiune de la 1 la 5\n")
                continue

            elif comanda == 0:
                print("Ati iesit din aplicatie!")
                return

            # ADAUGA
            elif comanda == 1:
                optiune = int(input("Doresc sa adaug un:\n1. Film\n2. Client\n"))
                if optiune == 1:
                    id_film = self.__service_filme.get_len()
                    titlu = input("Titlul filmului: ")
                    descriere = input("Descrierea filmului: ")
                    gen = input("Genul filmului: ")
                    # try except ...
                    self.__adauga_film(id_film, titlu, descriere, gen)

                elif optiune == 2:
                    id_client = self.__service_clienti.get_len()
                    nume = input("Numele clientului: ")
                    cnp = input("CNP-ul clientului: ")
                    # try except ...
                    self.__adauga_client(id_client, nume, cnp)


            # STERGE
            elif comanda == 2:
                optiune = int(input("Doresc sa sterg un:\n1. Film\n2. Client\n"))
                if optiune == 1:
                    self.__sterge_film()
                elif optiune == 2:
                    self.__sterge_client()


            # MODIFICA
            elif comanda == 3:
                optiune = int(input("Doresc sa modific un:\n1. Film\n2. Client\n"))
                if optiune == 1:
                    id_film = int(input("ID-ul filmului pe care doriti sa-l modificati: "))
                    titlu = input("Noul titlu: ")
                    descriere = input("Noua descriere: ")
                    gen = input("Noul gen: ")
                    self.__modifica_film(id_film, titlu, descriere, gen)

                elif optiune == 2:
                    id_client = int(input("ID-ul clientului pe care doriti sa-l modificati: "))
                    nume = input("Numele clientului: ")
                    self.__modifica_client(id_client, nume)


            # CAUTARE
            elif comanda == 4:
                optiune = int(input("Doresc sa caut un:\n1. Film\n2. Client\n"))
                if optiune == 1:
                    id_film = int(input("ID-ul filmului dorit: "))
                    self.__cauta_film(id_film)
                elif optiune == 2:
                    id_client = int(input("ID-ul clientului dorit: "))
                    self.__cauta_client(id_client)

            elif comanda == 5:
                optiune = int(input("1. Adauga client random\n2. Adauga film random\n"))
                if optiune == 1:
                    
                        id = self.__service_clienti.create_random_id()
                        nume = self.__service_clienti.generate_nume(random.randint(5, 15))
                        cnp = str(self.__service_clienti.create_random_id())
                        self.__adauga_client(id, nume, cnp)

                elif optiune == 2:

                        id = self.__service_clienti.create_random_id()
                        titlu = self.__service_clienti.generate_nume(random.randint(10, 20))
                        descriere = self.__service_clienti.generate_nume(random.randint(10, 20))
                        gen = self.__service_clienti.generate_nume(random.randint(10, 20))
                        self.__adauga_film(id, titlu, descriere, gen)
