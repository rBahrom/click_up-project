import project
def main():
    language = input("""
                1. Uzbek
                2. English
                3. Russia
                    >>>>> """)
    if language == "1":
        return project.choose()
    elif language == "2":
        return
    elif language == "3":
        return
    else:
        print("Error !")
        return main()


if __name__ == "__main__":
    main()
