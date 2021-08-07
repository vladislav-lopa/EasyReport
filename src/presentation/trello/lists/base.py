import requests


from presentation.trello.lists.list import List


class ListOperation():
   def get_name_of_list(list_id, token, key):
      query = {
         'key': key,
         'token': token
      }

      response = requests.request(
         "GET",
         List.url_for_get_name_list(list_id),
         params=query
      )

      return response.json()["name"]