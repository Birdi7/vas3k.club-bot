import enum
import logging
from typing import TYPE_CHECKING, Any, Dict, List, Optional, Union

from aiohttp import ClientSession

from app import settings

logger = logging.getLogger("bot")

if TYPE_CHECKING:
    from app.models.user import EnrichedUser, User


class RequestMethodEnum(enum.Enum):
    GET = "get"
    POST = "post"


class BlogApiCaller:
    def __init__(self):
        self.host = settings.CLUB_HOST
        self.port = settings.CLUB_PORT
        self.path = settings.CLUB_API_PATH

    def is_club_user(self, user: "User") -> bool:
        # TODO: use api here
        # se
        pass

    async def process_auth(self, user: "User", secret_hash: str) -> Optional["EnrichedUser"]:
        """

        :return: EnrichedUser if authentication was successful
        """
        from app.models.user import EnrichedUser

        response = await self.call(
            "user",
            secret_hash,
            data={
                "id": user.id,
                "username": user.username,
                "first_name": user.first_name,
                "last_name": user.last_name,
                "language_code": user.language_code,
            },
            request_method=RequestMethodEnum.POST,
        )

        logger.info(response)
        if response is None:
            return None

        return EnrichedUser.from_response(response)

    def fetch_enriched_data(self, user: "User") -> Optional["EnrichedUser"]:
        """

        :param user:
        :return: None if the user didn't complete auth else information
        """
        # TODO:
        pass

    async def call(
        self,
        *resources: Union[int, str],
        request_method: RequestMethodEnum = RequestMethodEnum.GET,
        json: Optional[Dict[str, Any]] = None,
        data: Optional[Dict[str, Any]] = None,
    ) -> Optional[dict]:
        logger.debug(f"Perform request at {self.construct_url(*resources)} with {data=}, {json=}")
        async with ClientSession() as session:
            async with session.request(
                request_method.value, self.construct_url(*resources), data=data, json=json
            ) as response:
                if response.status == 404:
                    return None

                return await response.json()

    def construct_url(self, *resources: List[Union[int, str]]) -> str:
        prefix, resources = (
            resources[0],
            resources[1:],
        )

        path_without_params = "http://{host}:{port}/{path}/{prefix}/".format(
            host=self.host, port=self.port, path=self.path, prefix=prefix
        )
        return path_without_params + "/".join(map(str, resources))
