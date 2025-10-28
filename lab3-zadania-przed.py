# Zadanie 1
def fizzbuzz(ceiling=100):
    """
    Napisz funkcję iterującą po liczbach całkowitych od 1 do 100 i wypisującą
    je na ekran. Dla liczb podzielnych przez 3 zamiast liczby wypisz "fizz",
    dla liczb podzielnych przez 5 wypisz "buzz", natomiast zamiast
    liczb podzielnych przez 3 i 5 wypisz "fizzbuzz".
    """

    for i in range(ceiling):
        ans = ""
        if i % 3 == 0:
            ans += "fizz"
        if i % 5 == 0:
            ans += "buzz"

        if not ans:
            ans = i

        print(f"{i}: {ans}")


# Zadanie 2
def reverse_list(ls):
    """
    Napisz funkcję, która dla zadanej listy zwróci listę zawierającą
    co trzeci element, w odwróconej kolejności, zaczynając od przedostatniego.
    Przykład: dla listy `[1, 2, 3, 4, 5, 6, 7, 8, 9]` wynikiem będzie `[8, 5, 2]`.
    """
    # return ls[:-2:-1]
    print(ls[-2::-3])


# Zadanie 3
def fibonacci(n=5):
    """
    Napisz funkcję rekurencyjną zwracającą piąty element ciągu Fibonacciego.
    Prześledź działanie tej funkcji, korzystając z debuggera.
    """
    if n == 0: return 0
    if n == 1: return 1
    return fibonacci(n - 1) + fibonacci(n - 2)


# Zadanie 4
def print_receipt():
    """
    Zmodyfikuj funkcję `print_receipt` tak, aby prócz sumowania kwoty 
    wyliczała należny podatek, uwzględniając grupy podatkowe poszczególnych towarów.
    Wskazówka: do mapowania grupy podatkowej na wartość podatku użyj słownika.
    Spodziewany wynik (przy założeniu, że w grupie podatkowej A podatek wynosi 12%,
    w grupie podatkowej B 8%, zaś w grupie podatkowej E 22%):

    ```
    2020-10-27
    1. Bananas	 4.99 B
    2. Oragnes	18.03 B
    3. Milk		 3.15 A
    4. Lollipop	 1.00 E
    -----------------------
    TAX              2.44
    TOTAL:		27.17
    TOTAL+TAX:	29.61
    ```
    """

if __name__ == "__main__":
    # fizzbuzz(40)
    # reverse_list([1, 2, 3, 4, 5, 6, 7, 8, 9])
    print(fibonacci())
    pass
