def presenteer(dict, totaal):  
    overzicht = []
    for k,v in dict.items():
        overzicht.append(f"{k} : {v}")
    overzicht.append("="*25)
    overzicht.append(f"totaal : {totaal}")
    return overzicht


