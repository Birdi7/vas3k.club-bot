from dataclasses import dataclass
from typing import Any, Dict, Optional

from aiogram import types

from app.utils.blog_api import BlogApiCaller

# TODO: optimize amount of requests to club back-end
# because currently that's...shit, you know


class User(types.User):
    def __init__(self, conf: Dict[str, Any] = None, **kwargs: Any):
        super().__init__(conf, **kwargs)
        self.slug: Optional[str] = None
        self.api_caller = BlogApiCaller()
        self.populate_with_club_information(self.api_caller.fetch_enriched_data(self))

    def populate_with_club_information(self, enriched_user: Optional["EnrichedUser"]):
        if not enriched_user:
            return

        update_fields = ("slug",)
        for field in update_fields:
            setattr(self, field, getattr(enriched_user, field, None))

    def is_club_user(self) -> bool:
        return self.api_caller.is_club_user(self)

    def process_auth(self, secret_hash: str) -> bool:
        enriched_user = self.api_caller.process_auth(secret_hash)
        self.populate_with_club_information(enriched_user)
        return bool(enriched_user)

    @classmethod
    def from_aiogram_user(cls, user: types.User) -> "User":
        return cls(**user.to_python())


@dataclass
class EnrichedUser:
    slug: str
