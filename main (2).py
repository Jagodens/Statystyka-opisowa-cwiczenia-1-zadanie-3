import matplotlib.pyplot as plt
import numpy as np

# Dane z Zadania 3 (Lotniska w Ameryce Północnej - ruch pasażerski w mln)[cite: 52]
airports = [
    "Boston Logan",
    "Charlotte Douglas",
    "Chicago O'Hare",
    "Dallas/Ft. Worth",
    "Denver",
    "Detroit Metropolitan",
    "Hartsfield-Jackson Atlanta",
    "Houston George Bush",
    "Las Vegas McCarran",
    "Los Angeles",
    "Miami",
    "Minneapolis/St. Paul",
    "New York John F. Kennedy",
    "Newark Liberty",
    "Orlando",
    "Philadelphia",
    "Phoenix Sky Harbor",
    "San Francisco",
    "Seattle-Tacoma",
    "Toronto Pearson",
]

traffic = np.array(
    [
        36.3,
        44.4,
        78.0,
        65.7,
        58.3,
        34.4,
        104.2,
        41.6,
        47.5,
        80.9,
        44.6,
        37.4,
        59.1,
        40.6,
        41.9,
        36.4,
        43.3,
        53.1,
        45.7,
        44.3,
    ]
)

# a. Najbardziej i najmniej zatłoczone lotnisko[cite: 52]
max_idx = np.argmax(traffic)
min_idx = np.argmin(traffic)

print("--- Podpunkt a: Ekstrema ruchu ---")
print(
    f"Najbardziej zatłoczone: {airports[max_idx]} ({traffic[max_idx]} mln"
    " pasażerów)"
)
print(
    f"Najmniej zatłoczone: {airports[min_idx]} ({traffic[min_idx]} mln"
    f" pasażerów)\n"
)

# b. Szereg rozdzielczy (szerokość klasy = 10, od 30 do 110)[cite: 52]
bins = [
    (30, 39.9),
    (40, 49.9),
    (50, 59.9),
    (60, 69.9),
    (70, 79.9),
    (80, 89.9),
    (90, 99.9),
    (100, 109.9),
]

print("--- Podpunkt b: Szereg rozdzielczy ---")
print(f"{'Przedział (mln)':<18} | {'Liczba lotnisk (częstość)'}")
print("-" * 45)

counts = []
for low, high in bins:
  if high == 109.9:
    count = np.sum((traffic >= low) & (traffic <= high))
  else:
    count = np.sum((traffic >= low) & (traffic < high + 0.1))
  counts.append(count)
  print(f"{low} - {high:<12} | {count}")

print(f"{'Suma':<18} | {sum(counts)}\n")

# c. Generowanie i zapis histogramu[cite: 52]
plt.figure(figsize=(9, 5))
bin_edges = np.arange(30, 111, 10)
plt.hist(
    traffic,
    bins=bin_edges,
    color="green",
    edgecolor="black",
    alpha=0.75,
    align="mid",
)

plt.title(
    "Histogram ruchu pasażerskiego na lotniskach w Ameryce Północnej (2018)"
)
plt.xlabel("Liczba pasażerów (miliony)")
plt.ylabel("Liczba lotnisk (częstość)")
plt.xticks(bin_edges)
plt.grid(True, linestyle="--", alpha=0.5)

# Zapis wykresu do pliku graficznego
plt.savefig("histogram_lotniska.png", dpi=300)
print("Histogram został wygenerowany i zapisany jako 'histogram_lotniska.png'.")

plt.show()