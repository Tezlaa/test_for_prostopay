from typing import Any, Optional


class NotFoundByKey(Exception):
    def __init__(self, key: Optional[Any]) -> None:
        super().__init__(f'Not found by key: {key}.')