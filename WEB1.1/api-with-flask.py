my_info = {
    'name': 'Fluffy',
    'likes': ['tennis balls', 'walks'],
    'address': {
        'street': '555 Post St',
        'city': 'San Francisco'
    },
    'age': 3,
    'favorite_fruits': [
        'kumquat',
        'peach',
        'dragonfruit',
        'cantaloupe',
        'lemon'
    ],
    'instructors': [
        {
            'name': 'Dani',
            'subject': 'obedience'
        },
        {
            'name': 'Mitchell',
            'subject': 'tricks'
        }
    ]
}

name = my_info['name']
print(f'Hello! My name is {name}.')

street_address = my_info['address']['street']
print(f'I\'m a Make School student and I live at {street_address}.')

# TODO 2: Fill in code to get the fruit at index 0 of the 'favorite_fruits' list
favorite_fruit = my_info['favorite_fruits'][0]
print(f'My ALL TIME favorite fruit is {favorite_fruit}.')

# # TODO 3: Fill in code to get the fruit at index 2 of the 'favorite_fruits' list
third_fave_fruit = my_info['favorite_fruits'][2]
print(f'If I can\'t have that, I guess I\'ll settle for {third_fave_fruit}.')

# # TODO 4: Fill in code to get the NAMES of instructors in the 'instructors' list
instructor_1_name = my_info['instructors'][0]['name']
instructor_2_name = my_info['instructors'][1]['name']
print(
    f'My instructors at Make School are {instructor_1_name} and {instructor_2_name}.')
