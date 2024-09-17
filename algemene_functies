meervoudig_aangeroepen_vanuit_combinatie = "False"
korte_lijst = []

def mijn_functie_1():
  print("Beste Peter dit is opdracht mijn_functie_1")
  print("Invoer is A")
  print("Uitvoer is A^2")
  Invoer = input("Welk getal will u geven als invoer waarde voor mijn_functie_1?")
  print(str(int(Invoer)**2))
  

def mijn_functie_2():
  global meervoudig_aangeroepen_vanuit_combinatie
  global korte_lijst
  if meervoudig_aangeroepen_vanuit_combinatie == "False": 
    print("Beste Peter dit is opdracht mijn_functie_2")
    print("Invoer is A,B")
  print("Uitvoer is [A+B,A-B,A*B,A/B]")
  if meervoudig_aangeroepen_vanuit_combinatie == "False": 
    Invoer = input("Welk getal will u geven als invoer waarde voor mijn_functie_2?").replace("[","").replace("]","")
    Invoer_as_list = Invoer.split(",")
  else: 
    Invoer_as_list = korte_lijst
  A = int(Invoer_as_list[0])
  B = int(Invoer_as_list[1])  
  Uitvoer = [int(A+B),int(A-B),int(A*B),int(A/B)]

  print(str(Uitvoer))



mijn_functie_1()
mijn_functie_2()




