from abc import ABCMeta, abstractmethod
import requests

class API_consumer(metaclass=ABCMeta):
    @abstractmethod
    def extract(self, id):
        pass


class API_Pokemon(API_consumer):
    def __init__(self):
        self.__URL = 'https://pokeapi.co/api/v2/pokemon/'

    @property
    def URL(self):
        return self.__URL

    def extract(self, id):
        URL = self.URL + str(id)
        try:
            dado = requests.get(URL).json()
            return ((dado.get('id'), dado.get('name')))
        except:
            pass

class API_Rick_Morty(API_consumer):
    def __init__(self):
        self.__URL = 'https://rickandmortyapi.com/api/character/'
    
    @property
    def URL(self):
        return self.__URL

    def extract(self, id):
        url = self.URL + str(id)
        try:
            response = requests.get(url)

            if response.raise_for_status():
                print(f'Erro na requisição {response.status_code}')
        
            response = response.json()
            dados = (response.get('id'), response.get('name'), response.get('species'))
            return dados
        except requests.exceptions.HTTPError as e:
            print(f'Erro na requisição {e}')

class API_Star_Wars(API_consumer):
    ''' The universe of Star Wars '''
    def __init__(self):
        self.__URL = 'https://swapi.dev/api/people/'
    
    @property
    def URL(self):
        return self.__URL

    def extract(self, id):
        url = self.URL + str(id)
        
        try:
            response = requests.get(url)
            if response.raise_for_status():
                print(f'Erro na requisição {response.status_code}')
            
            response = response.json()
            dados = (response.get('name'), response.get('films'))
            return dados
        except requests.exceptions.HTTPError as e:
            print(f'Erro na requisição {e}')

class API_Ice_and_Fire(API_consumer):
    ''' The universe of Ice And Fire '''
    def __init__(self):
        self.__URL = 'https://anapioficeandfire.com/api/characters/'
    
    @property
    def URL(self):
        return self.__URL

    def extract(self, id):
        url = self.URL + str(id)
        
        try:
            response = requests.get(url)
            if response.raise_for_status():
                print(f'Erro na requisição {response.status_code}')
            
            response = response.json()
            dados = (response.get('name'), response.get('tvSeries'))
            return dados
        except requests.exceptions.HTTPError as e:
            print(f'Erro na requisição {e}')
 