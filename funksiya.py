from datetime import date

def foydalanuvchi_anketasi():
    malumotlar = {}

    # Ism
    while True:
        ism = input("Ismingizni kiriting: ").strip()
        if ism.isalpha():      # bu harf A-z harflar bo'lsa 'True' qaytaradi
            malumotlar['ism'] = ism
            break
        else:
            print("⚠️ Ism faqat harflardan iborat bo‘lishi kerak.")

    # Familiya
    while True:
        familiya = input("Familyangizni kiriting: ").strip()
        if familiya.isalpha():
            malumotlar['familiya'] = familiya
            break
        else:
            print("⚠️ Familiya faqat harflardan iborat bo‘lishi kerak.")

    # Tug‘ilgan yil
    while True:
        tug_yil = input("Tug‘ilgan yilingizni kiriting (masalan, 2000): ").strip()
        if tug_yil.isdigit():
            tug_yil = int(tug_yil)
            hozirgi_yil = date.today().year
            if 1900 <= tug_yil <= hozirgi_yil:
                malumotlar['tugilgan_yil'] = tug_yil
                malumotlar['yosh'] = hozirgi_yil - tug_yil
                break
        print("⚠️ Tug‘ilgan yil noto‘g‘ri kiritildi.")

    # Tug‘ilgan joy
    while True:
        joy = input("Tug‘ilgan joyingizni kiriting: ").strip()
        if joy:
            malumotlar['tugilgan_joy'] = joy
            break
        else:
            print("⚠️ Tug‘ilgan joy bo‘sh bo‘lishi mumkin emas.")

    # Ixtiyoriy ma'lumotlar
    tel = input("Telefon raqamingizni kiriting (ixtiyoriy): ").strip()
    email = input("Elektron manzilingizni kiriting (ixtiyoriy): ").strip()

    if tel:
        malumotlar['telefon'] = tel
    if email:
        malumotlar['email'] = email

    return malumotlar

# Funksiyani chaqiramiz va natijani chiqaramiz
anketa = foydalanuvchi_anketasi()
print("\n Foydalanuvchi ma'lumotlari:")
print(anketa)
