import dataclasses


@dataclasses.dataclass
class TextInfo:
    curx: int
    cury: int
    attribute: int
    normattribute: int
    screenwidth: int
    screenheight: int


@dataclasses.dataclass
class CharInfo:
    letter: chr
    attr: int
