import logging
from typing import TYPE_CHECKING, List, Optional, Union

from aiogram.types import User
from aiohttp import ClientSession

from app import settings

logger = logging.getLogger("bot")

if TYPE_CHECKING:
    from app.models.user import EnrichedUser


class BlogApiCaller:
    def __init__(self):
        self.host = settings.CLUB_HOST
        self.port = settings.CLUB_PORT
        self.path = settings.CLUB_API_PATH

    def is_club_user(self, user: User) -> bool:
        # TODO: use api here
        # se
        pass

    def process_auth(self, user: User, secret_hash: str) -> Optional["EnrichedUser"]:
        """

        :return: True if authentication was successful
        """
        # TODO: use api here
        pass

    def fetch_enriched_data(self, user: User) -> Optional["EnrichedUser"]:
        """

        :param user:
        :return: None if the user didn't complete auth else information
        """
        # TODO:
        pass

    async def call(
        self,
        prefix,
        params: List[Union[int, str]],
    ):
        # FIXME: shit here for now

        logger.debug(f"Perform request at {self.construct_url(prefix, params)} with {params}")
        async with ClientSession() as session:
            async with session.get(self.construct_url(prefix, params)) as response:
                print(response.status)
                print(await response.text())

    def construct_url(self, prefix: str, params: List[Union[int, str]]) -> str:
        path_without_params = "http://{host}:{port}/{path}/{prefix}/".format(
            host=self.host, port=self.port, path=self.path, prefix=prefix
        )
        return path_without_params + "/".join(map(str, params))
