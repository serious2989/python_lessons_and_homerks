from err_check import check_new_data
from work import *
from export import *


def menu():
    while True:
        read_all()
        print(f"Hogwarts School \n{'*' * 20}")
        actions = input("1. Показать все записи\n"
                        "2. Найти запись\n"
                        "3. Добавить запись\n"
                        "4. Редактировать запись\n"
                        "5. Удалить запись\n"
                        "6. Импортировать/Экспортировать\n"
                        "7. Выход\n")
        match actions:
            case "1":
                print_all()
            case "2":
                find_entry(input("Введите имя или номер телефона(11 цифр): "), read_all())
            case "3":
                add_entry(add_menu())
            case "4":
                print_all()
                id_change = input(f"Enter the id: ")
                if find_entry(id_change, read_all()) and (answer := edit_menu()):
                    edit_entry(answer, id_change)
            case "5":
                del_entry(input("Введите имя или номер телефона(11 цифр): "))
            case "6":
                import_export_menu()
            case "7":
                logging.info("Остановка программы.\n")
                print("До свидания! Ждем Вас снова!")
                break
            case _:
                logging.warning(f"Main menu, wrong item selected.")
                print("The data is not recognized, repeat the input.")


def add_menu():
    logging.info('Start add menu')
    add_dict = {"id": "1", "name": "", "surname": "", "phone": "", "description": ""}
    for i in add_dict:
        if i != "id":
            add_dict[i] = check_new_data(i)
    logging.info('Stop edit menu')
    return add_dict


def edit_menu():
    add_dict = {"1": "name", "2": "surname", "3": "phone", "4": "description"}
    logging.info('Start edit menu')
    while True:
        print("\nChanging:")
        change = input("1. Имя\n"
                       "2. Фамилия\n"
                       "3. телефон\n"
                       "4. описание\n"
                       "5. Выход\n")

        match change:
            case "1" | "2" | "3" | "4":
                type_date = add_dict[change]
                return type_date, check_new_data(type_date)
            case "5":
                logging.info('Exited the edit menu')
                return 0
            case _:
                logging.warning(f"Edit menu, wrong item selected.")
                print("The data is not recognized, repeat the input.")


def import_export_menu():
    logging.info('Start import/export menu')
    while True:
        print("\nImport\\Export:")
        change = input("1. import file\n"
                       "2. export file\n"
                       "3. exit\n")
        match change:
            case "1":
                file_import(input(f"Enter the database name: "))
                return
            case "2":
                while True:
                    logging.info('Start choose a format menu')
                    format_type = input(f"Choose a format:\n"
                                        f"1. CSV\n")                
                    match format_type:
                        case "1":
                            save_csv(input("Enter the name of the file: "))
                            return
                       
                        case "4":
                            logging.info('Exited the choose a format menu')
                            return
                        case _:
                            logging.warning(f"Choose a format menu, wrong item selected.")
                            print("The data is not recognized, repeat the input.")

            case "3":
                logging.info('Exited the import/export menu')
                break
            case _:
                logging.warning(f"Import/export menu, wrong item selected.")
                print("The data is not recognized, repeat the input.")
