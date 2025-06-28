from dataclasses import dataclass


@dataclass
class Relic:
    color: str
    effects: tuple[str]

    def __hash__(self):
        return id(self)


@dataclass
class Vessel:
    slot_colors: tuple[str]
