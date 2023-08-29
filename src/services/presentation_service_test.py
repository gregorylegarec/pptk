import pytest

from .presentation_service import PresentationService

class TestPresentationService:
    @staticmethod
    def test_generate_presentation():
        service = PresentationService()
        result = service.generate_presentation()
        assert len(result.slides) == 1
        assert result.slides[0].image_path == "foo/bar"