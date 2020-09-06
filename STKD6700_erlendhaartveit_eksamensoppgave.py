# Oppgave 2 Legge inn og lagre informasjon

'''
I denne oppgaven skal vi lage et program for å holde oversikt over de ansatte
i en bedrift, deres lønn og hvor gamle de er. Vi vil ha muligheten til å kunne
legge inn brukere med tekst i terminalen, og ikke bare ved å redigere koden.
For å kunne benytte oss av informasjonen om ansatte, så ønsker vi å kunne
lagre dataene når vi er ferdig med å jobbe, samt å kunne lese inn dataene fra
tidligere når vi starter igjen. Skriv koden tydelig og lett leselig, og ta gjerne
med kommentarer eller forklaringer på hvorfor du har gjort ting på en bestemt
måte.
'''

# a) Skriv kode som ber en bruker om å oppgi navn, alder og lønn.
# Denne informasjonen skal lagres i et oppslagsverk eller en liste.

# b) Utvid koden din slik at det er mulig å legge inn informasjon om flere
# personer etter hverandre.
# Sørg for at informasjon om alle personene lagres. Hint: løkke, funksjon

# c) Legg til mulighet for å hoppe ut av løkken og avslutte programmet.
# Hint: break

# d) Skriv funksjon(er) og kode så dataene lagres til fil når programmet er
# ferdig med å kjøre.
# Bruk et av filformatene vi har gjennomgått på forelesning (csv, json
# eller txt).

# e) Vi ønsker at informasjonen skal lagres mellom hver gang programmet
# kjører.
# Juster programmet slik at man laster inn tidligere data fra filen ved
# programstart, og lagrer all informasjon ved programslutt.

# f) Kjør programmet ditt og legg inn 10 ansatte med tilhørende informasjon.
# Sjekk at informasjonen blir liggende i filen når programmet avsluttes.
# Last opp filen sammen med programmet når du leverer eksamen.

import os
import re # For aa ta bort bokstaver fra tall (integers).
from string import digits # For aa ta bort tall fra strenger.

fil_navn="noen_ansatte.txt"

s_ansatte="" # Streng av de ansatte som blir brukt til aa lagre dataen til slutt.
ansatte=[] # Liste over de ansatte.

def list_to_string(liste):
    s_list=""
    linje=""
    size=len(liste)
    for i in range(size):
        linje=""
        verdier=liste[i]
        linje=f"{verdier[0]},{verdier[1]},{verdier[2]}"
        s_list+=f"{linje}\n"
    s_list=s_list.strip()
    return s_list

# For aa lage en formatert streng for de ansatte i en liste.
def list_to_string_spaced(liste):
    s_list=""
    linje=""
    size=len(liste)
    for i in range(size):
        linje=""
        verdier=liste[i]
        linje=f"{verdier[0]}, {verdier[1]}, {verdier[2]}"
        s_list+=f"{linje}\n"
    s_list=s_list.strip()
    return s_list

# Funksjonen aapner en gitt fil, leser dataen, og legger den til listen "ansatte".
def aapne_fil(fil_navn):
    with open(fil_navn, mode='r', encoding='utf-8') as f2:
        fil_innhold=f2.read()
        #print(fil_innhold)
        
        linjer = fil_innhold.split('\n')
        linjer = list(filter(None,linjer)) # fjern eventuelle tomme strenger
        linjer_l=len(linjer)
        for i in range(linjer_l):
            linje=linjer[i]

            verdier=linje.split(",")
            verdier[1]=int(verdier[1])
            verdier[2]=int(verdier[2])
            ansatte.append(verdier)
        
        f2.close()

# Lager og lagrer de ansatte i strengen "s_ansatte" til en gitt fil.
def lag_fil(fil_navn):
    with open (fil_navn, mode='w', encoding ='utf-8') as f:
        f.write(s_ansatte)
        f.close()

# Aapne fil her... // Hvis filen ikke eksisterer, ikke aapne for aa unngaa kraesj.
if os.path.exists(fil_navn):
    aapne_fil(fil_navn)
else:
    print()
    print(f"Fil {fil_navn} eksisterer ikke, så ingenting å åpne!")
    print()
    
s_ansatte=list_to_string_spaced(ansatte)

equals="==============================================================================="

ongoing=True

