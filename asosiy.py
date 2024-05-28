import classes
# import register
import platforma
import json


def asosiy(pin):
    web = input("""
                1.  Karta qo'shish
                2.  Umumiy balans
                3.  Mobil aloqa uchun to'lov
                4.  Cashback
                5.  Sozlamalar
                6.  Kartaga pul quyish
                0.  Orqaga
                
                >>>>>> """)
    if web == "1":
        return car_add(pin)
    elif web == "2":
        return ummumiy_balansi(pin)
    elif web == "3":
        return phone_cash(pin)
    elif web == "4":
        return cashback(pin)
    elif web == "5":
        return sozlamalar(pin)
    elif web == "6":
        return cards_cash(pin)
    elif web == "0":
        return platforma.platforma(pin)
    else:
        print("Error !")
        return asosiy(pin)


def car_add(pin):
    # with open("baza/information.json", encoding="utf-8") as file:
    #     data = json.load(file)
    #     users = data["Users"]
    #     for user in users:
    #         if user["phone number"] == number:
    #             check_user = user
    #
    #     users.remove(check_user)

    card_name = input("Card name : ")
    card = input("Karta raqami : ")
    card_date = input("Amal qilish muddati : ")
    money = float(input("kartadagi pul miqdori : "))
    pul = classes.Card(card_name, card, card_date, money)
    pul.save_card(pin)
    """Bu yerda kamchilik bor va ikkinchi qismi classes qismida card classda """


# with open("baza/information.json", "w") as fayl:
#     new_card = {
#         "Card name": card_name,
#         "Card": card,
#         "Card date": card_date,
#         "money": money
#     }
#     check_user["cards"] = new_card
#     users.append(check_user)
#     data["Users"] = users
#     json.dump(data, fayl, indent=6)
#     print("correct")
#     return asosiy()

def ummumiy_balansi(pin):
    with open("baza/information.json", encoding="utf-8") as file:
        data = json.load(file)
        users = data["Users"]
        for user in users:
            if user["click_pin"] == pin:
                print(f"""
                                Foydalanuvchi: {user["first name"]} {user["last name"]}
                                Card turi: {user["card"]["Card name"]}
                                Card number: {user["card"]["Card"]}
                                Card date: {user["card"]["Card date"]}
                                Card money: {user["card"]["money"]} sum
                                """)
                return asosiy(pin)

def phone_cash(pin):
    # phone = input("Phone number : ")
    # cash = float(input("To'lov summa : "))
    print("hello")
    return asosiy(pin)

def cashback(pin):
    with open("baza/information.json", encoding="utf-8") as file:
        data = json.load(file)
        users = data["Users"]
        for user in users:
            if user["click_pin"] == pin:
                web = input(f"""
                                        Sizning Cashbackingizda : {user["cashback"]} sum bor
                                        
                                        Cashbackdagi pulni asosiy kartalaringizga o'tqazishni hohlaysizmi ?
                                        
                                            1.  Ha
                                            2.  Yo'q
                                            
                                            >>>>>>> """)
                if web == "1":
                    return cash_sent(pin)
                elif web == "2":
                    return asosiy(pin)
                else:
                    print("Error")
                    return ummumiy_balansi(pin)

def cash_sent(pin):
    with open("baza/information.json", encoding="utf-8") as file:
        data = json.load(file)

    with open("baza/information.json", "w") as f:
        users = data["Users"]
        for user in users:
            if user["click_pin"] == pin:
                check_user = user
                sent = int(input("Asosiy kartaga qancha o'tqazmoqchisiz : "))
                if user["cashback"] >= sent:

                    cash = user["cashback"] - sent
                    pul = user["card"]["money"] + sent

        users.remove(check_user)
        check_user["cashback"] = cash
        check_user["card"]["money"] = pul
        users.append(check_user)
        data["Users"] = users
        json.dump(data, f, indent=6)
        print("correct")
        return asosiy(pin)


def cards_cash(pin):
    print("hello")
    return asosiy(pin)
