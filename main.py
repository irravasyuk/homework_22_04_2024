# Завдання 1
# Реалізуйте базу даних зі штрафами податкової
# інспекції. Ідентифікувати кожну конкретну людину буде
# персональний ідентифікаційний код. В однієї людини може
# бути багато штрафів.
# Реалізуйте:
# 1. Повний друк бази даних;
# 2. Друк даних за конкретним кодом;
# 3. Друк даних за конкретним типом штрафу;
# 4. Друк даних за конкретним містом;
# 5. Додавання нової людини з інформацією про неї;
# 6. Додавання нових штрафів для вже існуючого запису;
# 7. Видалення штрафу;
# 8. Заміна інформації про людину та її штрафи.
# Використайте дерево для реалізації цього завдання.
import bintrees


class TaxFines:
    def __init__(self):
        self.database = bintrees.AVLTree()

    def print_database(self):
        for person_id, person_info in self.database.items():
            print(
                f"ID людини: {person_id}, Ім'я: {person_info['name']}, Місто: {person_info['city']}, Штраф: {person_info['fine']}")

    def print_person_info(self, person_id):
        if person_id in self.database:
            person_info = self.database[person_id]
            print(
                f"ID людини: {person_id}, Ім'я: {person_info['name']}, Місто: {person_info['city']}, Штраф: {person_info['fine']}")
        else:
            print('Людини з таким ID немає.')

    def print_type_tax(self, fine_type):
        for person_id, person_info in self.database.items():
            for fine in person_info['fine']:
                if fine['type'] == fine_type:
                    print(f'ID людини: {person_id}, Тип штрафу: {fine['type']}, Вартість: {fine['amount']}')

    def person_by_city(self, city):
        for person_id, person_info in self.database.items():
            if person_info['city'] == city:
                print(
                    f"ID людини: {person_id}, Ім'я: {person_info['name']}, Місто: {person_info['city']}, Штраф: {person_info['fine']}")

    def add_person(self, person_id, name, city):
        if person_id not in self.database:
            self.database[person_id] = {'name': name, 'city': city, 'fine': []}

        else:
            print('Людина з таким ID вже існує')

    def add_tax(self, person_id, fine_type, fine_amount):
        if person_id in self.database:
            self.database[person_id]['fine'].append({'type': fine_type, 'amount': fine_amount})
        else:
            print('Людини з таким ID немає.')

    def remove_tax(self, person_id, fine_index):
        fines = self.database[person_id]['fine']
        if person_id in self.database:
            if 0 <= fine_index < len(fines):
                fines.pop(fine_index)
            else:
                print('Ви щось ввели невірно.')
        else:
            print('Людини з таким ID немає.')

    def update_fine(self, person_id, fine_index, fine_type=None, fine_amount=None):
        if person_id in self.database:
            if 0 <= fine_index < len(self.database[person_id]['fine']):
                if fine_type is not None:
                    self.database[person_id]['fine'][fine_index]['type'] = fine_type
                if fine_amount is not None:
                    self.database[person_id]['fine'][fine_index]['amount'] = fine_amount
            else:
                print('Неправильний індекс штрафу')
        else:
            print('Людини з таким ID немає.')


tax_fines_db = TaxFines()

tax_fines_db.add_person('1234567890', 'Іван Петренко', 'Київ')
tax_fines_db.add_tax('1234567890', 'Перевищення швидкості', 100)
tax_fines_db.add_tax('1234567890', 'Паркування на тротуарі', 50)

tax_fines_db.add_person('0987654321', 'Марія Ковальчук', 'Львів')
tax_fines_db.add_tax('0987654321', 'Перевищення швидкості', 150)
tax_fines_db.add_tax('0987654321', 'Проїзд на червоне світло', 75)

print("Повна база даних:")
tax_fines_db.print_database()
print()

print("Інформація про особу з ID '1234567890':")
tax_fines_db.print_person_info('1234567890')
print()

print("Штрафи за 'Перевищення швидкості':")
tax_fines_db.print_type_tax('Перевищення швидкості')
print()

print("Особи з міста 'Львів':")
tax_fines_db.person_by_city('Львів')
print()

print("Видалення штрафу для особи з ID '1234567890':")
tax_fines_db.remove_tax('1234567890', 0)
print()

print("Оновлення штрафу для особи з ID '0987654321':")
tax_fines_db.update_fine('0987654321', 0, fine_type='Порушення правил паркування', fine_amount=120)
print()

print("Оновлена база даних:")
tax_fines_db.print_database()
