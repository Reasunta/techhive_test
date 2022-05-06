from clients.thecatapi_client import TheCatApiClient
from models.vote_models import VotesList, VoteModel

import random


class TestTheCatApi:
    def test_get_votes(self):
        # Arrange
        cat_api = TheCatApiClient()

        # Act
        votes = cat_api.get_votes(is_raw=True)
        actual_votes = VotesList(votes.json())

        # Arrange
        assert votes.status_code == 200
        assert actual_votes.get_votes_len() > 0

    def test_get_vote_by_id(self):
        # Arrange
        cat_api = TheCatApiClient()
        expected_vote = cat_api.get_votes().get(0)

        # Act
        actual_vote = cat_api.get_vote_by_id(expected_vote.id, is_raw=True)
        actual_model = VoteModel(**actual_vote.json())

        # Arrange
        assert actual_vote.status_code == 200
        assert len(actual_vote.text) > 0
        # match actual_model and expected_vote