def sozlamalar(pin):
    web = input(""" 
                    1.  Xavfsizlik
                    2.  Sozlamalar
                    3.  Qo'llab-quvvatlash xizmati
                    4.  Dastur haqida
                    0.  Orqaga
                    
                    >>>>>> """)
    if web == "1":
        return security(pin)
    elif web == "2":
        return settings(pin)
    elif web == "3":
        return contact
    elif web == "4":
        return programm_about(pin)
    elif web == "0":
        return asosiy(pin)
    else:
        print("Error")
        return sozlamalar(pin)

def security(pin):
    web = input("""
                Click-PIN ni o'zgartirishni hohlaysizmi ?
                    
                    1.  Ha
                    2.  Yo'q
                
                """)
    if web == "1":
        return click_pin(pin)
    elif web == "2":
        return sozlamalar(pin)
    else:
        print("Error")
        return security(pin)

def click_pin(passport_id):
    with open("baza/information.json", encoding="utf-8") as file:
        data = json.load(file)

    with open("baza/information.json", "w") as fayl:
        users = data["Users"]
        new_pin = input("""         new pincod : """)
        for user in users:
            if user["passport_id"] == passport_id:
                check_user = user

        users.remove(check_user)
        check_user["click_pin"] = new_pin
        users.append(check_user)
        data["Users"] = user
        json.dump(data, fayl, indent=6)
        print("Correct")
        return sozlamalar(passport_id)

def settings(pin):
    web = input("""
                        Sozlamalar display welcome
                            
                            1.  Shaxsiy malumotlar
                            2.  Tilni o'zgartirish               
                            
                            >>>>>>>> """)
    if web == "1":
        return person(pin)
    elif web == "2":
        return
    else:
        print("Error")
        return security(pin)

def person(pin):
    with open("baza/information.json", encoding="utf-8") as file:
        data = json.load(file)
        users = data["Users"]
        for user in users:
            if user["click_pin"] == pin:
                print(f"""
                            Ism : {user["first name"]}
                            Familiya : {user["last name"]}
                            Hudud : {user["hudud"]}
                            Passport ID : {user["passport_id"]}
                            Tug'ilgan sana : {user["birth day"]}
                            Ruyhatdan o'tgan sana : {user["create date"]}
                            
                            """)
                return asosiy(pin)

def contact(pin):
    print("""
                    Assalomu alaykum hurmatli mijoz bizning ilovamizdan foydalanayotganingizda
                    hursandmiz agarda sizda qandaydir tushunmovchilik bo'lsa quyidagi nomerga chiqishingiz mumkun.
                    
                    Admin: +9989 (71) 2310880
                               
                """)
    return asosiy(pin)


