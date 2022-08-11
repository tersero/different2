from subprocess import Popen


while True:
    last_digits = input('Введите последние цифры IP адреса сервера, например: 200 (завершить - введите 0) ')
    if last_digits == '0':
        print('Программа завершена')
        break
    full_ip = 'start ping -t 192.168.1.' + last_digits
    print(full_ip)
    p = Popen(full_ip, shell=True)

