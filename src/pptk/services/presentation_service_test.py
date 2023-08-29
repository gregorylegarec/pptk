import pytest

from .presentation_service import PresentationService
from pptk.models import PresentationSettings


class TestPresentationService:
    @staticmethod
    def test_generate_presentation():
        service = PresentationService()
        result = service.generate_presentation(
            PresentationSettings(number_of_slides=10)
        )
        assert len(result.slides) == 10
        assert result.slides[0].image_path == "foo/bar"
