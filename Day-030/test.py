#KeyError
# dictionary = {'Key': 'value'}
# value = dictionary['no_key']

#IndexError
# fruit_list = ['apple', 'pear','mango']
# fruit = fruit_list[4]

#TypeError
# text = 'hello'
# print(text + 5)

# try: something that might cause an exception
# except: do this if there was an exception
# else: do this if there were no exceptions
# finally: do this no matter what happens

#FileNotFound
# try:
#     file = open('data.txt')
#     asd = {'key': 'value'}
#     print(asd['key'])
# except FileNotFoundError:
#     print('file')
#     # with open('data.txt', 'w') as file:
#     #     file.write('newly created')
# except KeyError as error_message:
#     print(f'the key {error_message} doesn\'t exist')
# else:
#     content = file.read()
#     print(content)
# finally:
#     # file.close()
#     # print('File was closed.')
#     raise KeyError

height = float(input('Height: '))
weight = float(input('Weight: '))

if height > 3:
    raise ValueError('Human height should not be over 3 meters.')
    
bmi = weight / height ** 2
print(bmi)