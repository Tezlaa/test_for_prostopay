import pytest

from tests.testcases.put import put_testdata

from core.hashmap import HashMap


@pytest.fixture
def fulled_hashmap_by_testdata() -> HashMap:
    hashmap = HashMap(len(put_testdata))
    for data in put_testdata:
        hashmap[data[0]] = data[1]
    
    return hashmap


@pytest.mark.parametrize('key, value', put_testdata)
def test_putting_and_getting(key, value):
    hashmap = HashMap()
    hashmap[key] = value
    assert hashmap[key] == value


@pytest.mark.parametrize('key, value', put_testdata)
def test_big_data_search(key, value, fulled_hashmap_by_testdata):
    assert fulled_hashmap_by_testdata[key] == value