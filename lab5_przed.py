# Zadanie 1
def subset(int_set: str, length: int):
    """
    Napisać funkcję, która dla podanego ciągu liczb całkowitych znajdzie dowolny spójny podciąg o podanej długości i 
    największej sumie elementów. Napisać testy dla podanej funkcji. Proszę zastanowić się, 
    co funkcja ma zwrócić w przypadku gdy długość szukanego podciągu jest większa
    niż wielkość kolekcji podanej na wejściu.
    """
    if length > len(int_set):
        raise ValueError("Subset cannot be grater than set.")
    if not int_set: return 0

    int_set = sorted(int_set)
    return "".join(int_set[-length:])


# Zadanie 2
def distance(n, p1: tuple[int, int], p2: tuple[int, int]) -> int:
    """
    W grze mamy planszę o rozmiarze `2*N+1` na `2*N+1`. Współrzędne pól (dla wierszy i dla kolumn) są 
    z zakresu od `-N` do `N`. Plansza zawiera więc `(2*N+1) * (2*N+1)` pól.
    Plansza jest zawinięta tak, że pola o współrzędnych: `(-N, X)` i `(N, X)` jak i pola o współrzędnych 
    `(X, -N)` i `(X, N)` dla dowolnego `X` z zakresu `<-N, N>` stykają się ze sobą.

    Napisać funkcję `distance` obliczającą odległość na planszy pomiędzy dwoma punktami zgodnie z metryką miejską.
    Funkcja ma być zgodna z dostarczonymi w pliku `test_distance.py ` testami.
    
    Przy implementacji funkcji proszę dokonać jej dekompozycji na funkcję rozwiązującą prostszy problem i
    dla tej funkcji napisać testy. 

    Proszę założyć, że podawane jako parametry współrzędne mają wartość z zakresu 
    `<-N,N>`. Przekroczenie zakresu wartości współrzędnych nie jest weryfikowane przez dostarczone testy.

    Podpowiedź: mniejszym problemem jest obliczenie odległości dla przypadku jednowymiarowego.

    W metryce miejskiej odległość S między dwoma punktami `A` i `B` est określona wzorem `S = |a1 - b1| + |a2 - b2|`
    gdzie `(a1,a2)` i `(b1,b2)` są współrzędnymi punktów odpowiednio `A` i `B`. 
    Odległość ta jest interpretowana jako długość drogi między punktami A i B, mierzona wzdłuż ulic 
    wyłącznie prostopadłych lub równoległych.
    """    
    x1, y1 = p1
    x2, y2 = p2
    if min(x1, x2, y1, y2) < n or max(x1, x2, y1, y2) > n:
        raise ValueError("Coordinates must be in range <N, N>.")

    city_dist = count_city_dist(p1, p2)
    dist_though_edge = compute_1d_dist(n, x1, x2) + compute_1d_dist(n, y1, y2)
    
    if city_dist <= dist_though_edge:
        return city_dist
    return dist_though_edge


def compute_1d_dist(n, coord_of_1: int, coord_of_2: int) -> int:
    """
    Computes distence between coords through edges 
    (distance from first point(coord) to edge + distance from second(coord) point to the edge)
    """
    dist_on_edge = (n - coord_of_1) + (n - coord_of_2)
    return dist_on_edge


def count_city_dist(p1: tuple[int, int], p2: tuple[int, int]) -> int:
    x1, y1 = p1
    x2, y2 = p2
    return abs(x1 - x2) + abs(y1 - y2)

# Zadanie 3
def check_input_in2():
    """   
    Zmodyfikować funkcję z zadania 2 tak żeby w przypadku podania wartości współrzędnej o wartości spoza
    zakresu `<-N,N>` zgłaszała błąd przez zgłoszenie wyjątku - proszę wybrać odpowiedni typ wyjątku
    z listy standardowych wyjątków. 
    Dodatkowo proszę dopisać testy sprawdzające zgłaszanie tego wyjątku
    w przypadku przekroczenia dopuszczalnego zakresu wartości współrzędnych.
    """
    pass


