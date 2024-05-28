import json
from datetime import datetime
import random
import asosiy
# import login
import platforma
# import register


class User:
    def __init__(self, first_name: str, last_name: str, passport_id: str, birth_day: str, phone_number: str):
        self.first_name = first_name
        self.last_name = last_name
        self.passport_id = passport_id
        self.birth_day = birth_day
        self.phone_number = phone_number
        self.create_date = f"{datetime.now()}"
        self.cashback_card = (f"{random.randint(1000, 9999)} {random.randint(1000, 9999)}"
                              f" {random.randint(1000, 9999)} {random.randint(1000, 9999)}")
        self.cashback = 0

    def __str__(self):
        return (f"{self.first_name}"
                f"{self.last_name}"
                f"{self.birth_day}")

    def full_info(self):
        return f"""
                First Name : {self.first_name}
                Last Name : {self.last_name}
                Passport ID : {self.passport_id}
                Birth Day : {self.birth_day}
                Phone Number : {self.birth_day}
                Create Date : {self.create_date}
                """

    def save(self):
        """Bu yerda ruyhatdan o'tilgan mijozlar bazaga saqlanishi """
        with open("baza/information.json", encoding="utf-8") as file:
            data = json.load(file)

        with open("baza/information.json", "w") as fayl:
            users = {
                "first name": self.first_name,
                "last name": self.last_name,
                "passport_id": self.passport_id,
                "birth day": self.birth_day,
                "phone number": self.phone_number,
                "create date": self.create_date,
                "cashback_card": self.cashback_card,
                "cashback": self.cashback
            }
            data["Users"].append(users)
            json.dump(data, fayl, indent=6)
        print("Foydalanuvchi malumotlar bazasiga saqlandi ")

    @staticmethod
    def check_user(pin):
        with open("baza/information.json", encoding="utf-8") as file:
            data = json.load(file)
            for user in data["Users"]:
                if user["click_pin"] == pin:
                    return platforma.platforma(pin)
                # else:
                #     web = input("""
                #             Bunday foydalanuvchi mavjud emas ruyhatdan o'ting
                #             Yoki siz kiritgan Click-PIN kodi xatochilik bor
                #                     1.  Qayta PIN kirish
                #                     2.  Ruhyatdan o'tish
                #             """)
                #     if web == "1":
                #         return login.login()
                #     elif web == "2":
                #         return register.register()
                #     else:
                #         return login.login()


# def again():
#     web = input("""
#                                 Bunday foydalanuvchi mavjud emas ruyhatdan o'ting
#                                 Yoki siz kiritgan Click-PIN kodi xatochilik bor
#                                         1.  Qayta PIN kirish
#                                         2.  Ruhyatdan o'tish
#                                 """)
#     if web == "1":
#         return login.login()
#     elif web == "2":
#         return register.register()
#     else:
#         return again()
#

class Card:
    def __init__(self, card_name: str, card: int, card_date: str, money: float):
        # User.__init__(self, first_name, last_name, passport_id, birth_day, phone_number)
        self.card_name = card_name
        self.card = card
        self.card_date = card_date
        self.money = money

    def __str__(self):
        return (f"{self.card_name}\n"
                f"{self.card}\n"
                f"{self.card_date}\n"
                f"{self.money}")

    # @property
    # def get_money(self):
    #     return self.__money

    def save_card(self, pin):
        """Bu yerda ruyhatdan o'tilgan mijozlar bazaga saqlanishi """
        with open("baza/information.json", encoding="utf-8") as file:
            data = json.load(file)

        with open("baza/information.json", "w") as fayl:
            users = data["Users"]
            for user in users:
                if user["click_pin"] == pin:
                    check_user = user
            new_card = {
                "Card name": self.card_name,
                "Card": self.card,
                "Card date": self.card_date,
                "money": self.money
            }
            users.remove(check_user)
            check_user["card"] = new_card
            users.append(check_user)
            data["Users"] = users
            json.dump(data, fayl, indent=6)
        print("Foydalanuvchi malumotlar bazasiga saqlandi ")
        return asosiy.asosiy(pin)
