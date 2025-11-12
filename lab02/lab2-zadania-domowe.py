
# Zadanie 2 przed
def generate_filename(id: str):
    """
    W celu wykonania zadania utwórz nowy skrypt pythonowy i uruchom go po wykonaniu
    poniższych instrukcji. Nie zaleca się wykonywania tego zadania z poziomu interaktywnej
    powłoki Pythona!

    Zaimplementuj funkcję `generate_filename`, która przyjmuje jeden parametr `id`
    będący całkowitoliczbowym identyfikatorem i zwraca nazwę pliku
    w formacie `data_<id>.txt`. Część nazwy dotycząca identyfikatora powinna być
    dopełniona wiodącymi zerami do długości 4 jak w przykładzie poniżej.

    ```
    id   -> data_<id>.txt
    ---------------------
    0    -> data_0000.txt
    1    -> data_0001.txt
    23   -> data_0023.txt
    400  -> data_0400.txt
    1001 -> data_1001.txt
    ```

    Następnie wywołaj funkcję dla podanych w przykładzie wartości i wypisz każdy
    z rezultatów. Sprawdź czy otrzymane wartości pokrywają się z podanymi w przykładzie.
    """

    def format_filename(id: str):
        return f"data_{id:0004}.txt"

    for i in range(2000):
        if i % 17 == 0:
            print(format_filename(i))


# Zadanie domowe 1
def common_line_segments_part(seg1: tuple[int], seg2: tuple[int]) -> tuple:
    """
    Napisz funkcję, która przyjmuje dwa odcinki (w przestrzeni jednowymiarowej)
    i zwraca odcinek będący ich częścią wspólną. Odcinki reprezentuj za pomocą
    dwuelementowej krotki. Możesz założyć, że podane odcinki zawsze będą
    zawierały część wspólną.
    """
    seg1 = sorted(seg1)
    seg2 = sorted(seg2)
    
    # x - the beginning of a segment, y - the end coordinate
    x1, x2 = seg1
    y1, y2 = seg2

    # check if one contains the other entirely
    if x1 < y1 and y2 < x2:
        return (y1, y2)
    
    # check if they have a common part
    if x1 < y1 <= x2 and y1 <= x2 < y2:
        return (y1, x2)

    # they do not overlap
    if x2 < y1:
        return (None, None)
    
    # switch sides #TODO
    common_line_segments_part(seg2, seg1)


# Zadanie domowe 2

def create_frame(text: str, w: int):
    """
    Napisz funkcję, która przyjmuje tekst wiadomości oraz szerokość, a następnie
    wypisuje wiadomość w ramce ułożonej ze znaków `*` o zadanej szerokości
    i wysokości 5.
    Możesz założyć, że zadana szerokość będzie wystarczająca dla zadanego tekstu.

    ```
    Przykład dla ramki o szerokości 11:
    ***********
    *         *
    *  HELLO  *
    *         *
    ***********
    ```
    """
    height = 5
    middle = 5 // 2 - 1
    ans = ""
    ans += "*" * w + "\n"

    for i in range(height-2):
        if i == middle:
            ans += "*" + text.center(w-2) + "*\n"
        else:
            ans += "*" + " " * (w - 2) + "*\n"

    ans += "*" * w + "\n"

    print(ans)


# Zadanie domowe 3
def fill_rectangle(w, h):
    """
    Napisz funkcję, która przyjmuje wysokość i szerokość prostokąta, a następnie
    wypełnia go, wypisując znaki `#` na ekran.

    Przykład dla prostokąta o wymiarach 6x3:
    ```
    ######
    ######
    ######
    ```
    """
    ans = ""
    w = int(w)
    h = int(h)

    for i in range(h):
        ans += f"{'#' * w}\n"
    
    print(ans)
    # return ans


if __name__ == "__main__":
    # create_frame("hello", 11)
    # fill_rectangle(5,3)
    print(common_line_segments_part((10, 23), (13, 17)))
    print(common_line_segments_part((10, 17), (13, 23)))
    print(common_line_segments_part((10, 13), (17, 23)))
    print(common_line_segments_part((10, 17), (17, 23)))
