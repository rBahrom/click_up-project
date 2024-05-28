import platforma
def hisobot(pin):
    web = input(""" 
                    1.  O'tkazmalar tarixi
                    0.  Orqaga
                    """)
    if web == "1":
        return history()
    elif web == "0":
        return platforma.platforma(pin)
    else:
        print("Error !")
        return hisobot(pin)

def history():
    pass
