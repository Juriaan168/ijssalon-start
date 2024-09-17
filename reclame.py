from algemene_functies import mijn_functie_2
import algemene_functies

Invoer_lijst_2 = 0
vanuit_LH = "False"


from algemene_functies import meervoudig_aangeroepen_vanuit_combinatie
from algemene_functies import korte_lijst


def aanbieding_1():
    #argumenten aanvragen
    print("Beste Peter dit is opdracht aanbieding_1")
    Smaak = input("Welke smaak wilt u in de aanbieding zetten?")
    Prijs_orgineel = input("Wat was de orginele prijs?")

    #Nieuwe prijs berekenen
    Prijs_inc_korting = float(Prijs_orgineel) * (1 - float(input("wat is de fractie die u van de prijs afwilt?")))

    #kosten uitdrukken in 2 decimaal bv 3.6 euro wordt 3.60 euro
    Prijs_inc_korting = "{:.2f}".format(round(Prijs_inc_korting, 2))

    # . vervangen door , dus 3.60 word 3,60
    Prijs_inc_korting = Prijs_inc_korting.replace(".",",")

    #aanbeiding printen
    print(f"Vandaag in de aanbieding: emmertje ijs (1 liter) in de smaak {Smaak}, van {Prijs_orgineel} euro voor {Prijs_inc_korting} euro.")





def inkomsten_totaal():
    print("Beste Peter dit is opdracht totaale inkomsten bij elkaar optellen")
    inkomsten = input("Voer a.u.b inkomsten in bv 10,20,30,40,50,60,70 =>").replace("[","").replace("]","")
    list_inkomsten = inkomsten.split(",")
    list_inkomsten = [int(i) for i in list_inkomsten]
    inkomsten_sum = sum(list_inkomsten)
    
    _totaal = str("{:.2f}".format(round(inkomsten_sum, 2))).replace(".",",")
    #De belastingdienst doet weer is vervelend
    Vervelende_belasting = float(input("wat is de fractie die u kwijtraakt aan belasting?").replace("[","").replace("]","").replace(",",".")) *inkomsten_sum
    _bedrag = str("{:.2f}".format(round(Vervelende_belasting, 2))).replace(".",",")

    ##Het totaal van alle inkomsten van deze week is <totaal> euro, waarover <bedrag> euro btw betaald dient te worden.
    print(f"Het totaal van alle inkomsten van deze week is {_totaal} euro, waarover {_bedrag} euro btw betaald dient te worden.")




def laag_en_hoog():
    global meervoudig_aangeroepen_vanuit_combinatie
    global Invoer_lijst_2
    global korte_lijst
    global vanuit_LH
    if meervoudig_aangeroepen_vanuit_combinatie == "False":
        if  vanuit_LH == "False":      
            print("Beste Peter dit is de opdracht hoogste en laagste getal pakken")
        inkomstenLH = input("Voer a.u.b inkomsten in bv 10,20,30,40,50,60,70 =>").replace("[","").replace("]","")
    else:
        inkomstenLH = str(Invoer_lijst_2)        
    list_inkomstenLH = inkomstenLH.split(",")
    list_inkomstenLH = [int(i) for i in list_inkomstenLH]
    if meervoudig_aangeroepen_vanuit_combinatie == "False":
        print("congrats hier komen de hoogste en laagste")
    List_enkel_laag_en_hoog_LH = [max(list_inkomstenLH) ,min(list_inkomstenLH) ]
    if meervoudig_aangeroepen_vanuit_combinatie == "False":
        print(List_enkel_laag_en_hoog_LH)
    else:
        korte_lijst = List_enkel_laag_en_hoog_LH
        algemene_functies.korte_lijst = List_enkel_laag_en_hoog_LH



def gemiddelde():
    print("Beste Peter dit is de opdracht om gemiddelde te berekenen")
    mijnlijst = input("Voer a.u.b inkomsten in bv 10,20,30,40,50,60,70 =>").replace("[","").replace("]","")
    mijnlijst = mijnlijst.split(",")
    mijnlijst = [int(i) for i in mijnlijst]
   
   
    mijnlijst =  sum(mijnlijst)/len(mijnlijst)
    mijnlijst = "{:.2f}".format(round(mijnlijst, 2))
    mijnlijst = mijnlijst.replace(".",",")
    print(f"De gemiddelde inkomsten deze week zijn {mijnlijst} euro.")
   
def meervoudig():
    global meervoudig_aangeroepen_vanuit_combinatie
    global vanuit_LH

    if meervoudig_aangeroepen_vanuit_combinatie == "False":
        print("Beste Peter dit is de opdracht meervoudig deze verschilt verder wijnig van Laag/Hoog")

    vanuit_LH = "TRUE"
    laag_en_hoog()
    vanuit_LH = "False"
    


def combinatie():
    global meervoudig_aangeroepen_vanuit_combinatie
    global Invoer_lijst_2
    global korte_lijst
    print("Beste Peter dit is de combinatie opdracht.")
    Invoer_lijst_2 = input("Welke waarde wilt u hebben als Invoer lijst 2?").replace("[","").replace("]","")
    meervoudig_aangeroepen_vanuit_combinatie = "True"
    algemene_functies.meervoudig_aangeroepen_vanuit_combinatie = "True"
    meervoudig()
    print(korte_lijst)
    mijn_functie_2()
    meervoudig_aangeroepen_vanuit_combinatie = "False"
    algemene_functies.meervoudig_aangeroepen_vanuit_combinatie = "False"


aanbieding_1()    
inkomsten_totaal()
laag_en_hoog()
gemiddelde()
meervoudig()
combinatie()
print("Beste Peter dat waren alle opdrachten van Les8 bedankt voor het testen en nakijken")
print("Met vriendelijke groet,")
print("Juriaan")
