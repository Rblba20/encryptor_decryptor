import pyAesCrypt

print('Введите enc, если хотите зашифровать файл. Если хотите расшифровать файл, то введите dec.')
answer = input('Введите команду: ')
if answer == 'enc':
    password = input('Введите пароль для шифровки файла: ')
    # encrypt
    file = input('Введите путь до файла: ')
    name = input('Введите желаемое имя для зашифрованного файла(без расширения) : ')
    pyAesCrypt.encryptFile(file, name+'.txt.aes', password)
elif answer == 'dec':
    password = input('Введите пароль для расшифровки файла: ')
    file = input('Введите путь до файла: ')
    name = input('Введите желаемое имя для расшифрованного файла(без расширения) : ')
    # decrypt
    pyAesCrypt.decryptFile(file, name+'.txt', password)
else:
    print('Ошибка. Перезапустите программу.')
