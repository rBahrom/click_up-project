import asosiy
import tulov
import utkazmalar
import hisobot
def platforma(pin):
    web = input("""
            1.  Asosiy
            2.  To'lovlar 
            3.  O'tkazmalar
            4.  Hisobotlar
            
             >>>>>>> """)
    if web == "1":
        return asosiy.asosiy(pin)
    elif web == "2":
        return tulov.tolov(pin)
    elif web == "3":
        return utkazmalar.utkazmalar(pin)
    elif web == "4":
        return hisobot.hisobot(pin)
    else:
        print("Error !")
        return platforma(pin)
