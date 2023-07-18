from data_create import input_user_data


def input_data():
    name, surname, phone, adress = input_user_data()
    var = int(input(f'\nВ каком виде записать данные?\n'
                    f'1 Вариант: \n'
                    f'{name}\n'
                    f'{surname}\n'
                    f'{phone}\n'
                    f'{adress}\n\n'
                    f'2 Вариант: \n'
                    f'{name};{surname};{phone};{adress}\n\n'
                    f'Ваш выбор:'))

    if var == 1:
        with open('data_first_variant.csv', 'a', encoding='utf-8') as file:
            file.write(f'{name}\n'
                       f'{surname}\n'
                       f'{phone}\n'
                       f'{adress}\n\n')
    else:
        with open('data_second_variant.csv', 'a', encoding='utf-8') as file:
            file.write(f'{name};{surname};{phone};{adress}\n\n')

    print(f'Данные добавлены в {var} файл')


def print_data():
    print('1 файл: ')
    with open('data_first_variant.csv', 'r', encoding='utf-8') as file:
        data = file.readlines()
        data_list = list()
        j = 0
        for i in range(len(data)):
            if data[i] == '\n':
                data_list.append(''.join(data[j:i]))
                j = i
        print(''.join(data_list))

    print('2 файл: ')
    with open('data_second_variant.csv', 'r', encoding='utf-8') as file:
        data = list(file.readlines())
        print(''.join(data))            
            
        
'''
Подскажите пожалуйста как реализовать возможность удаления данных в телефонном справочнике?
Если бы контакты были записаны в списке, то вроде понятна логика. 
А вот как удалять данные из файлов data_first_variant.csv и data_second_variant.csv я не совсем понимаю(
Заранее спасибо за помощь
'''

# def delete_data():
#     print("Введите контакт: ")
#     name1 = input('> ')
#     for contact in contacts:
#         if contact['name'] == name1:
#             print("Вы хотите удалить контакт %s (yes/no)?: " % name )
#             name_del = input('> ')
#             if name_del == 'yes':
#                contacts.remove(contact)
#                print("Вы удалили контакт %s " % name)           
            
#     contacts = [
#     {
#         "name": "Женя",
#         "phone": "7939687"
#     },
#     {
#         "name": "Коля",
#         "phone": "7967011"
#     },
#     {
#         "name": "Аня",
#         "phone": "6405861"
#     },
# ]