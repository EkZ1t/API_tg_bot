import json

import requests

class CRUD:

    def get_all_todos(passer, url='http://3.67.196.232/'):
        response = requests.get(url + 'todo/all')
        if response.status_code == 200:
            return json.loads(response.text) 
        return f' непредвиденная ошибка - {response.status_code}'

    def create_todo(passer, data, url='http://3.67.196.232/'):
        response = requests.post(url + 'todo/create', data=json.dumps(data))
        if response.status_code == 200:
            return 'запись создана'
        return f' непредвиденная ошибка - {response.status_code}'

    def retrieve_todo(passer, id_: int, url='http://3.67.196.232/'):
        response = requests.get(url + f'todo/{id_}')
        if response.status_code == 200:
            return json.loads(response.text) 
        elif response.status_code == 404:
            return 'запись не найдена'
        return f'непредвиденная ошибка - {response.status_code}'

    def update_todo(passer, data, id_, url='http://3.67.196.232/'):
        response = requests.put(url + f'todo/{id_}/update', data=json.dumps(data))
        if response.status_code == 200:
            return 'запись обновлена'
        elif response.status_code == 404:
            return 'запись не найдена'
        return f'непредвиденная ошибка - {response.status_code}'

    def delete_todo(passer, id_, url='http://3.67.196.232/'):
        response = requests.delete(url + f'todo/{id_}/delete')
        if response.status_code == 200:
            return 'запись удалена'
        elif response.status_code == 404:
            return 'запись не найдена'
        return f'непредвиденная ошибка - {response.status_code}' 