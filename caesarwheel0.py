#!usr/bin/env python3
#caesarwheel0.py

import random

base_wheel = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n',
'o','p','q','r','s','t','u','v','w','x','y','z']
print(list(enumerate(base_wheel)))
new_wheel = []

spinner = random.randint(0,25)
spinner_key = spinner

#populate reorganized base_wheel
for b in base_wheel:
	new_wheel.append(base_wheel[spinner])
	spinner -= 1

word = str(input('enter word: '))

my_letters = list(word.strip())
print(my_letters)
new_word_list = []

for k,v in list(enumerate(base_wheel)):
	if v in my_letters:
		new_word_list.append(new_wheel[k])

print(f'key: {spinner_key}\nnewspelling: {new_word_list}\nnew word:  ' +''.join(new_word_list))
