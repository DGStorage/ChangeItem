import DGStorage as DGS
dbHandle=DGS.DGStorage()
dbHandle.select('YourDataCollection')
ok=False
i=0
while ok==False:
	res=dbHandle.fetch(20,(i-1)*20)
	if len(res)==0:
		ok=True
	for item in res:
		#Do something with item
