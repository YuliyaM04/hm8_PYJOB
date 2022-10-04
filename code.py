from itertools import count
from secrets import choice
import csv
import random
print("Добро пожаловать в мониторинг процесса работы сотрудников")

def main_menu ():
    print("\nМеню")
    print("1. Добавить сотрудника и информацию")
    print("2. Показать всех сотрудников")
    print("3. Поиск сотрудника по фамилии")
    print("4. Поиск сотрудника по кабинету")
    print("5. Поиск сотрудника по месту, которое он занимает")
    print("6. Выход")

    choice = input("Введите пункт: ")
    if choice == '1':
        newcontact()
        main_menu()
    elif choice == '2':
        with open('employee.csv',encoding = 'utf-8') as csvfile:
            spamreader = csv.DictReader(csvfile ,delimiter='|')
            for row in spamreader:
                user=[]
                id = row['ID']
                user=[row['Имя'] ,row['Фамилия'] ,row['Дата рождения'], row['Должность']]
                with open('cabinet.csv',encoding = 'utf-8') as csvfile:
                        spamreader2 = csv.DictReader(csvfile ,delimiter='|')
                        for row2 in spamreader2:
                            if row2['ID'] == id:
                                # user2 = [row2['Кабинет'], row2['Номер места'],row2['Оборудование']]
                                user.append(row2['Кабинет'])
                                user.append(row2['Номер места'])
                                user.append(row2['Оборудование'])
                                print("____________________________________")
                                print("Имя:"+user[0] + " Фамилия:"+user[1])
                              #print("Имя:"+user[0])
                                print("Дата рождения:"+user[2])
                                print("Должность:"+user[3])
                                print("Кабинет:"+user[4]+" Номер места:"+user[5])
        main_menu()
    elif choice == '3':
        lastn = input("Введите фамилию сотрудника для поиска?:")  
        with open('employee.csv',encoding = 'utf-8') as csvfile:
            spamreader = csv.DictReader(csvfile ,delimiter='|')
            for row in spamreader:
                if row['Фамилия'] == lastn:
                   id = row['ID']
                   with open('cabinet.csv',encoding = 'utf-8') as csvfile:
                        spamreader = csv.DictReader(csvfile ,delimiter='|')
                        for row in spamreader:
                            if row['ID'] == id:
                                print("НАЙДЕН СОТРУДНИК ПО ФАМИЛИИ ",str(lastn),"СИДИТ В : ", "Кабинете:", row['Кабинет'], "На месте:", row['Номер места'])
        main_menu()
    elif choice == '4':
        koko = input("Какой кабинет?:")
        with open('cabinet.csv',encoding = 'utf-8') as csvfile:
            spamreader = csv.DictReader(csvfile ,delimiter='|')
            for row in spamreader:
                if row['Кабинет'] == koko:
                    id = row['ID']
                    with open('employee.csv',encoding = 'utf-8') as csvfile:
                        spamreader = csv.DictReader(csvfile ,delimiter='|')
                        for row in spamreader:
                            if row['ID'] == id:
                                print("НАЙДЕН СОТРУДНИК В КАБИНЕТЕ",str(koko),":", row['Имя'] ,row['Фамилия'] ,row['Дата рождения'], row['Должность'])
        main_menu()
    elif choice == '5':
        mes = input("Какое место?:")
        with open('cabinet.csv',encoding = 'utf-8') as csvfile:
            spamreader = csv.DictReader(csvfile ,delimiter='|')
            for row in spamreader:
                if row['Номер места'] == mes:
                    id = row['ID']
                    with open('employee.csv',encoding = 'utf-8') as csvfile:
                        spamreader = csv.DictReader(csvfile ,delimiter='|')
                        for row in spamreader:
                            if row['ID'] == id:
                                print("НАЙДЕН СОТРУДНИК В КАБИНЕТЕ",str(mes),":", row['Имя'] ,row['Фамилия'] ,row['Дата рождения'], row['Должность'])
        main_menu()           
    elif choice == '6':
        print("Спасибо, что воспользовались мониторингом!")
    else:
        print("Пожалуйста, введите правильный пунк!")
        

def newcontact():
    randomka = random.randint(0,99)
    firstname = input("Введите имя сотрудника: ")
    lastname = input("Введите фамилию сотрудника: ")
    bithday = input("Введите дату рождения сотрудника: ")
    jobtitl = input("Введите должность сотрудника: ")
    cabinet = input("Введите кабинет: ")
    placenumber = input("Введите номер рабочего места: ")
    equipment = input("Введите оборудование, с которым работает сотрудник: ")
    zapis = [randomka,lastname, firstname,bithday,jobtitl]
    with open ('employee.csv', mode="a", encoding = 'utf-8') as csvfile:
        writer=csv.writer(csvfile,delimiter='|', lineterminator="\r")
        writer.writerow(zapis)
    zapis1 = [randomka,cabinet, placenumber, equipment]
    with open ('cabinet.csv', mode="a", encoding = 'utf-8') as csvfile:
        writer=csv.writer(csvfile,delimiter='|', lineterminator="\r")
        writer.writerow(zapis1)
    print("\n____________________________________________\nСотрудник:" + lastname + "\nуспешно сохранен.")

main_menu()