def programm_about(pin):
    print("""   
                        Mobil qurilmalardagi Click Up ilovasining foydalanuvchi bitimi

        1.      UMUMIY MAZMUNI
        1.1.    Joriy Foydalanuvchi bitimi (bundan keyin “Bitim”) mobil qurilmalarda “Click Up” mobil 
                ilovasidan foydalanish shartlarini belgilaydi hamda pastda belgilangan harakatlar orqali
                 ushbu Bitimga qo’shilgan yuridik salohiyatli jismoniy shaxs (bundan keyin – “Foydalanuvchi”)
                  bilan Ilovaga alohida egalik huquqlariga ega bo’lgan “CLICK” MChJ (bundan keyin – “Huquq egasi”) 
                  o’rtasida tuzilgan.
        1.2.    “Click Up” mobil ilovasi (bundan keyin “Ilova”) Foydalanuvchiga Android va Apple iOS operatsion
                tizimlari boshqaruvidagi mobil qurilmalar uchun ilovalar Do’konlarida mavjud bo’lgan va “CLICK” 
                xizmati orqali mijozning hisobraqamlarini masofaviy boshqaruv xizmatini taqdim qiluvchi dasturiy 
                mahsulotdir.
        1.3.    Foydalanuvchining mobil qurilmasiga Ilovaning ko’chirilishi (yuklanishi) va o’rnatilishi Foydalanuvchi 
                tomonidan ushbu Bitimni so’zsiz aktseptini (qabul qilishini) va ushbu Bitim shartlariga to’liq roziligini,
                 hamda ushbu shartlar uning qonuniy huquqlari cheklab qo’yilmaganligini tasdiqlashi hisoblanadi.
        1.4.    Ushbu Bitimda quyidagi atamalar va ta’riflar ishlatiladi:
        1.4.1.  Foydalanuvchining mobil telefoni – CLICK xizmatini ulatishda ko’rsatib o’tilgan Foydalanuvchining mobil
                telefon raqami (amaldagi uyali aloqa operatorlaridan istalgan birining).
        1.4.2. CLICK xizmati (CLICK servisi) – ushbu Bitim shartlarini qabul qilgan Foydalanuvchiga istalgan paytda
                va CLICK xizmatining istalgan interfeyslari orqali o’z hisobraqamini onlayn tarzda mosafaviy boshqarish
                 imkonini taqdim qiluvchi xizmat.
        1.4.3.  CLICK Xizmatining interfeyslari – CLICK Tizimining dasturiy-apparat vositalarining vizual qismi. 
                Ular yordamida Foydalanuvchi o’zining bankdagi hisobraqamini boshqaradi va ular o’z ichiga quyidagilarni 
                oladi: (1) mobil veb-interfeys, (2) veb-interfeys, va (3) USSD/SMS portallari.
        1.4.4.  Foydalanuvchining Shaxsiy kabineti – mijozlarga Internet orqali hisobraqamni hamda CLICK servisining 
                xizmatlarini boshqarish va nazorat qilish uchun kerakli o’z shaxsiy ma’lumotlari olish imkonini beruvchi
                 CLICK xizmatining veb-interfeysining vizual qismi.
        1.4.5.  CLICK tizimi – Mijozlarning hisobraqamlaridan ularning buyrug’i bo’yicha va ularning nomidan Yetkazib
                beruvchi foydasiga ko’rsatilgan xizmatlar yoki sotilgan tovarlar uchun yoki O’tkazma paytida boshqa Mijoz
                foydasiga CLICK xizmatining interfeyslari orqali chakana Elektron to’lovlar/O’tkazmalarni amalga oshirish
                 imkonini beruvchi Bank tomonidan ishlatilayotgan tizim.
        1.4.6.  Elektron to’lov (bundan keyin “To’lov”) – O’zbekiston Respublikasining milliy valyutadagi Yetkazib 
                beruvchi foydasiga ko’rsatilgan xizmatlar yoki sotilgan tovarlar uchun to’lanadigan pul mablag’lari. 
                To’lov CLICK servisidan foydalangan holda elektron to’lov hujjatlari orqali amalga oshiriladi.
        1.4.7.  Elektron O’tkazma (bundan keyin “O’tkazma”) – O’zbekiston Respublikasining milliy valyutasida Mijoz 
                (Yuboruvchi) topshirig’i asosida boshqa Mijoz (Oluvchi) foydasiga, yoki Bankdagi yohud boshqa banklardagi
                o’z hisobraqamlariga o’tkaziladigan pul mablag’lari. O’tkazma CLICK servisidan foydalangan holda elektron
                 to’lov hujjatlari orqali amalga oshiriladi
        1.4.8.  Yetkazib beruvchi(lar) – CLICK xizmatining Mijozlaridan to’lovlarni qabul qilish imkoniga ega tovar 
                sotayotgan yoki xizmat ko’rsatayotgan yuridik yoki yuridik shaxsni tashkil qilmasdan turib tadbirkorlik
                amaliyotini olib borayotgan (yakka tartibdagi tadbirkor) jismoniy shaxs.
        1.4.9.  Tariflar – CLICK xizmati ko’rsatilganligi uchun Bank tomonidan Mijozdan ushlab qolinadigan va joriy 
                shartnomaning ajratilmas qismi bo’lgan Bank tomonidan o’rnatilgan tarif va haqlar. """)
    return asosiy(pin)
