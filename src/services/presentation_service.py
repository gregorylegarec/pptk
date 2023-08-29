from dataclasses import dataclass

from models import Presentation, Slide

@dataclass
class PresentationService:
    def generate_presentation(self) -> Presentation:
        return Presentation(slides=[Slide(image_path="foo/bar")])