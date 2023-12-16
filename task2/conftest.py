import asyncio
from typing import AsyncGenerator

import pytest
import pytest_asyncio

from sqlalchemy.ext.asyncio import AsyncSession, AsyncEngine, create_async_engine
from sqlalchemy.orm import sessionmaker

from config.settings import DB_CONNECTION_URL
from config.database import BaseModel


@pytest_asyncio.fixture
async def engine() -> AsyncEngine:
    return create_async_engine(DB_CONNECTION_URL, echo=False)
    

@pytest_asyncio.fixture(autouse=True)
async def session(engine: AsyncEngine) -> AsyncGenerator[AsyncSession, None]:
    maker = sessionmaker(bind=engine, class_=AsyncSession, expire_on_commit=False)
    
    async with maker() as session:
        yield session
    
    await engine.dispose()


@pytest_asyncio.fixture(autouse=True)
async def start_database(engine: AsyncEngine) -> AsyncGenerator[None, None]:
    async with engine.begin() as connect:
        await connect.run_sync(BaseModel.metadata.drop_all)
        await connect.run_sync(BaseModel.metadata.create_all)
    
    yield
    
    async with engine.begin() as connect:
        await connect.run_sync(BaseModel.metadata.drop_all)


@pytest.fixture(scope='session')
def event_loop():
    loop = asyncio.get_event_loop_policy().new_event_loop()
    
    yield loop
    
    loop.close()