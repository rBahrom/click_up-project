import json
import classes
import random
import platforma

def register():
    """Bu yerda foydalanuvhi ruyhatdan o'tishi"""
    print("Welcome Register display ")
    firstname = input("First Name: ")
    lastname = input("Last Name: ")
    passport_id = input("Passport_ID: ")
    Birth_day = input("Birth Day: ")
    Phone_number = input("Phone Number: ")
    user = classes.User(firstname, lastname, passport_id, Birth_day, Phone_number)
    user.save()
    return register_number(passport_id)

def register_number(passport_id):
    """Bu yerda foydalanuvchi malumotlarni kiritgandan so'ng Clickga ulamoqchi bulgan nomerni kiritish
     """
    print("""Hurmatli foydalanuvchi telefon raqamingizni kiriting""")
    number = input("Telefon number : ")
    print(f"""
                    Shu raqamga sms xabar orqali kod boradi : {number}
                     iltimos biroz kuring ......... 
                    """)
    return register_number_sms(passport_id)


def register_number_sms(passport_id):
    """Bu yerda click app ga ulamoqchi bulgan nomeringizga kod boradi ushani tekshiradi
    """
    print("""
                    Hurmatli mijoz bu kodni hech kimga bermang ! .
                """)
    array = random.randint(10000, 99999)

    print(f""" {array}""")
    cod = int(input("Kodni kiriting : "))
    if cod == array:
        return Click_pin(passport_id)
#     else:
#         return number_sms(array, cod)
#
# def number_sms(array, cod):
#     if cod in array:
#         return Click_pin()
#     else:
#         return number_sms(array, cod)

# def kod():
#     if cod.isdigit():
#         cod = int(cod)
#     web = input("""
#                             Ko'p o'rinishlar sababli kod eskirdi.
#                                 Kod qaytadan yuborilsinmi......
#                                     1.  Ha
#                                     2.  Yo'q
#                                     >>>> """)
#     if web == "1":
#         return register_number_sms()
#     elif web == "2":
#         return
#     else:
#         print("Error !")
#         return kod()

def Click_pin(passport_id):
    """Click app ga kirishda click app ga quyiladigan kod"""
    print("Welcome Click up display")
    with open("baza/information.json", encoding="utf-8") as file:
        data = json.load(file)
        users = data["Users"]
        for i in users:
            if i["passport_id"] == passport_id:
                check_user = i

        users.remove(check_user)

    with open("baza/information.json", "w") as fayl:
        password1 = int(input("click_pin : "))
        password2 = int(input("click_pin : "))

        if password1 == password2:
            check_user["click_pin"] = password2
            users.append(check_user)
            data["Users"] = users
            json.dump(data, fayl, indent=6)
            print("Click-PIN foydalanuvchi bazasiga saqlandi")
            return platforma.platforma(passport_id)
        else:
            return Click_pin(passport_id)
