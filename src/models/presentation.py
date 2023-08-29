from dataclasses import dataclass
from typing import List

from .slide import Slide

@dataclass
class Presentation:
    slides: List[Slide]
    