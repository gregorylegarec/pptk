from dataclasses import dataclass

from pptk.models import Presentation, PresentationSettings, Slide


@dataclass
class PresentationService:
    def generate_presentation(self, settings: PresentationSettings) -> Presentation:
        return Presentation(
            slides=[
                Slide(image_path="foo/bar"),
                Slide(image_path="foo/bar"),
                Slide(image_path="foo/bar"),
                Slide(image_path="foo/bar"),
                Slide(image_path="foo/bar"),
                Slide(image_path="foo/bar"),
                Slide(image_path="foo/bar"),
                Slide(image_path="foo/bar"),
                Slide(image_path="foo/bar"),
                Slide(image_path="foo/bar"),
            ]
        )
