wiersze=open('przyklad.txt','r')
tablica=[]
for wiersz in wiersze:
    wiersz=wiersz.strip()
    tablica.append(wiersz)
#4.1
# slowo=""
#
# for i  in range(39,len(tablica),40):
#     slowo+=tablica[i][9]
#
# print(slowo)
#4.2
# maks=""
# aktualnaliczbaroznychlier=set()
# najwiekszaliczbaroznychlier=set()
# for tab in tablica:
#     for litery in tab:
#         aktualnaliczbaroznychlier.add(litery)
#     if len(aktualnaliczbaroznychlier) > len(najwiekszaliczbaroznychlier):
#         najwiekszaliczbaroznychlier.clear()
#         najwiekszaliczbaroznychlier=aktualnaliczbaroznychlier.copy()
#         maks = tab
#     aktualnaliczbaroznychlier.clear()
#
# print(str(maks)+" "+str(len(najwiekszaliczbaroznychlier)))
#4.3
czyjest=True
for tab in tablica:
    for wiersz in range(len(tab)-1):
        if (ord(tab[wiersz])-ord(tab[wiersz+1])>10 or ord(tab[wiersz])-ord(tab[wiersz+1])<(-10)) and czyjest :
            czyjest=False
    if czyjest:
        print(tab)
    czyjest=True

