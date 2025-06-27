from dataclasses import dataclass, field
import uuid

@dataclass
class Relic:
    color: str
    effects: tuple[str]

    def __hash__(self):
        return id(self)


@dataclass
class Vessel:
    slot_colors: tuple[str]
