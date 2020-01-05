
import sys
from typing import Union, MutableMapping, Iterator, Optional, Type
from types import TracebackType

if sys.version_info >= (3, 8):
    from typing import Final
else:
    from typing_extensions import Final

_KeyType = Union[str, bytes]
_ValueType = Union[str, bytes]

error = OSError

class _Database(MutableMapping[_KeyType, bytes]):

    def __init__(self, filebasename: str, mode: str, flag: str = ...) -> None: ...
    def sync(self) -> None: ...
    def iterkeys(self) -> Iterator[bytes]: ...  # undocumented
    def close(self) -> None: ...
    def __getitem__(self, key: _KeyType) -> bytes: ...
    def __setitem__(self, key: _KeyType, value: _ValueType) -> None: ...
    def __delitem__(self, key: _KeyType) -> None: ...
    def __iter__(self) -> Iterator[bytes]: ...
    def __len__(self) -> int: ...
    def __del__(self) -> None: ...
    def __enter__(self) -> _Database: ...
    def __exit__(self, exc_type: Optional[Type[BaseException]], exc_val: Optional[BaseException], exc_tb: Optional[TracebackType]) -> None: ...

def open(file: str, flag: str = ..., mode: int = ...) -> _Database: ...