def brute_force(k, n, values, weights):
    best_value = 0
    best_vector = []

    for i in range(2 ** n):  # 2**n : całkowita liczba możliwych kombinacji przedmiotów
        current_vector = []
        current_value = 0
        current_weight = 0

        # Konwertowanie liczby 'i' na wektor bitów
        for j in range(n):
            if i & (1 << j):
                current_vector.append(1)
                current_value += values[j]
                current_weight += weights[j]
            else:
                current_vector.append(0)

        # Sprawdzanie czy aktualny wektor jest lepszy od dotychczasowego najlepszego
        if current_weight <= k and current_value > best_value:
            best_value = current_value
            best_vector = current_vector

        # Wypisywanie informacji o postępie
        print("Iteracja:", i + 1, "Najlepsza wartość:", best_value, "Najlepszy wektor:", best_vector)

    return best_vector


# Odczytywanie danych z pliku
def read_input_file(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
        k, n = map(int, lines[0].split())
        values = list(map(int, lines[1].split(',')))
        weights = list(map(int, lines[2].split(',')))
        return k, n, values, weights


# Przykładowe użycie
file_path = "plecaki/plecak5.txt"
k, n, values, weights = read_input_file(file_path)
best_vector = brute_force(k, n, values, weights)
print("Najlepszy wektor:", best_vector)
