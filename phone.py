import os

filename = 'phon.txt'
fields = ['Фамилия', 'Имя', 'Телефон', 'Описание']

def saveData(filename, data): # функция сохранения данных в файл
    with open(filename, 'w', encoding='utf-8')as fout:
        for i in range(len(data)):
            s=''
            for v in data[i].values():
                s+= v + ','
            fout.write(f'{s[:-1]}\n')
    print('Данные обновлены')

def ReadData(filename: str): # Функция выгрузки данных в файл
    data = []
    with open(filename, 'w', encoding='utf-8')as fin:
        for line in fin:
            record = dict(zip(fields, line.strip().split(',')))
            data.append(record)
    return data

def PrintIndent (): # Функция вывода отступа для лучшей читаемости данных с консоли
    print()
    for i in range(20):
        print('_', end='')
    print()


def GetNewPerson(): # Функция добавления человека в базу
    phoneDirectory = ReadData(filename)
    newRecord = dict()
    for i in range(len(fields)):
        newRecord[fields[i]]=(input(f'Введите данные по полю "{fields[i]}": '))
    phoneDirectory.append(newRecord)
    saveData(filename, phoneDirectory)




def AskSearch(): # меню поиска данных
    while True:
        PrintIndent()
        print('Меню поиска')
        for i in range(len(fields)):
            print(f'{i} - поиск по полю {fields[i]}')
        print(f'{len(fields)} - выход в главное меню')
        answer = int(input('Введите номер меню: '))
        if answer == len(fields): break
        if 0 <= answer <len(fields):
            searched = input('Введите искомое значение')
            SearchData(searched, answer)



def RemRecord(): #Удаление записи по введенному индексу
    PrintAllData()
    recIndex = int(input('Введите номер удаляемой записи: '))-1
    phoneDirectory = ReadData(filename)
    phoneDirectory.pop(recIndex)
    saveData(filename, phoneDirectory)
    os.system('pause')

def ChangeRecord(): # меню изменения записи
    PrintAllData()
    recIndex = int(input('Введите номер редактируемой записи: '))-1
    print(*enumerate(fields))
    fieldsIndex = int(input('Введите номер поля для редактирования: '))
    phoneDirectory = ReadData(filename)
    phoneDirectory[recIndex][fields[fieldsIndex]] = input('Введите новые данные: ')
    saveData(filename, phoneDirectory)
    os.system('pause')

def PrintAllData(): # Функция вывода всех данных
    phoneDirectory = ReadData(filename)
    tick = 0
    PrintIndent()
    print('Данные справочника: ')
    for line in phoneDirectory:
        tick+=1
        print(f'{tick}', end=" ")
        print(*line.values())
    os.system('pause')

def SearchData(searchedData, fieldNum): # Функция поиска по определенному полю
    phoneDirectory = ReadData(filename)
    tick = 0
    PrintIndent()
    print('Результаты поиска: ')
    for line in phoneDirectory:
        tick+=1
        if searchedData.lower() in line[fields[fieldNum]].lower:
            find = True
            print(f'{tick}', end=" ")
            print(*line.values())
    if find == False: print(f'{searchedData} не найдена')



def ReadData(filename: str): # Функция выгрузки данных в файл
    data = []
    with open(filename, 'r', encoding='utf-8') as fin:
        for line in fin:
            record = dict(zip(fields, line.strip().split(',')))
            data.append(record)
    return data


def AskAction(): # Функция вывода главного меню
    while True:
        PrintIndent()
        print('Главное меню.\n'
              '0 - ввести новую запись \n'
              '1 - войти в меню поиска \n'
              '2 - вывести все данные \n'
              '3 - удалить запись из справочника \n'
              '4 - редактировать запись из справочника \n'
              '5 - выйти из программы \n'
              'Что вы хотите сделать?' , end='')
        answer = int(input())
        if answer == 5:
            return
        elif answer == 0:
            GetNewPerson()
        elif answer == 2:
            PrintAllData()
        elif answer == 1: 
            AskSearch()
        elif answer == 3: 
            RemRecord() 
        elif answer == 4:
            ChangeRecord 

AskAction()




