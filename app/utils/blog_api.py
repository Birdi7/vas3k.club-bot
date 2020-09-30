from typing import Optional

from aiogram.types import User
from models.user import EnrichedUser


class BlogApiCaller:
    def is_club_user(self, user: User) -> bool:
        # TODO: use api here
        pass

    def process_auth(self, user: User, secret_hash: str) -> Optional[EnrichedUser]:
        """

        :return: True if authentication was successful
        """
        # TODO: use api here
        pass

    def fetch_enriched_data(self, user: User) -> Optional[EnrichedUser]:
        """

        :param user:
        :return: None if the user didn't complete auth else information
        """
        # TODO:
        pass
