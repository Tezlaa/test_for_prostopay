import pytest

from sqlalchemy import select, insert

from sqlalchemy.ext.asyncio import AsyncSession

from service.user_service import UserService
from service.models import User
from service.schemas import UserDTO, UserType

from testcases.usernames import test_cases_usernames


@pytest.fixture
def userservice(session: AsyncSession) -> UserService:
    return UserService(session)


@pytest.mark.parametrize('username', test_cases_usernames)
async def test_added_users(username, userservice: UserService):
    await userservice.add(user=UserType(username=username))
    
    test_request = await userservice._session.execute(select(User).where(User.username == username))
    assert test_request.scalar_one_or_none().username == username


@pytest.mark.parametrize('username', test_cases_usernames)
async def test_get_users(username, userservice: UserService):
    await create_user(userservice._session, username)
    user_dto = await userservice.get(1)
    
    assert user_dto == UserDTO(username=username, id=1)


async def test_get_from_fulled_db(userservice: UserService):
    id_databases: dict[str, int] = {}
    for username in test_cases_usernames:
        user_id = await create_user(userservice._session, username)
        id_databases[username] = user_id
    
    for username, user_id in id_databases.items():
        found_user_dto = await userservice.get(user_id)
        assert UserDTO(
            id=user_id,
            username=username
        ) == found_user_dto
    

async def create_user(session: AsyncSession, username: str) -> int:
    """ Create user by username. Returned user id"""
    
    query = insert(User).values(
        username=username
    ).returning(User.id)
    returning_id = await session.execute(query)
    await session.commit()
    return returning_id.scalar_one()
    
    