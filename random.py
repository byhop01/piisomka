from random import choice

mena = ("Filip", "Marek", "David", "Adam", "Samo")
slovesa = ("bezi", "plave", "spieva", "skace", "hra")
pridmena = ("rychlo", "pomaly", "tazko", "silno", "slabo")
predmet = ("auto", "pocitac", "mobil", "tablet", "kabel")

for _ in range(int(input("Enter integer value : "))):
    print(list(map(choice, [mena, slovesa, pridmena, predmet])))
