from lab5_przed import *
import pytest


def test_subset():
    assert subset("123456789", 3) == "789"
    assert subset("94385744444", 3) == "789"
    assert subset("94385744444", 1) == "9"
    assert subset("12345", 5) == "12345"


def test_subset_corner():
    assert subset("", 0) == 0


def test_distance():
    with pytest.raises(ValueError):
        distance(5, (6, 3), (2, 1))


def test_count_elements_above_average_collection():
    assert count_elements_above_average_collection([[1, 2, 3], [5, 6, 7], [], [3, 4, 5], ["12a", 1, 4]]) == [1, 1, "DZIELENIE PRZEZ ZERO", 1, "ZŁA WARTOŚĆ" ]


# Zadanie 4
def test_decrypt_vigenere():
    """
    Napisać testy dla funkcji szyfrującej tekst (tylko duże litery alfabetu łacińskiego i spacja) za pomocą
    oryginalnego szyfru Vigenère’a z autokluczem (jako klucz podawana jest jedna litera) -
    [link do strony opisującej szyfr Vigenère’a](https://pl.wikipedia.org/wiki/Szyfr_Vigen%C3%A8re%E2%80%99a).
    Proszę zastanowić się jakie będą przypadki graniczne oraz niepoprawne dane.

    Napisane testy będą wykorzystane w kolejnych zadaniach.
    """
    assert decrypt_vigenere()


def test_encrypt_vigenere():
    pass
