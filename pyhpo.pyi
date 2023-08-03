from typing import Any, Dict, Iterable, Iterator, List, Set, Tuple

from . import annotations as annotations
from annotations import Gene as Gene
from annotations import Omim as Omim


__version__: str
__backend__: str


class InformationContent:
    gene: float
    omim: float
    def __getitem__(self, key: str) -> float: ...




class HPOTerm:
    id: str
    name: str
    information_content: InformationContent
    parents: Set[HPOTerm]
    all_parents: Set[HPOTerm]
    children: Set[HPOTerm]
    genes: Set[Gene]
    diseases: Set[Omim]
    categories: List[HPOTerm]
    def parent_of(self, other: HPOTerm) ->  bool: ...
    def child_of(self, other: HPOTerm) -> bool: ...
    def parent_ids(self) -> List[int]: ...
    def common_ancestors(self, other: HPOTerm) -> Set[HPOTerm]: ...
    def count_parents(self) -> int: ...
    def shortest_path_to_root(self) -> int: ...
    def shortest_path_to_parent(self, other: HPOTerm) -> Tuple[float, List[HPOTerm]]: ...
    def path_to_other(self, other: HPOTerm) -> Tuple[int, List[HPOTerm], int, int]: ...
    def similarity_score(self, other: HPOTerm, kind: str = "omim", method: str = "graphic") -> float: ...
    def similarity_scores(self, other: List[HPOTerm], kind: str = "omim", method: str = "graphic") -> List[float]: ...
    def toJSON(self, verbose: bool = False) -> Dict[str, Any]: ...
    def __str__(self) -> str: ...
    def __int__(self) -> int: ...
    def __hash__(self) -> int: ...


class HPOSet:
    def __init__(self, terms: List[int | HPOTerm]): ...
    def add(self, term: int | HPOTerm): ...
    def child_nodes(self) -> HPOSet: ...
    def remove_modifier(self) -> HPOSet: ...
    def replace_obsolete(self) -> HPOSet: ...
    def all_genes(self) -> Set[Gene]: ...
    def omim_diseases(self) -> Set[Omim]: ...
    def information_content(self) -> Dict[str, Any]: ...
    def similarity(self, other: HPOSet, kind: str = "omim", method: str = "graphic", combine: str = "funSimAvg") -> float: ...
    def batch_similarity(self, other: List[HPOSet], kind: str = "omim", method: str = "graphic", combine: str = "funSimAvg") -> List[float]: ...
    def toJSON(self, verbose: bool = False) -> Dict[str, Any]: ...
    def serialize(self) -> str: ...
    def terms(self) -> List[HPOTerm]: ...
    @classmethod
    def from_queries(cls, queries: List[int | str]) -> HPOSet: ...
    @classmethod
    def from_serialized(cls, pickle: str) -> HPOSet: ...
    @classmethod
    def from_gene(cls, gene: Gene) -> HPOSet: ...
    @classmethod
    def from_disease(cls, disease: Omim) -> HPOSet: ...
    def __len__(self) -> int: ...
    def __str__(self) -> str: ...
    def __iter__(self) -> Iterator[HPOTerm]: ...
    def __contains__(self, term: HPOTerm) -> bool: ...


class BasicHPOSet:
    def __init__(self, terms: List[int | HPOTerm]): ...
    def add(self, term: int | HPOTerm): ...
    def child_nodes(self) -> HPOSet: ...
    def remove_modifier(self) -> HPOSet: ...
    def replace_obsolete(self) -> HPOSet: ...
    def all_genes(self) -> Set[Gene]: ...
    def omim_diseases(self) -> Set[Omim]: ...
    def information_content(self) -> Dict[str, Any]: ...
    def similarity(self, other: HPOSet, kind: str = "omim", method: str = "graphic", combine: str = "funSimAvg") -> float: ...
    def batch_similarity(self, other: List[HPOSet], kind: str = "omim", method: str = "graphic", combine: str = "funSimAvg") -> List[float]: ...
    def toJSON(self, verbose: bool = False) -> Dict[str, Any]: ...
    def serialize(self) -> str: ...
    def terms(self) -> List[HPOTerm]: ...
    @classmethod
    def from_queries(cls, queries: List[int | str]) -> HPOSet: ...
    @classmethod
    def from_serialized(cls, pickle: str) -> HPOSet: ...
    @classmethod
    def from_gene(cls, gene: Gene) -> HPOSet: ...
    @classmethod
    def from_disease(cls, disease: Omim) -> HPOSet: ...
    def __len__(self) -> int: ...
    def __str__(self) -> str: ...
    def __iter__(self) -> Iterator[HPOTerm]: ...
    def __contains__(self, term: HPOTerm) -> bool: ...


class Ontology:
    # We're documenting the Ontology as if it were a static method,
    # because it is exposed as a Singleton and not as a class
    genes: Gene
    omim_diseases: Omim
    @staticmethod
    def get_hpo_object(query: str | int) -> HPOTerm: ...
    @staticmethod
    def match(query: str) -> HPOTerm: ...
    @staticmethod
    def path(query1: str | int, query2: str | int) -> Tuple[int, List[HPOTerm], int, int]: ...
    @staticmethod
    def search(query: str) -> List[HPOTerm]: ...
    @staticmethod
    def hpo(id: int) -> HPOTerm: ...
    @staticmethod
    def version() -> str: ...
    @staticmethod
    def __call__(data_folder: str = "", from_obo_file: bool = True): ...
    @staticmethod
    def __len__() -> int: ...
    @staticmethod
    def __repr__() -> int: ...
    @staticmethod
    def __getitem__(id_: int) -> HPOTerm: ...
    @staticmethod
    def __iter__() -> Iterable[HPOTerm]: ...
