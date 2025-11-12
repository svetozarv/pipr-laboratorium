# ---------------- w klasie ----------------
def add(a, b):
    return a+b

def pow(num, p):
    return num ** p

# Zadanie 1
def zadanie1():
    """
    Zaimplementuj funkcję, która przyjmuje jedną wartość liczbową
    i zwraca tę wartość podniesioną do 3-ciej potęgi.

    Następnie wywołaj i wypisz na ekran wynik działania funkcji dla
    wartości: 0, 1, -3, 2e3.
    """
    nums = [0, 1, -3, 2e3]
    for i in nums:
        print(pow(i, 3))


# Zadanie 2
def calc_polinomial(x, params: list):
    """
    #TODO
    Zaimplementuj funkcję obliczającą wartość wielomianu ~~drugiego~~ dowolnego stopnia
    o parametrach zadanych w jej argumentach. Przetestuj ją dla różnych argumentów.
    
    - params - list with cooficients [a, b, c, d, ...]
    """

    answer = 0
    i = 0
    curr_pow = len(params) - 1

    while curr_pow >= 0:
        answer += x**curr_pow * params[i]
        curr_pow -= 1
        i += 1

    print(answer)


def calc_polinomial_test():
    calc_polinomial(2, [6, 7, 2, 16])
    calc_polinomial(4, [67])
    calc_polinomial(6, [1, 2])


# Zadanie 3
def print_student_assignment_time(student_name, assign_num, time_ms):
    """
    Napisz funkcję, która przyjmuje parametr określający imię, numer zadania oraz
    czas wykonania zadania wyrażony w milisekundach, a następnie generuje i zwraca
    tekst informujący o wykonaniu przez podaną osobę danego zadania w określonym czasie.
    Wyraź czas w sekundach określonych z dokładnością do trzeciego miejsca po przecinku.

    Przykład:

    > Adam wykonał(a) zadanie nr 1 w 123.052s.

    Użyj jej do napisania programu informującego o ukończeniu przez Ciebie
    tego zadania (podaj zmyślony czas wykonania, np. 555111ms).
    """
    print(f"Student {student_name} has completed task No.{assign_num} in {int(time_ms)/1000:0.03f}s")

# ---------------- w domu, do poćwiczenia ----------------

# Zadanie 4
def perpendicular_bisector_point(point1: tuple[int], point2: tuple[int]):
    """
    Napisz funkcję, która akceptuje dwa punkty w przestrzeni dwuwymiarowej i
    zwraca punkt znajdujący się na symetralnej odcinka stworzonego przez argumenty wejściowe.
    Punkty reprezentuj za pomocą dwuelementowej krotki.
    """
    x_mean = (point1[0] + point2[0]) / 2
    y_mean = (point1[1] + point2[1]) / 2

    print(x_mean, y_mean)


# Zadanie 5
def to_binary(num: int):
    """
    Napisz funkcję, która zwraca liczbę cyfr dwójkowej reprezentacji liczby podanej
    w argumencie.
    """
    print(bin(num))


# Zadanie 6
def compute_mean(nums: tuple[int]):
    """
    Napisz funkcje, które obliczają przedział wartości oraz średnią wartość liczb
    podanych w krotce. Możesz założyć, że krotka zawiera co najmniej jeden element.
    """
    
    mean = 0
    for num in nums: 
        mean += num
    
    print(f"średnia wartość liczb: {mean / len(nums)}")
    print(f"przedział wartości: [{min(nums)}, {max(nums)}]")


# Zadanie 7
def make_table(width, height, length):
    """
    Napisz funkcję, która przyjmuje szerokość, wysokość oraz długość obiektu,
    a następnie prezentuje je za pomocą tabeli. Wymiary wypisz jako liczby
    dziesiętne z dokładnością do 3-go miejsca po przecinku.
    
    Przykład:
    ```
    Wymiar    |  Wartość
    ----------------------
    Szerokość | 2434.400
    Wysokość  |   35.350
    Długość   |    0.202
    ```
    
    Zadbaj o minimalną szerokość obu kolumn tabeli. Zapewnij margines o szerokości
    jednego odstępu. Tekst powinien być wyrównany do zewnętrznej strony tabeli
    (do lewej w lewej kolumnie i do prawej w prawej kolumnie).
    """
    ocw1 = optimal_column_width("Wymiar", ("Szerokość", "Wysokość", "Długość"))
    ocw2 = optimal_column_width("Wartość", (width, height, length))
    
    # format_row(("Wymiar", ocw1), ("Wartość", ocw2))
    print(f"{'Wymiar':{ocw1}}|{'Wartość':>{ocw2}}")

    print("-" * (ocw1 + ocw2 + 2))
    format_row(("Szerokość", ocw1), (width, ocw2))
    format_row(("Wysokość", ocw1), (height, ocw2))
    format_row(("Długość", ocw1), (length, ocw2))


def format_row(cont1: tuple[str, float], cont2: tuple[str, float]):
    text1, width1 = cont1
    text2, width2 = cont2
    text2 = float(text2)
    width1 = int(width1)
    width2 = int(width2)
    row = f"{text1:{width1}}|{text2:>{width2}.3f}"
    print(row)


def optimal_column_width(column_name: str, dimensions: tuple[str]):
    max_len_elem = 0
    for elem in dimensions:
        elem = str(elem)
        if len(elem) > max_len_elem:
            max_len_elem = len(elem)
    
    if len(column_name) > max_len_elem:
        max_len_elem = len(column_name)

    return max_len_elem + 2


# Zadanie 8
def compute_binominal_roots(a, b, c):
    """
    Napisz funkcję, która oblicza pierwiastki równania kwadratowego o zadanych
    parametrach.
    """
    import math

    roots = []
    delta = b**2 - 4*a*c
    root1 = (-b - math.sqrt(delta)) / 2*a
    root2 = (-b + math.sqrt(delta)) / 2*a
    roots.append(root1)
    if root1 != root2: roots.append(root2) 

    print(roots)


if __name__ == "__main__":
    # calc_polinomial_test()
    # print_student_assignment_time("Ja", "3", "123052")
    # perpendicular_bisector_point((3, 0), (0, 3))
    # to_binary(8)
    # compute_mean((1, 2, 3, 4, 5, 20))
    # compute_binominal_roots(1, 6, -18)
    # compute_binominal_roots(1, -8, 16)
    # make_table(2434.400, 35.350, 0.202)
    make_table("70", "3", "2")
    make_table("2434.400", "35.350", "0.202")