"""
List Comprehension exercise for Python - by Sean Fagan.

If you make it to the end of this exercise, you will officially know *too*
much about list comprehensions. Out in the real world, remember to always favor
clarity over cleverness.
"""

apt_animals = {
    101: [('harry', 'cat')],
    102: [('kenneth', 'cat'), ('russell', 'fish')],
    103: [('deborah', 'dog'), ('christopher', 'dog')],
    104: [('thomas', 'arachnid'), ('debra', 'arachnid'), ('doug', 'arachnid')],
    201: [('linda simmons', 'cat')],
    202: [('debra', 'dog')],
    203: [('cherry', 'fish')],
    204: [('nancy drew', 'fish'), ('drew nancy', 'fish')],
    301: [],
    302: [('gregory', 'cat'), ('pamela', 'dog')],
    303: [('debra', 'ferret'), ('tammy', 'snake')],
    304: [('harry', 'dog')]
}

# Using a single list comprehension on apt_animals, try and...

# 1. Build a list of all apartment numbers (no need to sort)
#    [101, 102, 103, ...]
apt_nums = []

print 'apt_nums:', apt_nums

# 2. USING CONDITIONALS
#    Build a list of all the apartment numbers on the third floor
#    [301, 302, 303, ...]
third_floor_apt_nums = []

print 'third_floor_apt_nums:', third_floor_apt_nums

# 3. ACCESSING THE DICTIONARY KEY'S VALUE
#    Build a list of all the apartment numbers with more than one pet
#    [204, 102, 103, ...]
multi_pet_apts = []

print 'multi_pet_apts:', multi_pet_apts

# 4. NESTING FOR LOOPS
#    Build a *flat* list of all the animal names (duplicates ok)
#    ['linda simmons', 'debra', 'cherry', ...]
all_animal_names = []

print 'all_animal_names:', all_animal_names

# 5. COMBINING NESTED LOOPS WITH CONDITIONALS
#    Build a list of all the animal types with the name 'debra' (duplicates ok)
#    ['dog', 'arachnid', ...]
debra_animals = []

print 'debra_animals:', debra_animals

# 6. Build a list of all the fish names that live on the second floor
#    ['cherry', 'nancy drew', ...]
second_floor_fish_names = []

print 'second_floor_fish_names:', second_floor_fish_names
