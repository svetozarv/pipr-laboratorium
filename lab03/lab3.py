# 1. Napisz funkcję, która wypisuje z pierwszej listy imiona i nazwiska
# wszystkich adminów, po jednym adminie na linijkę.

# 2. Napisz funkcję, która sprawdza, czy w drugiej strukturze jest
# Ervin Howell i czy nie ma Johna Smitha.

# 3.Napisz funkcję, która zwróci listę długości geograficznych
# każdego z adminów.

admin_names = [
    "Leanne Graham",
    "Ervin Howell",
    "Clementine Bauch",
    "Patricia Lebsack",
    "Chelsey Dietrich",
    "Mrs. Dennis Schulist",
    "Kurtis Weissnat",
    "Nicholas Runolfsdottir V",
    "Glenna Reichert",
    "Clementina DuBuque",
]

admin_sites = {
    "Chelsey Dietrich": "demarco.info",
    "Clementina DuBuque": "ambrose.net",
    "Clementine Bauch": "ramiro.info",
    "Ervin Howell": "anastasia.net",
    "Glenna Reichert": "conrad.com",
    "Kurtis Weissnat": "elvis.io",
    "Leanne Graham": "hildegard.org",
    "Mrs. Dennis Schulist": "ola.org",
    "Nicholas Runolfsdottir V": "jacynthe.com",
    "Patricia Lebsack": "kale.biz",
}

admins_min = [
    {"Leanne Graham": "hildegard.org"},
    {"Ervin Howell": "anastasia.net"},
    {"Clementine Bauch": "ramiro.info"},
    {"Patricia Lebsack": "kale.biz"},
    {"Chelsey Dietrich": "demarco.info"},
    {"Mrs. Dennis Schulist": "ola.org"},
    {"Kurtis Weissnat": "elvis.io"},
    {"Nicholas Runolfsdottir V": "jacynthe.com"},
    {"Glenna Reichert": "conrad.com"},
    {"Clementina DuBuque": "ambrose.net"},
]

admins_full = [
    {
        "name": "Leanne Graham",
        "website": "hildegard.org",
        "address": {
            "street": "Kulas Light",
            "suite": "Apt. 556",
            "city": "Gwenborough",
            "zipcode": "92998-3874",
            "geo": {"lat": "-37.3159", "lng": "81.1496"},
        },
    },
    {
        "name": "Ervin Howell",
        "website": "anastasia.net",
        "address": {
            "street": "Victor Plains",
            "suite": "Suite 879",
            "city": "Wisokyburgh",
            "zipcode": "90566-7771",
            "geo": {"lat": "-43.9509", "lng": "-34.4618"},
        },
    },
    {
        "name": "Clementine Bauch",
        "website": "ramiro.info",
        "address": {
            "street": "Douglas Extension",
            "suite": "Suite 847",
            "city": "McKenziehaven",
            "zipcode": "59590-4157",
            "geo": {"lat": "-68.6102", "lng": "-47.0653"},
        },
    },
    {
        "name": "Patricia Lebsack",
        "website": "kale.biz",
        "address": {
            "street": "Hoeger Mall",
            "suite": "Apt. 692",
            "city": "South Elvis",
            "zipcode": "53919-4257",
            "geo": {"lat": "29.4572", "lng": "-164.2990"},
        },
    },
    {
        "name": "Chelsey Dietrich",
        "website": "demarco.info",
        "address": {
            "street": "Skiles Walks",
            "suite": "Suite 351",
            "city": "Roscoeview",
            "zipcode": "33263",
            "geo": {"lat": "-31.8129", "lng": "62.5342"},
        },
    },
    {
        "name": "Mrs. Dennis Schulist",
        "website": "ola.org",
        "address": {
            "street": "Norberto Crossing",
            "suite": "Apt. 950",
            "city": "South Christy",
            "zipcode": "23505-1337",
            "geo": {"lat": "-71.4197", "lng": "71.7478"},
        },
    },
    {
        "name": "Kurtis Weissnat",
        "website": "elvis.io",
        "address": {
            "street": "Rex Trail",
            "suite": "Suite 280",
            "city": "Howemouth",
            "zipcode": "58804-1099",
            "geo": {"lat": "24.8918", "lng": "21.8984"},
        },
    },
    {
        "name": "Nicholas Runolfsdottir V",
        "website": "jacynthe.com",
        "address": {
            "street": "Ellsworth Summit",
            "suite": "Suite 729",
            "city": "Aliyaview",
            "zipcode": "45169",
            "geo": {"lat": "-14.3990", "lng": "-120.7677"},
        },
    },
    {
        "name": "Glenna Reichert",
        "website": "conrad.com",
        "address": {
            "street": "Dayna Park",
            "suite": "Suite 449",
            "city": "Bartholomebury",
            "zipcode": "76495-3109",
            "geo": {"lat": "24.6463", "lng": "-168.8889"},
        },
    },
    {
        "name": "Clementina DuBuque",
        "website": "ambrose.net",
        "address": {
            "street": "Kattie Turnpike",
            "suite": "Suite 198",
            "city": "Lebsackbury",
            "zipcode": "31428-2261",
            "geo": {"lat": "-38.2386", "lng": "57.2232"},
        },
    },
]


# Zadanie 1
def count_chars(word: str) -> dict:
    """
    Napisz funkcję, która jako parametr przyjmuje wyraz i tworzy słownik, gdzie kluczami są litery,
    zaś wartościami liczba ich wystąpień w danym słowie. Przykład: dla słowa "kukułka"
    funkcja powinna zwrócić: `{'k': 3, 'u': 2, 'ł': 1, 'a': 1}`.
    """
    mydict = {}
    for char in word:
        mydict[char] = word.count(char)

    return mydict


