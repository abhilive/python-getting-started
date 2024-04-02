menus = {
    'Breakfast': ['Egg Sandwich', 'Bagel', 'Coffee'],
    'Lunch': ['BLT', 'PB&J', 'Turkey Sandwich'],
    'Dinner': ['Soup', 'Salad', 'Spaghetti', 'Taco']
}

# print('Breakfast Menu:\t', menus['Breakfast'])
# print('Lunch Menu:\t', menus['Lunch'])
# print('Dinner Menu:\t', menus['Dinner'])

for name, menu in menus.items():
    print(name, ":", menu)

person = {'name': 'Sarah Smith',
          'city': 'Orlando',
          'age': 100 }

print(person.get('name'), 'is', person.get('age'), 'years old')
