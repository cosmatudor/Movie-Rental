from testare.teste import TesteFilm, TesteClient
from validare.validare_client import ValidatorClient
from validare.validare_film import ValidatorFilm
from infrastructura.repo_clienti import RepoCleinti
from infrastructura.repo_filme import RepoFilme
from business.service_clienti import ServiceClienti
from business.service_filme import ServiceFilme
from prezentare.consola import UI

if __name__ == '__main__':
    teste_film = TesteFilm()
    teste_film.ruleaza_toate_testele()
    teste_client = TesteClient()
    teste_client.ruleaza_toate_testele()
    validator_client = ValidatorClient()
    validator_film = ValidatorFilm()
    repo_clienti = RepoCleinti()
    repo_filme = RepoFilme()
    service_clienti = ServiceClienti(validator_client, repo_clienti)
    service_filme = ServiceFilme(validator_film, repo_filme)
    consola = UI(service_clienti, service_filme)
    consola.run()