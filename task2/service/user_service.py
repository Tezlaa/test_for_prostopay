from typing import Optional

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, insert

from service.schemas import UserDTO, UserType
from service.models import UsersModel
from service.exceptions import NotFoundUserById


class UserService:
    def __init__(self, session: AsyncSession) -> None:
        self._session = session
        
    async def get(self, user_id: int) -> UserDTO:
        """ Get UserDTO by user id """
        
        user = await self.__filter(id=user_id)
        if not user:
            raise NotFoundUserById(user_id)
        
        return user

    async def add(self, user: UserType) -> None:
        """
        Add user to database.
        If the user exists in the database, returned None
        """
        
        found_user = await self.__filter(username=user.username)
        if found_user:
            return
        
        await self.__insert(user)
    
    async def __filter(self, **kwargs) -> Optional[UserDTO]:
        """
        Filter for selecting from service.models.UsersModel model
        Using example:
            self.__filter(username='Bogdan', id=5)
            => will be translate to select(UsersModel).where(UsersModel.username='Bogdan', UsersModel.id=5)
               and returned as pydantic model service.schemas.UserDTO
        If the user is not found, returned: None
        """
        
        filters = []
        for attribute, value in kwargs.items():
            filters.append(UsersModel.__dict__[attribute] == value)

        query = select(UsersModel).where(*filters)
        query_result = await self._session.execute(query)
        
        scalar_one = query_result.scalar_one_or_none()
        if not scalar_one:
            return None

        return UserDTO.model_validate(scalar_one)

    async def __insert(self, user_schemas: UserType) -> None:
        """
        Method for insert by schemas. Schemas need be indentical to service.model.UsersModel model
        """
        
        query = insert(UsersModel).values(
            **dict(user_schemas)
        )
        await self._session.execute(query)
        await self._session.commit()