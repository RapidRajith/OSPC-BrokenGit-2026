from taskforge.storage import load_tasks, save_tasks

def test_load_returns_list_for_missing_file(tmp_path):
    assert load_tasks(tmp_path / "not-here.json") == []

def test_save_and_load_tasks(tmp_path):
    file_path = tmp_path / "tasks.json"
    tasks = [{"id": 1, "title": "Test Task", "completed": False, "priority": "medium"}]
    count = save_tasks(tasks, file_path)
    assert count == 1
    loaded = load_tasks(file_path)
    assert loaded == tasks

def test_load_empty_file(tmp_path):
    file_path = tmp_path / "empty.json"
    file_path.write_text("")
    assert load_tasks(file_path) == []

