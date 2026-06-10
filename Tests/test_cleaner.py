    
from Scanner import scan
from Cleaner import find_duplicate

def test_find_duplicate(tmp_path):
    # Create two identical files
    f1 = tmp_path / "file1.txt"
    f2 = tmp_path / "file2.txt"
    f1.write_text("same content")
    f2.write_text("same content")
    results = scan(str(tmp_path))
    duplicates = find_duplicate(results)
    assert len(duplicates) == 1    # one duplicate group found

def test_no_duplicates(tmp_path):
    f1 = tmp_path / "file1.txt"
    f2 = tmp_path / "file2.txt"
    f1.write_text("different content")
    f2.write_text("very different content")
    
    results = scan(str(tmp_path))
    duplicates = find_duplicate(results)
    assert len(duplicates) == 0    # no duplicates 