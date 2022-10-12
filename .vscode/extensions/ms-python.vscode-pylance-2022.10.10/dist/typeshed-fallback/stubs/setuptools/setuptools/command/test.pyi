from _typeshed import Self
from collections.abc import Callable
from types import ModuleType
from typing import Any, Generic, TypeVar, overload
from unittest import TestLoader, TestSuite

from setuptools import Command

_T = TypeVar("_T")

class ScanningLoader(TestLoader):
    def __init__(self) -> None: ...
    def loadTestsFromModule(self, module: ModuleType, pattern: Any | None = ...) -> list[TestSuite]: ...  # type: ignore[override]

class NonDataProperty(Generic[_T]):
    fget: Callable[..., _T]
    def __init__(self, fget: Callable[..., _T]) -> None: ...
    @overload
    def __get__(self: Self, obj: None, objtype: object = ...) -> Self: ...
    @overload
    def __get__(self, obj: Any, objtype: object = ...) -> _T: ...

class test(Command):
    description: str
    user_options: Any
    test_suite: Any
    test_module: Any
    test_loader: Any
    test_runner: Any
    def initialize_options(self) -> None: ...
    def finalize_options(self) -> None: ...
    @NonDataProperty
    def test_args(self) -> list[str]: ...
    def with_project_on_sys_path(self, func) -> None: ...
    def project_on_sys_path(self, include_dists=...): ...
    @staticmethod
    def paths_on_pythonpath(paths) -> None: ...
    @staticmethod
    def install_dists(dist): ...
    def run(self) -> None: ...
    def run_tests(self) -> None: ...
