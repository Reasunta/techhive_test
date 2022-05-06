import requests
from models.vote_models import VotesList, VoteModel



class TheCatApiClient:
    def __init__(self):
        self._base_url = "https://api.thecatapi.com/v1"
        self._headers = {"x-api-key": "DEMO-API-KEY"}

    def _send_request(self, method: str, resource: str):
        url = "{}/{}".format(self._base_url, resource)
        return requests.request(method, url, headers=self._headers)

    def get_votes(self, is_raw: bool = False):
        response = self._send_request("GET", "votes")
        return response if is_raw else VotesList(response.json())

    def get_vote_by_id(self, vote_id: int, is_raw: bool = False):
        response = self._send_request("GET", "{}/{}".format("votes", vote_id))
        return response if is_raw else VoteModel(**response.json())
