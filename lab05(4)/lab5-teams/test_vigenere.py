from vigenere import encrypt_vigenere, decrypt_vigenere


def test_encrypt_vigenere_empty():
    assert encrypt_vigenere('K', '') == ''


def test_encrypt_vigenere_spaces():
    assert encrypt_vigenere('K', '   ') == '   '


def test_encrypt_vigenere_one_letter():
    assert encrypt_vigenere('K', 'G') == 'Q'


def test_encrypt_vigenere_text1():
    assert encrypt_vigenere('D', 'ABCDEFGHIJKLMNOPQRSTUVWXYZ') == 'DBDFHJLNPRTVXZBDFHJLNPRTVX'


def test_encrypt_vigenere_test2():
    assert encrypt_vigenere('K', 'TO JEST BARDZO TAJNY TEKST') == 'DH XNWL UBRUCN HTJWL RXOCL'


def test_encrypt_vigenere_test3():
    assert encrypt_vigenere('A', 'SDWLDRAKD DPBQALDUBFHL ADRFF') == 'SVZHOURKN GSQRQLOXVGMS LDUWK'


def test_encrypt_vigenere_test4():
    assert encrypt_vigenere('Z', 'JDLTQM TPTDHYDS    UAHUF HPW') == 'IMOEJC FIIWKFBV    MUHBZ MWL'


def test_dencrypt_vigenere_empty():
    assert decrypt_vigenere('K', '') == ''


def test_dencrypt_vigenere_spaces():
    assert decrypt_vigenere('K', '   ') == '   '


def test_dencrypt_vigenere_one_letter():
    assert decrypt_vigenere('K', 'Q') == 'G'


def test_dencrypt_vigenere_text1():
    assert decrypt_vigenere('D', 'DBDFHJLNPRTVXZBDFHJLNPRTVX') == 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'


def test_dencrypt_vigenere_test2():
    assert decrypt_vigenere('K', 'DH XNWL UBRUCN HTJWL RXOCL') == 'TO JEST BARDZO TAJNY TEKST'


def test_dencrypt_vigenere_test3():
    assert decrypt_vigenere('A', 'SVZHOURKN GSQRQLOXVGMS LDUWK') == 'SDWLDRAKD DPBQALDUBFHL ADRFF'


def test_dencrypt_vigenere_test4():
    assert decrypt_vigenere('Z', 'IMOEJC FIIWKFBV    MUHBZ MWL') == 'JDLTQM TPTDHYDS    UAHUF HPW'
