from logger import logging
import model as m
import check_in

def menu():
    print()
    print('Журнал заметок открыт!\n')
    logging.info('Start program')
    while True:
        type_num = input('\n*****Главное меню*****\nВыберите пункт меню:\n'
                         '1 - Показать все записи\n'
                         '2 - Найти запись\n'
                         '3 - Добавить запись\n'
                         '4 - Редактировать запись\n'
                         '5 - Удалить запись\n'
                         '0 - Выход\n')
        type_num = check_in.check_type_num(type_num)

        if type_num not in range(6):
            logging.error('Error: wrong main menu selection')
            print("Ошибка! Выберите пункт меню!\n")
             

        if type_num == 1:  # показать все записи
            print('Список всех заметок')
            m.get_table('Note.csv')
            print('Вы будете перемещены в главное меню.\n')
          

        if type_num == 2:  # найти запись
            input_value = input('Введите данные для поиска: ').lower()
            find_list_id = m.find_info('Note.csv', input_value)
            if len(find_list_id) == 0:
                print('По вашему запросу ничего не найдено')
            else:
                print('Информация по вашему запросу.')
            print('Вы будете перемещены в главное меню.\n')
           

        if type_num == 3:  # добавить запись
            print('Добавление новой записи...')
            m.add_text('Note.csv')
            print('Вы будете перемещены в главное меню.\n')
        

        if type_num == 4:  # редактировать запись
            input_value = input('Введите данные для поиска: ').lower()
            find_list_id = m.find_info('Note.csv', input_value)

            if len(find_list_id) == 0:
                print('По вашему запросу ничего не найдено')
            else:
                print('Информация по вашему запросу.')  
                note_id = input('Введите id записи, данные которой вы хотите изменить:\n')
                checked_note_id = check_in.check_type_num(note_id)

                if checked_note_id == -1:
                    logging.error('Error: incorrect id entered.')
                    print('Введено некорректное значение. Попробуйте ещё раз!')
                else:  
                    existed_note_id = check_in.check_id_exist(checked_note_id, find_list_id)
                    if existed_note_id == -1:
                        logging.error('Error: incorrect id entered.')
                        print('Ошибка ввода id заметки. Попробуйте ещё раз!')
                    else:
                        operation = input('\nКакие изменения вы хотите внести:\n'
                                    '1 - Изменить заметку\n'
                                    '2 - Изменить статус заметки\n'
                                    '3 - Изменить все данные\n')
                        checked_operation = check_in.check_type_num(operation)
                        if checked_operation in range(1, 4):
                            m.change_info('Note.csv', existed_note_id, checked_operation)
                        else:
                            logging.error('Error: wrong submenu selection')
                            print("Ошибка! Выберите пункт меню!")
            print('Вы будете перемещены в главное меню.\n')
            

        if type_num == 5:  # удалить запись
            input_value = input('Введите данные для поиска: ').lower()
            find_list_id = m.find_info('Note.csv', input_value)

            if len(find_list_id) == 0:
                print('По вашему запросу ничего не найдено.')
            else:
                print('Информация по вашему запросу.') 
                note_id = input('Введите id записи, которую хотите удалить:\n')
                checked_note_id = check_in.check_type_num(note_id)
                if checked_note_id == -1:
                    logging.error('Error: incorrect id entered.')
                    print('Введено некорректное значение. Попробуйте ещё раз!')
                else:   
                    existed_note_id = check_in.check_id_exist(checked_note_id, find_list_id)
                    if existed_note_id == -1:
                        logging.error('Error: incorrect id entered.')
                        print('Ошибка ввода id заметки. Попробуйте ещё раз!')
                    else:
                        m.delete_info('Note.csv', existed_note_id)
            print('Вы будете перемещены в главное меню.\n')
                

        if type_num == 0:  # выход
            logging.info("Stop program")
            print('Работа с журналом заметок окончена!\n')
            break

