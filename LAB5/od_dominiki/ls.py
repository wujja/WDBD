from snakebite.client import Client

cli = Client('localhost',9000)
for x in cli.ls(['/']):
	print(x)
