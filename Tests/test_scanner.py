'''Test scan feature:'''

from Scanner import scan
import pytest

def test_scan_valid_folder(tmp_path):
    #Create a temporary file
    f = tmp_path / "test.txt"
    f.write_text("hello")

    results = scan(str(tmp_path))
    assert len(results) == 1
    assert results[0]["name"] == "test.txt"
    assert results[0]["extension"] == ".txt"

def test_scan_invalid_folder():
    with pytest.raises(ValueError):
        scan("D:/nonexist/folder")

def test_scan_skips_hidden(tmp_path):
    #Hidden file
    hidden = tmp_path /  ".hidden"
    hidden.write_text("normal")
    #Normal file
    normal = tmp_path / "normal.txt"
    normal.write_text("Hello")

    results = scan(str(tmp_path))
    assert len(results) == 1
    assert results[0]["name"] == "normal.txt"

    '''Command line to test: py -m pytest Tests/test_scanner.py'''