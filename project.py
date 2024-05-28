import register
import login
def choose():
    regis = input("""
                1.  Login
                2.  Register
                >>>>>>>> """)
    if regis == "1":
        return login.login()
    elif regis == "2":
        return register.register()
    else:
        print("Error !")
        return choose()
