import os
import random
import string
from pytest import fixture
from zipfile import ZipFile
from code.code_fixtures import write_zipfile, read_zipfile


@fixture
def fzipfile():
    content_lenght = 50
    content = ''.join(random.choices(string.ascii_lowercase, k=content_lenght))
    fnumber = ''.join(random.choices(string.digits, k=3))
    filename = f'file{fnumber}.zip'

    write_zipfile(filename, content)
    yield filename, content

    os.remove(filename)


def test_writeread_zipfile():
    TESTFILE = 'test.zip'
    TESTCONTENT = 'to jest test'
    write_zipfile(TESTFILE, TESTCONTENT)
    content = read_zipfile(TESTFILE)
    assert TESTCONTENT == content


def test_readwrite_zipfile(fzipfile):
    filename, expected_content = fzipfile
    content = read_zipfile(filename)
    assert content == expected_content


def test_internal_zipfile(fzipfile):
    filename, expected_content = fzipfile
    EXPECTED_LIST = ['internal.txt']
    with ZipFile(filename, 'r') as zipfile:
        assert zipfile.namelist() == EXPECTED_LIST
