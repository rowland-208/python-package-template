import pytest

from packagename import example


@pytest.fixture
def data():
    return example.load_data()


def test_load_data(data):
    assert isinstance(data, list)
    item = data[0]
    assert isinstance(item, dict)
    assert "foo" in item
    assert item["foo"] == "bar"


def test_show_lena():
    example.show_lena()
