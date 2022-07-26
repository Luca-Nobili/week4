import http.client

host = input ('Inserire IP del sistema target: ')
porta = input('Inserire la pota del sitema target(default:80): ')

if(porta == ''):
	porta = 80
try:
	connessione = http.client.HTTPConnection(host, porta)
	connessione.request('OPTION','/phpMyAdmin/')
	risposta = connessione.getresponse()
	print('I metodi abilitati sono:',risposta.status,risposta.reason )
	connessione.close()
except ConnectionRefusedError:
	print('Connessione fallita')

