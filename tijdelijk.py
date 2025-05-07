#opdracht 2
prijzen = {
    "aardbei" : 3,
    "Vanille" : 4,
    "Chocolade" : 5
}

#opdracht 3
aanbieding = prijzen["aardbei"] *0.8

#opdracht 4
#In de opdracht staat dat de aanbieding "vanille-ijs" zou moeten zijn, echter klopt dit dan niet met de bovenstaande code
reclame_tekst = f"Vandaag in de aanbieding: aardbei-ijs, 1 liter – slechts € {aanbieding}"
#print(reclame_tekst)

#opdracht 5
reclame_tekst2 = reclame_tekst[:62]
#print(reclame_tekst2)

#opdracht 6
reclame_tekst3 = (reclame_tekst2.upper())
#print(reclame_tekst3)

#opdracht 7
reclame_tekst4 = (reclame_tekst3.split(" "))
#print(reclame_tekst4)

#opdracht 8-10
for el in reclame_tekst4:
    if len(el) > 4:
        print(el.upper())
    else:
        print(el.lower())
    
