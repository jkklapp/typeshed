import sys
from _typeshed import StrPath
from collections.abc import Callable, Iterable, Mapping

__all__ = [
    "getlocale",
    "getdefaultlocale",
    "getpreferredencoding",
    "Error",
    "setlocale",
    "resetlocale",
    "localeconv",
    "strcoll",
    "strxfrm",
    "str",
    "atof",
    "atoi",
    "format",
    "format_string",
    "currency",
    "normalize",
    "LC_CTYPE",
    "LC_COLLATE",
    "LC_MESSAGES",
    "LC_TIME",
    "LC_MONETARY",
    "LC_NUMERIC",
    "LC_ALL",
    "CHAR_MAX",
]

# This module defines a function "str()", which is why "str" can't be used
# as a type annotation or type alias.
from builtins import str as _str
from decimal import Decimal
from typing import Any

CODESET: int
D_T_FMT: int
D_FMT: int
T_FMT: int
T_FMT_AMPM: int
AM_STR: int
PM_STR: int

DAY_1: int
DAY_2: int
DAY_3: int
DAY_4: int
DAY_5: int
DAY_6: int
DAY_7: int
ABDAY_1: int
ABDAY_2: int
ABDAY_3: int
ABDAY_4: int
ABDAY_5: int
ABDAY_6: int
ABDAY_7: int

MON_1: int
MON_2: int
MON_3: int
MON_4: int
MON_5: int
MON_6: int
MON_7: int
MON_8: int
MON_9: int
MON_10: int
MON_11: int
MON_12: int
ABMON_1: int
ABMON_2: int
ABMON_3: int
ABMON_4: int
ABMON_5: int
ABMON_6: int
ABMON_7: int
ABMON_8: int
ABMON_9: int
ABMON_10: int
ABMON_11: int
ABMON_12: int

RADIXCHAR: int
THOUSEP: int
YESEXPR: int
NOEXPR: int
CRNCYSTR: int

ERA: int
ERA_D_T_FMT: int
ERA_D_FMT: int
ERA_T_FMT: int

ALT_DIGITS: int

LC_CTYPE: int
LC_COLLATE: int
LC_TIME: int
LC_MONETARY: int
LC_MESSAGES: int
LC_NUMERIC: int
LC_ALL: int

CHAR_MAX: int

class Error(Exception): ...

def setlocale(category: int, locale: _str | Iterable[_str | None] | None = ...) -> _str: ...
def localeconv() -> Mapping[_str, int | _str | list[int]]: ...
def nl_langinfo(__key: int) -> _str: ...
def getdefaultlocale(envvars: tuple[_str, ...] = ...) -> tuple[_str | None, _str | None]: ...
def getlocale(category: int = ...) -> tuple[_str | None, _str | None]: ...
def getpreferredencoding(do_setlocale: bool = ...) -> _str: ...
def normalize(localename: _str) -> _str: ...
def resetlocale(category: int = ...) -> None: ...
def strcoll(__os1: _str, __os2: _str) -> int: ...
def strxfrm(__string: _str) -> _str: ...
def format(percent: _str, value: float | Decimal, grouping: bool = ..., monetary: bool = ..., *additional: Any) -> _str: ...

if sys.version_info >= (3, 7):
    def format_string(f: _str, val: Any, grouping: bool = ..., monetary: bool = ...) -> _str: ...

else:
    def format_string(f: _str, val: Any, grouping: bool = ...) -> _str: ...

def currency(val: int | float | Decimal, symbol: bool = ..., grouping: bool = ..., international: bool = ...) -> _str: ...
def delocalize(string: _str) -> _str: ...
def atof(string: _str, func: Callable[[_str], float] = ...) -> float: ...
def atoi(string: _str) -> int: ...
def str(val: float) -> _str: ...

# native gettext functions
# https://docs.python.org/3/library/locale.html#access-to-message-catalogs
# https://github.com/python/cpython/blob/f4c03484da59049eb62a9bf7777b963e2267d187/Modules/_localemodule.c#L626
if sys.platform == "linux" or sys.platform == "darwin":
    def gettext(__msg: _str) -> _str: ...
    def dgettext(__domain: _str | None, __msg: _str) -> _str: ...
    def dcgettext(__domain: _str | None, __msg: _str, __category: int) -> _str: ...
    def textdomain(__domain: _str | None) -> _str: ...
    def bindtextdomain(__domain: _str, __dir: StrPath | None) -> _str: ...
    def bind_textdomain_codeset(__domain: _str, __codeset: _str | None) -> _str | None: ...

if sys.version_info >= (3, 11):
    def getencoding() -> _str: ...

locale_alias: dict[_str, _str]  # undocumented
locale_encoding_alias: dict[_str, _str]  # undocumented
windows_locale: dict[int, _str]  # undocumented
