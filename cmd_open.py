from pythonping import ping

host_ip_list = ['192.168.1.71', '192.168.1.72', '192.168.1.200']
for host_ip in host_ip_list:
    response_list = ping(host_ip, size=40, count=10)
    if response_list.rtt_avg_ms >= 2000:
        print('Хост {} недоступен'.format(host_ip))
    else:
        print('Время отклика до хоста {0} составляет {1} мс'.format(host_ip, response_list.rtt_avg_ms))

ping('8.8.8.8', verbose=True)