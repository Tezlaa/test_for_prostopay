
class NotFoundUserById(Exception):
    def __init__(self, user_id: int) -> None:
        super().__init__(f'Not found user by this id: {user_id}.')