import classes
def login():
    """Bu yerda foydalanuvchi uzining pin kodi orqali kirish joyini tekshiradi"""
    print("Welcome Login display ")
    pin = int(input("pincod : "))
    if classes.User.check_user(pin):
        return classes.User.check_user
