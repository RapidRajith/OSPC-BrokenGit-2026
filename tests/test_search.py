import pytest
from taskforge.search import search_tasks

def test_exact_case_search():
    tasks = [{"id": 1, "title": "Learn Python"}]
    assert len(search_tasks(tasks, "Python")) == 1

def test_case_insensitive_search():
    tasks = [{"id": 1, "title": "Learn Git"}, {"id": 2, "title": "Write Code"}]
    results = search_tasks(tasks, "git")
    assert len(results) == 1
    assert results[0]["id"] == 1

def test_search_invalid_query_type():
    with pytest.raises(ValueError, match="Search query must be text"):
        search_tasks([], 123)

