def decoreer(tekst = ""):
    tekst = "header"
    lengte = len(tekst) + 4
    print()
    print(lengte * "*")
    print(f"* {tekst} *")
    print(lengte * "*")
    print()

def fooi_pp(bedrag,personen):
    try:
        fooi = bedrag/personen
    except:
        fooi = "??"
    pp = f"Het bedrag per persoon is {fooi} euro"
    return pp

def onderstreep(tekst= ""):
    uit = []
    uit.append(tekst)
    uit.insert(1, len(tekst) * "=")
    return uit

def som(dict):
    som = sum(dict.values())
    return som