from unittest.mock import MagicMock

import pytest


@pytest.fixture
def fixture_magic_mock():
    return MagicMock()
