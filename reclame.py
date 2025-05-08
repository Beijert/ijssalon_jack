from algemene_functies import mijn_functie_2


def aanbieding_1(smaak, prijs, korting):
    kortingsprijs = prijs - prijs * korting
    aanbieding = f"Vandaag in de aanbieding: emmertje ijs (1 liter) in de smaak {smaak}, van {prijs} euro voor {kortingsprijs} euro."
    return aanbieding

def inkomsten_totaal(inkomsten, btw):
    bruto = sum(inkomsten)
    aftrek = bruto*btw
    netto = f"Het totaal van alle inkomsten van deze week is {bruto} euro, waarover {aftrek} euro btw betaald dient te worden."
    return netto

def laag_en_hoog(mijn_lijst):
    min_max =[min(mijn_lijst), max(mijn_lijst)]
    return min_max

def gemiddelde(mijn_lijst):
    gemiddelde = sum(mijn_lijst)/len(mijn_lijst)
    tekst = f"De gemiddelde inkomsten deze week zijn {gemiddelde} euro."
    return tekst

def meervoudig(invoer_lijst):
    uitvoer = [laag_en_hoog(invoer_lijst)]
    return uitvoer

def combinatie(invoer_lijst_2):
    korte_lijst = laag_en_hoog(invoer_lijst_2)
    uitvoer = mijn_functie_2(korte_lijst[0], korte_lijst[1])
    return uitvoer
