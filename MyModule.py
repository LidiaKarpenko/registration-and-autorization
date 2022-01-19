from random import *
def displayMenu():
    status = input("Вы зарегистрированный пользователь? y/n? нажмите q чтобы выйти")
    if status == "y":
        oldUser()
    elif status == "n":
        newUser()
 
def newUser():
    createLogin = input("Создайте имя для входа: ")
 
    if createLogin in Users:
        print("\nТакое имя пользователя уже существует\n")
    else:
        createPassw = input("Создать пароль: ")
        Users.write(createLogin,createPassw)
        print("\nИмя пользователя создано!\n")
 
def oldUser():
    login = input("Введите имя пользователя: ")
    passw = input("Введите пароль: ")
 
    if login in Users and passw in Users:
        print("\nВы успешно зашли!\n")
    else:
        print("\nИмя пользователя не существует или неверный пароль!\n")
    while status != "q":
        displayMenu()
def lugemine(f:str,l:list):
    """info logins f listisse l
    """
    fail=open(f,"r") #,encloding="utf-8-sig"
    for rida in fail:
        l.append(rida.strip()) #"\n"
    fail.close()
    return l

def failisse_salvestamine(f:str,l:list):
    """Loetelu salvestamine failisse
    """
    fail=open(f,"w")
    for el in l:
        fail.write(el+"\n")
    fail.close()

def rida_salvestamine(f:str,rida:str):
    """Üks sõna või lause(rida) salvestame failisse
    :param str f: fail kuku salvastame
    :param str rida: sõna, mis vaja salvestada failisse
    """
    fail=open(f,"a")
    fail.write(rida+"\n")
    fail.close()


    rida_salvestamine("logins.txt", users)



