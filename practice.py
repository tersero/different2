current_contacts = {}
while True:
    print("Текущие контакты на телефоне:")
    if current_contacts:
        for name in current_contacts:
            print(name, current_contacts[name])
    else:
        print("<Пусто>")
    new_contact = input("Введите имя (для остановки введите пустую строку): ")
    new_telephone = int(input("Введите номер телефона: "))
    if new_contact in current_contacts:
        print("Ошибка: такое имя уже существует.")
    else:
        current_contacts[new_contact] = new_telephone