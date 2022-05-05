from snakebite.client import Client

cli = Client('localhost',9000)

for dr in cli.delete(['/detective_stories'], recurse=True):
	print(dr)
