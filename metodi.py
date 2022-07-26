import http.client

host = input ('Inserire IP del sistema target: ')
porta = input('Inserire la pota del sitema target(default:80): ')

if(porta == ''):
	porta = 80
try:
	connection = http.client.HTTPConnection(host, porta)
	connection.request('OPTION', '/phpMyAdmin/')
	response = connection.getresponse()
	print('I metodi abilitati sono:',response.status,response)
	connection.close()
except ConnectionRefusedError:
	print('Connessione fallita')

