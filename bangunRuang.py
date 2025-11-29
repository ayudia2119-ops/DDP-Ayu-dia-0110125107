 Import math
def kubus(sisi):
    hasil = math.pow(sisi, 3)
    return hasil
print(kubus(3))

def balok(p,l,t):
    hasil = p * l * t
    return hasil
print(balok(3,3,3))

def prisma(alas, tinggi_segitiga, tinggi_prisma):
    luas_alas = 0.5 * alas * tinggi_segitiga
    hasil = luas_alas * tinggi_prisma
    return hasil
print(prisma(18,15,26))

def tabung(jari_jari, tinggi):
    hasil = (jari_jari ** 2) * tinggi
    return hasil
print(tabung(5,10))

def kerucut(jari_jari, tinggi):
    hasil = (1/3) * (3.14) * (jari_jari ** 2) * tinggi
    return hasil
print(kerucut(4,9))
