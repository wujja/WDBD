from snakebite.client import Client

cli = Client('localhost',9000)

for line in cli.text(['/mojkatalog/opowiesc.txt']):
	with open('nowy_plik.txt', 'w') as f:
		f.write(str(line))
