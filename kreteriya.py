
weight =[]
index =[]

def kreteriya(obekt,klass,m1,m2):
    # Kelgan obekt tartib bo'yicha saralab shunga
    # bog'liq classni ham bir xil saralash
    max = 0
    adress=0
    for i in range(len(obekt)):
        for j in range(len(obekt)):
            if obekt[i] < obekt[j]:
                q = obekt[i]
                obekt[i] = obekt[j]
                obekt[j] = q
                k = klass[i]
                klass[i] = klass[j]
                klass[j] = k


    # formuladani har bir qiymat uchun belgilar

    u11=0   # birinchi classning chap tarafdagilar soni
    u21=0   # birinchi classning o'ng tarafdagilar soni
    u12=0   # ikkinchi classning chap tarafdagilar soni
    u22=0   # ikkinchi classning o'ng tarafdagilar soni
    weight1=0
    weight2=0
    weight3=0

    # kreteriya bo'yicha eng kattasini aniqlash jarayoni

    for  i in range(len(obekt)-1):
            natija = 0
            # obektda ketma-ket teng bo'lmasa shart bajariladi
            if obekt[i] != obekt[i+1]:
                if klass[i] == 1:
                    u11+=1
                    u21= m1-u11
                    u22=m2-u12
                else:
                    u12+=1
                    u22=m2-u12
                    u21=m1-u11
                # Kreteriya formulasi bo'yicha ishlaydigan joy

                weight1 = (u11 * (u11 - 1) + u21 * (u21 - 1) + u12 * (u12 - 1) + u22 * (u22 - 1))
                weight2 = (u11 * (m2 - u21) + u21 * (m1 - u11) + u12 * (m2 - u22) + u22 * (m1 - u12))
                weight3 = (m1 * (m1 - 1) + m2 * (m2 - 1)) * 2 * m1 * m2
                natija = (weight1*weight2)/weight3

            else:
                if klass[i] == 1:
                    u11+=1
                    u21= m1-u11
                    u22=m2-u12
                else:
                    u12+=1
                    u22=m2-u12
                    u21=m1-u11

            if natija !=0:
                if max < natija:
                    max = natija
                    adress = i


    weight.append(max)
    index.append(adress)

def tartiblash(obekt):
    # Fayldan malumotdan o'qib olib listga aylantirish
    obekt += ' '
    obekt.replace('\n', ' ')
    obekt1 = []
    toplash = ''
    for i in obekt:
        if i != ' ' and i != '\n':
            toplash += i
        else:
            toplash = int(toplash)
            obekt1.append(toplash)
            toplash = ''

    obekt2 = []

    # Listdagi elementlarni klasslargacha farqini topish

    klass = []
    qadam = 0
    for i in obekt1:
        if i != 1 and i != 2:
            qadam += 1
        else:
            break

    for i in obekt1:
        if i != 1 and i != 2:
            obekt2.append(i)
        else:
            klass.append(i)
    klass1 = tuple(klass)

    #  har bir classlar sonini aniqlash
    m1 = 0
    m2 = 0
    for i in range(len(klass)):
        if klass[i] == 1:
            m1 += 1
        else:
            m2 += 1

    # Listdagi har bir xususiyatni funksiya uzatgan holda eng kattasi ehtimolni topish

    obekt3 = []
    b_nuqta = 0

    while b_nuqta < qadam:
        klass = list(klass1)
        obekt3 = []
        for i in range(b_nuqta, len(obekt2), qadam):
            obekt3.append(obekt2[i])
        kreteriya(obekt3, klass, m1, m2)
        b_nuqta += 1

    print(f"Kretiriyada har bir xususiyat bo'yicha erishayotgan vaznlar")
    print(weight)
    maxWeight = 0
    engKattaQiymat = 0

    for i in range(len(weight)):
        if maxWeight < weight[i]:
            maxWeight = weight[i]
            b_nuqta = index[i]
            engKattaQiymat = i

    # Natijani ko'rish jarayoni
    obekt1 = []
    while True:
        for i in range(engKattaQiymat, len(obekt2), qadam):
            obekt1.append(obekt2[i])
        break

    klass = list(klass1)

    for i in range(len(obekt1)):
        for j in range(len(obekt1)):
            if obekt1[i] < obekt1[j]:
                q = obekt1[i]
                obekt1[i] = obekt1[j]
                obekt1[j] = q
                k = klass[i]
                klass[i] = klass[j]
                klass[j] = k

    print(f"Eng katta qiymatga {engKattaQiymat + 1}-xususiyatda erishayapti.\nNatija bilan tanishamiz! "
          f"\nNatija = {maxWeight}")

    for i in range(0, len(obekt1)):
        if i != b_nuqta:
            print(obekt1[i], end=' ')
        else:
            print(obekt1[i], end=' | ')
    print()
    for i in range(0, len(klass)):
        if i != b_nuqta:
            print(klass[i], end='  ')
        else:
            print(klass[i], end='  | ')

