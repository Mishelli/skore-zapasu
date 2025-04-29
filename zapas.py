skore = []
for i in range (10):
    dalsi = input ("zadejte skore hráčů od 0 do 10")
    skore.append (dalsi)
print(skore)
prumer=sum (skore/10)
print (prumer)
print (min(skore))
print(max(skore))
