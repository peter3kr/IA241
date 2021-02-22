"""
Lab 5 if statement 
"""

# 3.1
alien_color = 'red'

if alien_color == 'green':
    print('You just earned 5 points!')
    
    
# 3.2
alien_color = 'yellow'

if alien_color == 'green':
    print('You just earned 5 points!')
    
else:
    print('You just earned 10 points!')
    
    
# 3.3
favorite_fruits = ['Strawberry', 'Grape', 'Blueberry']

if 'Blueberry' in favorite_fruits:
    print('You really like Blueberries')
    
if 'Strawberry' in favorite_fruits:
    print('You really like Strawberries')
    
if 'Banana' in favorite_fruits:
    print('You really like Bananas')
    
    
# 3.4
age = 89

if age < 10:
    print('You are a kid')
elif age < 10:
    print('You are a teenager')
else:
    print('You are an adult')
    if age > 65:
        print('You are an elder')