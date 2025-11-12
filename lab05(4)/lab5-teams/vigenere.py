def encrypt_vigenere(key, plaintext):
    ciphertext = ''
    for letter in plaintext:
        if letter != ' ':
            letter, key = vigenere_letter(key, letter), letter
        ciphertext += letter
    return ciphertext


def decrypt_vigenere(key, ciphertext):
    plaintext = ''
    for letter in ciphertext:
        if letter != ' ':
            letter = key = vigenere_letter(vigenere_reverse_key(key), letter)
        plaintext += letter
    return plaintext


number_of_letters = ord('Z') - ord('A') + 1


def vigenere_reverse_key(key):
    return chr((number_of_letters - (ord(key)-ord('A'))) % number_of_letters + ord('A'))


def vigenere_letter(row_letter, col_letter):
    row = ord(row_letter) - ord('A')
    col = ord(col_letter) - ord('A')
    result = (row + col) % number_of_letters
    return chr(result + ord('A'))


# for row in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
#    s = ''
#    for col in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
#        s = s + vigenere_letter(row, col)
#    print(s)
s = "TO JEST BARDZO TAJNY TEKST"
c = encrypt_vigenere('N', s)
s2 = decrypt_vigenere('N', c)
print(s)
print(c)
print(s2)
