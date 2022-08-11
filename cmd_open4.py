from subprocess import Popen

print(100 * '-')
print('Программа для автоматического запуска пингования хостов')
while True:
    print(100 * '-')
    print('Введите последние цифры IP адреса компьютера или сервера,')
    last_digits = input('например: 200 (завершить - введите 0): ')
    if last_digits == '0':
        print(100 * '-')
        print('Программа завершена')
        break
    print('Старт пинга хоста 192.168.1.' + last_digits)
    full_ip = 'start ping -t 192.168.1.' + last_digits
    # print(full_ip)
    p = Popen(full_ip, shell=True)

