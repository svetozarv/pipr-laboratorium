# Zadanie 1
def fizzbuzz(ceiling=100):
    """
    Napisz funkcję iterującą po liczbach całkowitych od 1 do 100 i wypisującą je na ekran. 
    Dla liczb podzielnych przez 3 zamiast liczby wypisz "fizz", dla liczb podzielnych przez 5 wypisz "buzz", 
    natomiast zamiast liczb podzielnych przez 3 i 5 wypisz "fizzbuzz". 
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


if __name__ == "__main__":
    fizzbuzz(40)