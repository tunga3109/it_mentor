person_data = {
    'имя': 'Иван',
    'возраст': 25,
    'пол': 'мужской',
    'рост': 180,
    'вес': 75,
}



print("Данные о человеке:")
for key, value in person_data.items():
    print(f"{key}: {value}")

person_data['размер ноги'] = 43

del person_data['возраст']

print("Данные о человеке:")
for key in person_data:
    print(f'{key}: {person_data[key]}')