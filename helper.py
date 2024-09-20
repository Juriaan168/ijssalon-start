def decoreer(tekst=""):
    lengte = len(tekst) + 4
    print()
    print(lengte * "*")
    print(f"* {tekst} *")
    print(lengte * "*")
    print()

def fooi_pp(bedrag, personen):         
    bedrag_pp = bedrag/personen 
    return f"Het bedrag per persoon is {bedrag_pp} euro"
       

def onderstreep(tekst = ""):
    uit = []    
    uit.append(tekst)
    uit.append("=" * len(tekst))
    return uit

def som(input_dict):

    #Pak alle values en zet ze achter elkaar als array/list, want keys hebben we niks aan bij totaal bereken
    output_dict = []
    for key in input_dict.keys() :
        output_dict.append(input_dict[key])
    return sum(output_dict)

