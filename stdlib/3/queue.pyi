# Stubs for queue

# NOTE: These are incomplete!

from typing import Any, TypeVar, Generic, Optional

_T = TypeVar('_T')

class Empty(Exception): ...
class Full(Exception): ...

class Queue(Generic[_T]):
    maxsize = ...  # type: int
    def __init__(self, maxsize: int = ...) -> None: ...
    def _init(self, maxsize: int) -> None: ...
    def empty(self) -> bool: ...
    def full(self) -> bool: ...
    def get(self, block: bool = ..., timeout: Optional[float] = ...) -> _T: ...
    def get_nowait(self) -> _T: ...
    def _get(self) -> _T: ...
    def put(self, item: _T, block: bool = ..., timeout: Optional[float] = ...) -> None: ...
    def put_nowait(self, item: _T) -> None: ...
    def _put(self, item: _T) -> None: ...
    def join(self) -> None: ...
    def qsize(self) -> int: ...
    def _qsize(self) -> int: ...
    def task_done(self) -> None: ...

class PriorityQueue(Queue): ...
class LifoQueue(Queue): ...