print(f'''{equals}

Hei, velkommen til ansatt-løkka!

Legg til ansatte i formatet:
navn-alder-lønn

For eksempel:
Bjarne Bjarnason - 50 - 500000

Husk slashen mellom navn-alder og alder-lønn!''')

if len(ansatte)>0:
    print(f'''
{equals}

{s_ansatte}''')

# Funksjonen legger til en ny ansatt til listen "ansatte".
def legg_til_ny_ansatt():
    ansatt=input("Ansatt: ")
    verdier=ansatt.split("-")
    verdier_l=len(verdier)
    if verdier_l<3 or verdier_l>3:
        print()
        print("For få/mange slasher! Bare to stk mellom navn-alder og alder-lønn.")
    else:
        navn=verdier[0]
        alder=verdier[1]
        lonn=verdier[2]
        # Tar bort unodvendig mellomrom.
        navn=navn.strip()
        alder=alder.strip()
        lonn=lonn.strip()

        if navn.isdigit():
            print()
            print("Ikke bruk tall i navnet!")
            legg_til_ny_ansatt()
            return
        else:
            # Tar bort tall etter bokstavene.
            remove_digits = str.maketrans('', '', digits)
            navn=navn.translate(remove_digits).strip().title()
            
        alder=re.sub('\D', '', alder)
        if len(alder)<1:
            print()
            print("Bruk tall for alderen!")
            legg_til_ny_ansatt()
            return
        else:
            alder=int(alder)
        
        lonn=re.sub('\D', '', lonn)
        if len(lonn)<1:
            print()
            print("Bruk tall for lønna!")
            legg_til_ny_ansatt()
            return
        else:
            lonn=int(lonn)

        # At this point, there shouldn't be any issues?:
        verdier[0]=navn
        verdier[1]=alder
        verdier[2]=lonn
        
        ansatte.append(verdier)
        print()
        print(f'''Ansatt lagt til listen! Personen heter {navn}, er {alder} år,
og har en årslønn på {lonn} kroner.''')    

# 
def slette_ansatt(liste):
    
    s_ansatt_liste=""
    
    liste_l=len(liste)
    
    if liste_l<1:
        print()
        print("Listen over ansatte er tom!")
        return
    
    for i in range(liste_l):
        linje=""
        en_ansatt=liste[i]
        nummer=i+1
        linje=f"{nummer}: {en_ansatt[0]}, {en_ansatt[1]}, {en_ansatt[2]}\n"
        s_ansatt_liste+=linje
    
    s_ansatt_liste=s_ansatt_liste.strip()
    
    print('''
0: Gå tilbake.
''')
    print(s_ansatt_liste)
    
    ansatt_nr=input("Hvem vil du slette?: ")
    
    if ansatt_nr.isdigit():
        ansatt_nr=re.sub('\D', '', ansatt_nr)
        ansatt_nr=int(ansatt_nr)
        if ansatt_nr>len(ansatte):
            print()
            print("Vennligst velg et nummer ved siden av en ansatt i lista ovenfor!")
            slette_ansatt(liste)
            return
        elif ansatt_nr==0:
            return
        else:
            # Now it should be a valid index?
            index=ansatt_nr-1
            ans=ansatte[index]
            print()
            print(f"{ans[0]} ble slettet fra listen.")
            del ansatte[index]
            return
    else:
        print()
        print("Vennligst velg et nummer ved siden av en ansatt i lista ovenfor!")
        slette_ansatt(liste)
        return

while ongoing:

    print(f'''
{equals}

1. Legge til ny ansatt.
2. Slette informasjonen til en ansatt.
3. Lagre til fil.''')
    action=input("Hva vil du gjøre?: ")
    if not action.isdigit():
        print()
        print("Skriv et tall mellom 1 og 3!")
    else:
        # Hm, remove letters from the string?
        action=re.sub('\D', '', action)
        action=int(action)
        if action==1:
            legg_til_ny_ansatt()
        elif action==2:
            slette_ansatt(ansatte)
        elif action==3:
            print()
            print("Lagrer listen i filen noen_ansatte.txt.")
            ongoing=False
            break
        else:
            print()
            print("Skriv et tall mellom 1 og 3!") 

ansatte_l=len(ansatte)

s_ansatte=list_to_string(ansatte)

if ansatte_l>0:
    print()
    print(s_ansatte)

lag_fil(fil_navn)
