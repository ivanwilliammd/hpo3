from typing import Any, Dict, Set
from pyhpo.pyhpo import HPOSet

class Gene:
    id: int
    name: str
    hpo: Set[int]
    def hpo_set(self) -> HPOSet: ...
    def toJSON(self, verbose: bool = False) -> Dict[str, Any]: ...
    @classmethod
    def get(cls, query: int|str) -> 'Gene': ...
    def __str__(self) -> str: ...
    def __int__(self) -> int: ...
    def __hash__(self) -> int: ...


class Omim: 
    id: int
    name: str
    hpo: Set[int]
    def hpo_set(self) -> HPOSet: ...
    def toJSON(self, verbose: bool = False) -> Dict[str, Any]: ...
    @classmethod
    def get(cls, query: int|str) -> 'Omim': ...
    def __str__(self) -> str: ...
    def __int__(self) -> int: ...
    def __hash__(self) -> int: ...
