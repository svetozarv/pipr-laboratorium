# Zadania przed laboratorium 2 - podstawy pythona

## Zadanie 1

1. Uruchom interaktywny interpreter pythona i oblicz iloczyn liczb `3000` i `1e100`.
   Zapisz obliczoną wartość do zmiennej `product`.
2. Sprawdź typ zmiennej `product`.
3. Skonwertuj zmienną `product` do zmiennej całkowitej i zapisz wynik w zmiennej `product_int`.
4. Utwórz krotkę zawierającą na kolejnych pozycjach tekstową reprezentację zmiennej `product`
   oraz tekstową reprezentację zmiennej `product_int`.
5. Oblicz liczbę cyfr składających się na dziesiętną reprezentację liczby ze zmiennej `product_int`.

## Zadanie 2

W celu wykonania zadania utwórz nowy skrypt pythonowy i uruchom go po wykonaniu
poniższych instrukcji. Nie zaleca się wykonywania tego zadania z poziomu interaktywnej
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
