from snakebite.client import Client

cli = Client('localhost',9000)

for f in cli.copyToLocal(['/mojkatalog/opowiesc.txt'], '/tmp'):
	print(f)