# Zadanie 2
def filter_words(phrase: str, filter: tuple[str, int]):
    """
    Napisz funkcję, która jako parametry przyjmuje napis, oraz krotkę z literą i jej
    częstością. Funkcja powinna odfiltrować z napisu słowa (przyjmujemy, że słowa oddzielone
    są od siebie spacją), które zawierają więcej lub tyle samo wystąpień podanej litery w stosunku
    do zadanej częstości. 
    
    Przykładowe argumenty:
        "Alice in wonderland went into a deep coma.", ("e", 2)
    Przykładowy rezultat działania:
        "Alice in wonderland went into a coma."

    Podpowiedź: [str.split]
    """
    filter_letter, filter_letter_count = filter
    answer = phrase
 
    for word in phrase.split():
        if count_chars(word).get(filter_letter, 0) >= filter_letter_count:
            answer = answer.replace(word, "")
    
    return " ".join(answer.split())


# -------------------- w domu --------------------
# Zadanie 1
def count_symbols(matrix: list[list[str]]) -> dict:
    """
    Napisz funkcję `count_symbols` zliczającą wystąpienia poszczególnych symboli w tablicy dwuwymiarowej
    (przekazywanej jako argument wywołania). Jako wynik wywołania zwróć słownik, gdzie kluczami są poszczególne symbole
    występujące w tablicy wejściowej, zaś wartościami - liczba ich wystąpień.

    Można założyć, że jedynymi symbolami występującymi w tablicy są małe i wielkie litery alfabetu łacińskiego.

    Przykład: dla poniższej tablicy
    ```
    [['a', 'c', 'o'],
     ['a', 'a', 'c'],
     ['d', 'o', 'O'],
     ['c', 'b', 'a']]
    ```
    rezultatem powinien być następujący słownik: `{'a': 4, 'c': 3, 'o': 2, 'd': 1, 'O': 1, 'b': 1}`
    """
    chars_seq = ""
    for row in matrix:
        chars_seq += "".join(row)
    print(count_chars(chars_seq))


# Zadanie 2
num_to_word = {
    1: 'one',
    2: 'two',
    3: 'three',
    4: 'four',
    5: 'five',
    6: 'six',
    7: 'seven',
    8: 'eight',
    9: 'nine',
    10: 'ten',
    11: 'eleven',
    12: 'twelve',
    13: 'thirteen',
    14: 'fourteen',
    15: 'quarter',  # Obsługuje 15 minut (past) i 45 minut (to)
    16: 'sixteen',
    17: 'seventeen',
    18: 'eighteen',
    19: 'nineteen',
    20: 'twenty',
    21: 'twenty one',
    22: 'twenty two',
    23: 'twenty three', # Jak w przykładzie (6, 37) -> 23 minuty do
    24: 'twenty four',
    25: 'twenty five',
    26: 'twenty six',
    27: 'twenty seven',
    28: 'twenty eight',
    29: 'twenty nine',
    30: 'half'       # Obsługuje 30 minut
}


def time_description(hours: int, minutes: int) -> str:
    """
    Napisz funkcję `time_description`, która przyjmuje jako argumenty dwie liczby całkowite oznaczające liczbę godzin i 
    liczbę minut, i zwraca napis odpowiadający słownemu opisowi godziny w języku angielskim.

    Wskazówki: jeśli liczba minut wynosi zero, użyj słowa `o' clock`. Jeśli liczba minut mieści się pomiędzy 1 a 30,
    użyj `past`. Jeśli liczba minut jest większa niż 30, użyj `to`. Do mapowania liczb na słowa wykorzystaj słownik.

    Uwaga! Godziny podawane są wyłącznie w systemie 12-godzinnym. Podanie błędnej godziny bądź minuty powinno 
    skutkować komunikatem `Incorrect input data!`.

    Przykłady:
    - dla `time_description(8, 15)` zwraca `quarter past eight`
    - dla `time_description(11, 13)` zwraca `thirteen minutes past eleven`
    - dla `time_description(12, 30)` zwraca `half past twelve`
    - dla `time_description(6, 37)` zwraca `twenty three minutes to seven`
    - dla `time_description(3, 45)` zwraca `quarter to four`
    - dla `time_description(15, 5)` zwraca `Incorrect input data!`
    """

    # check input
    if hours > 12 or minutes > 60:
        return ValueError("Incorrect input data!")
    
    if minutes == 0:
        return f"{num_to_word[hours]} o'clock"
    if minutes <= 30:
        return f"{num_to_word[minutes]} past {num_to_word[hours]}"
    if minutes > 30:
        return f"{num_to_word[60-minutes]} to {num_to_word[hours+1]}"


if __name__ == "__main__":
    # print(filter_words("Alice in wonderland went into a deep coma.", ("e", 2)))
    # print(filter_words("Alice in wonderland went into a deep eeee coma.", ("e", 2)))
    
    # char_table = [
    #     ['a', 'c', 'o'],
    #     ['a', 'a', 'c'],
    #     ['d', 'o', 'O'],
    #     ['c', 'b', 'a']
    # ]
    # count_symbols(char_table)
    
    # print(time_description(8, 15))
    # print(time_description(11, 13))
    # print(time_description(12, 30))
    # print(time_description(6, 37))
    # print(time_description(3, 45))
    # print(time_description(15, 5))
    count_chars("kukułka")
