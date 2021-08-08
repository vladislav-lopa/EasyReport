import requests


from presentation.trello.boards.board import Board


class BoardOperation():
    def get_name_of_board(board_id, token, key):
        headers = {
           "Accept": "application/json"
        }

        query = {
           'key': key,
           'token': token
        }

        response = requests.request(
           "GET",
           Board.url_for_get_name_board(board_id),
           headers=headers,
           params=query
        )
        return response.json()["name"]