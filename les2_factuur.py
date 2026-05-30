print("=== Factuur Generator ===\n")
klantnaam = input("Geef de naam van de klant: ")
aantal = int(input("Geef het aantal producten: "))
if aantal < 0:
    print("FOUT: Aantal producten mag niet negatief zijn!")
print("\nKies BTW-percentage:")
print("1. 6%")
print("2. 12%")
print("3. 21%")
keuze = input("Maak een keuze (1-3): ")
if keuze == "1":
    btw_percentage = 0.06
elif keuze == "2":
    btw_percentage = 0.12
else:
    btw_percentage = 0.21

prijs_per_stuk = float(input("\nGeef de prijs per stuk (€): "))

subtotaal = aantal * prijs_per_stuk
btw_bedrag = subtotaal * btw_percentage
totaal = subtotaal + btw_bedrag

print("\n" + "="*45)
print(f"Factuur voor: {klantnaam}")
print(f"Aantal producten: {aantal}")
print(f"Prijs per stuk:   € {prijs_per_stuk:.2f}")
print(f"BTW-percentage:   {btw_percentage*100:.0f}%")
print("-" * 45)
print(f"Subtotaal:        € {subtotaal:.2f}")
print(f"BTW:              € {btw_bedrag:.2f}")
print(f"TOTAAL:           € {totaal:.2f}")
print("="*45)