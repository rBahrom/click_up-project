import platforma
def tolov(pin):
    web = input("""
                    1.  Mobil operatorlar
                    2.  Komunal to'lov
                    3.  Soliq
                    0.  Orqaga 
                    """)
    if web == "1":
        return phone_operator(pin)
    elif web == "2":
        return Utility()
    elif web == "3":
        return soliq()
    elif web == "0":
        return platforma.platforma(pin)
    else:
        print("Error !")
        return tolov(pin)

def phone_operator(pin):
    web = input("""
            Qaysi telefon raqam kompaniyasiga pul quymoqchisiz
                    
                    1.  Beeline
                    2.  Ucell
                    3.  UzMobile
                    4.  Humis
                    5.  Mobiuz
                    6.  OQ
                    0.  Orqaga 
                    
                    >>>> """)
    if web == "1":
        return beeline(pin)
    elif web == "2":
        return ucell(pin)
    elif web == "3":
        return uzmobile(pin)
    elif web == "4":
        return humas(pin)
    elif web == "5":
        return mobiuz(pin)
    elif web == "6":
        return oq(pin)
    elif web == "0":
        return tolov(pin)
    else:
        print("Error")
        return phone_operator(pin)


def beeline(pin):
    web = input("""
                1.  +998 (90) -  
                2.  +998 (91) - 
                 >>>> """)
    if web == "1":
        return beeline_bir(pin)
    elif web == "2":
        return beeline_ikki(pin)
    else:
        print("Error")
        return beeline(pin)

def beeline_bir(pin):
    web = input("""
                +998 (90) - """)
    cash = float(input("""
                    pul : """))

    print(f""" 
                {web} nomerga {cash} sum
                To'lov amalga oshirildi """)
    return tolov(pin)


def beeline_ikki(pin):
    web = input("""
                 +998 (91) - """)
    cash = float(input("""
                        pul : """))
    print(f"""      
                {web} nomerga {cash} sum
                To'lov amalga oshirildi """)
    return tolov(pin)

def ucell(pin):
    web = input("""
                    1.  +998 (93) -  
                    2.  +998 (94) - 
                     >>>> """)
    if web == "1":
        return ucell_bir(pin)
    elif web == "2":
        return ucell_ikki(pin)
    else:
        print("Error")
        return beeline(pin)

def ucell_bir(pin):
    web = input("""
                    +998 (93) - """)
    cash = float(input("""
                        pul : """))
    print(f"""      
                {web} nomerga {cash} sum
                To'lov amalga oshirildi """)
    return tolov(pin)

def ucell_ikki(pin):
    web = input("""
                     +998 (94) - """)
    cash = float(input("""
                        pul : """))
    print(f"""      
                {web} nomerga {cash} sum
                To'lov amalga oshirildi. . . .  """)
    return tolov(pin)

def uzmobile(pin):
    web = input("""
                nomer: +998 (99) - """)
    cash = float(input("""
                        pul : """))
    print(f"""      
                {web} nomerga {cash} sum
                To'lov amalga oshirildi. . . .  """)
    return tolov(pin)

def humas(pin):
    web = input("""
                    nomer: +998 (33) - """)
    cash = float(input("""
                            pul :  """))
    print(f"""      
                    {web} nomerga {cash} sum
                    To'lov amalga oshirildi. . . .  """)
    return tolov(pin)

def mobiuz(pin):
    web = input("""
                    nomer: +998 (97) - """)
    cash = float(input("""
                            pul :  """))
    print(f"""      
                    {web} nomerga {cash} sum
                    To'lov amalga oshirildi. . . .  """)
    return tolov(pin)

def oq(pin):
    web = input("""
                    nomer: +998 (22) - """)
    cash = float(input("""
                            pul : """))
    print(f"""      
                    {web} nomerga {cash} sum
                    To'lov amalga oshirildi. . . .  """)
    return tolov(pin)

def Utility():
    web = input("""
            1.  Elektr-energiya
            2.  Suv
            3.  Gaz
            4.  
            """)
    if web == "1":
        return


def soliq():
    print("hello")
