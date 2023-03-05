import abc
import typing

RenderType = typing.TypeVar("RenderType")
EventsType = typing.TypeVar("EventsType")


class RuntimeLoop:
    @abc.abstractmethod
    def events(self, render: EventsType): ...

    @abc.abstractmethod
    def update(self): ...

    @abc.abstractmethod
    def render(self, render: RenderType): ...
