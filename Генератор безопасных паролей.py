from random import *

def generate_password(lenght, chars):
    # Другой вариант: return sample(chars, lenght)
    password = ''
    for i in range(lenght):
        password += choice(chars)
    return password

digits = '0123456789'
lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
punctuation = '!#$%&*+-=?@^_'

chars = ''

n = int(input('Введите количество паролей для генерации\n'))
len_pass = int(input('Введите длину одного пароля\n'))
dig_pass = input(
    'Включать ли цифры 0123456789? (д - да, н - нет)\n')
upp_pass = input(
    'Включать ли прописные буквы ABCDEFGHIJKLMNOPQRSTUVWXYZ? (д - да, н - нет)\n')
low_pass = input(
    'Включать ли строчные буквы abcdefghijklmnopqrstuvwxyz? (д - да, н - нет)\n')
pun_pass = input(
    'Включать ли символы !#$%&*+-=?@^_? (д - да, н - нет)\n')
amb_pass = input(
    'Исключать ли неоднозначные символы il1Lo0O? (д - да, н - нет)\n')

if dig_pass.lower() == 'д':
    chars += digits
if upp_pass.lower() == 'д':
    chars += uppercase_letters
if low_pass.lower() == 'д':
    chars += lowercase_letters
if pun_pass.lower() == 'д':
    chars += punctuation
if amb_pass.lower() == 'д':
    for c in 'il1Lo0O':
        chars = chars.replace(c, '')

print('Сгенерированные пароли:')
for i in range(n):
    print(generate_password(len_pass, chars), sep='')