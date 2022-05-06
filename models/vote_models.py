import random

class VoteModel:
    def __init__(self, id, image_id, sub_id, created_at, value, country_code):
        self.id = id
        self.image_id = image_id
        self.sub_id = sub_id
        self.created_at = created_at
        self.value = value
        self.country_code = country_code


class VotesList:
    def __init__(self, votes: list):
        self.votes = [VoteModel(**vote) for vote in votes]

    def get_votes_len(self) -> int:
        return len(self.votes)

    def get(self, i: int):
        return self.votes[i]
