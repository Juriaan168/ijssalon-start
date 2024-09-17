from helper import decoreer


def print_aanbieding():
    # prijslijst
    prijzen = {
    "aardbei" : 3,
    "vanille" : 4,
    "chocolade" : 5
    }

    # aanbieding want vanille is goedkoper
    aanbieding = prijzen["aardbei"] * 0.8 


    # reclame text van aanbeiding
    reclame_tekst = "Vandaag in de aanbieding: aardbei-ijs, 1 liter - slechts €" + str(aanbieding)


    # Afronden naar 2 tekens achter comma
    reclame_tekst2 = reclame_tekst[:62]


    # Oom ellie met sportvliegtuig
    reclame_tekst3 = reclame_tekst2.upper()


    # List van woorden
    reclame_tekst4 = reclame_tekst3.split(" ")


    # de for loop alles onder elkaar
    for el in reclame_tekst4:
        if len(el) < 5:
         print(el.lower())
        else:
            print(el.upper()) 
            # In princiepe is de upper in de else stakement hier overbodig omdat bij de stap van het spoortvliegtuig alles al in upper gezet was. Maar will wel netjes consistent blijven met de if stakement war lower wel genoed is.


decoreer("Aanbieding")
print_aanbieding()
