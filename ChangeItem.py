import DGStorage as DGS
dbHandle=DGS.DGStorage()
dbHandle.select('YourDataCollection')
ok=False
i=0
while ok==False:
	res=dbHandle.fetch(1,(i-1)*1)
	i+=1
	if len(res)==0:
		ok=True
	for item in res:
		pass
		#Do something with item
