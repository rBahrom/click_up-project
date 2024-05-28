import platforma
import json
def utkazmalar(pin):
    web = input(""" 
                    
                    1.  Pul o'tkazish
                    2.  Kartalar o'rtasida 
                    0.  Orqaga                  
                    """)
    if web == "1":
        return cash_sent(pin)
    elif web == "2":
        return card_between(pin)
    elif web == "0":
        return platforma.platforma(pin)
    else:
        print("Error !")
        return utkazmalar(pin)

def cash_sent(pin):
    with open("baza/information.json", encoding="utf-8") as file:
        """Bu yerda pul utqazadigan foydalanuvchini topayapdi"""
        data = json.load(file)
        users = data["Users"]
        karta = input("Karta raqami : ")
        for user in users:
            if user["card"]["Card"] == karta:
                for myuser in users:
                    my = myuser
                    print(f"Qabul qiluvchi: {user["first name"]} {user["last name"]}")
                    sent = int(input("Summa : "))
                    cash = my["card"]["money"] - sent
                    pul = user["card"]["money"] + sent
                    cashelock = (sent * 10) / 100
                    data_x = my
                    users.remove(my)
                    data_x["card"]["money"] = cash
                    my["cashback"] = cashelock
                    users.append(data_x)
                    data["Users"] = users
                    with open("baza/information.json", "w") as f:
                        json.dump(data, f, indent=6)
                    data_y = user
                    users.remove(user)
                    data_y["card"]["money"] = pul
                    # my["cashback"] = cashelock
                    users.append(data_y)
                    data["Users"] = users
                    with open("baza/information.json", "w") as f:
                        json.dump(data, f, indent=6)
                    return utkazmalar(pin)

        # for i in users:
        #     if i["click_pin"] == pin:
        #         check_user = i
        #         cash = i["card"]["money"] - sent
        #         pul = i["card"]["money"] + sent
        #         cashelock = (sent * 10)/100
        # users.remove(check_user)
        # check_user["card"]["money"] = cash
        # check_user["cashback"] = cashelock
        # users.append(check_user)
        # with open("baza/information.json", "w") as f:
        #     json.dump(data, f, indent=6)
        #
        # user1 = i
        # users.remove(user1)
        # user1["card"]["money"] = pul
        # check_user["cashback"] = cashelock
        # users.append(user1)
        # with open("baza/information.json", "w") as f:
        #     json.dump(data, f, indent=6)
        #     print("correct")


def card_between(pin):
    web = input("""
                        Kartalar o'rtasida pul almashish
                     
                1.  Asosiy kartadan qushimcha kartaga
                2.  Qushimcha kartadan Asosiy kartaga 
                """)
    if web == "1":
        return asosiy(pin)
    elif web == "2":
        return qushimcha(pin)
    else:
        print("Error")
        return card_between(pin)

def asosiy(pin):
    with open("baza/information.json", encoding="utf-8") as file:
        data = json.load(file)
    with open("baza/information.json", "w") as f:
        users = data["Users"]
        for user in users:
            if user["click_pin"] == pin:
                check_user = user
                sent = int(input("Qo'shimcha kartaga qancha o'tqazmoqchisiz : "))
                if user["cashback"] >= sent:

                    cash = user["cashback"] - sent
                    pul = user["card"]["money"] + sent
        users.remove(check_user)
        check_user["cashback"] = pul
        check_user["card"]["money"] = cash
        users.append(check_user)
        data["Users"] = users
        json.dump(data, f, indent=6)
        print("correct")
    return utkazmalar(pin)

def qushimcha(pin):
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
    return utkazmalar(pin)
