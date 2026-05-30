
klantnaam = input("Geef de naam van de klant: ")
aantal = int(input("Geef het aantal producten: "))
prijs_per_stuk = float(input("Geef de prijs per stuk (€): "))

subtotaal = aantal * prijs_per_stuk
btw_bedrag = subtotaal * 0.21
totaal = subtotaal + btw_bedrag

print("\n" + "="*40)
print(f"Factuur voor: {klantnaam}")
print(f"Aantal producten: {aantal}")
print(f"Prijs per stuk:   € {prijs_per_stuk:.2f}")
print("-" * 40)
print(f"Subtotaal:        € {subtotaal:.2f}")
print(f"BTW (21%):        € {btw_bedrag:.2f}")
print(f"TOTAAL:           € {totaal:.2f}")
print("="*40)