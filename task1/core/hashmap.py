from dataclasses import dataclass
from typing import Hashable, TypeVar, Any

from core.exceptions import NotFoundByKey


T = TypeVar('T')


@dataclass
class Pointer:
    hashed_key: int
    memory_pointer: int


class HashMap:
    def __init__(self, size: int = 20) -> None:
        self.__memory: list = [None] * (size + 1)
        self.__pointers: list[Pointer] = []
        self.size: int = 0
        
    def put(self, key: Hashable, value: T) -> T:
        pointer = Pointer(
            hashed_key=self._hash_func(key),
            memory_pointer=self.size,
        )
        
        self.__pointers.append(pointer)
        self.__memory[self.size] = value
        
        self.__sort_pointers()
        self.size += 1
        
        return value

    def get(self, key: Hashable) -> Hashable:
        
        hashed_key = self._hash_func(key)
        try:
            memory_pointer = self.__lookup_memory_pointer(hashed_key)
        except NotFoundByKey:
            raise NotFoundByKey(key=key)

        return self.__memory[memory_pointer]
    
    def __setitem__(self, key: Hashable, value: T) -> T:
        return self.put(key=key, value=value)
    
    def __getitem__(self, key: Hashable) -> Any:
        return self.get(key=key)
    
    def _hash_func(self, key: Hashable) -> int:
        return hash(key)
    
    def __lookup_memory_pointer(self, hashed_key: int) -> int:
        """ Using binary search to find a pointer """
        
        low, high = 0, len(self.__pointers) - 1
        while low <= high:
            mid_index = (low + high) // 2
            pointer = self.__pointers[mid_index]

            if pointer.hashed_key == hashed_key:
                return pointer.memory_pointer
            
            if pointer.hashed_key < hashed_key:
                low = mid_index + 1
            else:
                high = mid_index - 1
        
        raise NotFoundByKey(key=hashed_key)

    def __sort_pointers(self) -> None:
        self.__pointers.sort(key=lambda pointer: pointer.hashed_key)
