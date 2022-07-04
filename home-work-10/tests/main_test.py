from unittest.mock import patch, call, MagicMock

import pytest

from utils.task_1 import write_to_file


@pytest.mark.parametrize('test_filename, test_phrase',
                         [
                             ('../file_1.txt', 'To be, or not to be, that is the question:'),
                             ('../file_2.txt', 'Whether it is nobler in the mind to suffer'),
                             ('../file_3.txt', 'The slings and arrows of outrageous fortune')
                          ]
                         )
def test_write_to_file(test_filename, test_phrase):
    with patch('builtins.open', MagicMock()) as open_mock:
        write_to_file(test_filename, test_phrase)
        open_mock.assert_called()
        open_mock.assert_has_calls(calls=[call(test_filename, 'w')])
        handle = open_mock()
        handle.write.assert_called_with(test_phrase)


@pytest.mark.xfail(raises=TypeError)
def test_type_error(fixture_magic_mock):
    with pytest.raises(TypeError):
        write_to_file("test.txt", fixture_magic_mock)


def test_write_to_file_with_mock(fixture_magic_mock):
    with patch('builtins.open', fixture_magic_mock) as open_mock:
        test_filename = 'test_filename.txt'
        test_phrase = 'test_phrase'
        write_to_file(test_filename, test_phrase)
        open_mock.assert_called()
        open_mock.assert_has_calls(calls=[call(test_filename, 'w')])

