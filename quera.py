n=int(input('enter n'))
list_of_k=[]
for i in range(n):
    kalameh=input('enter kalameh')
    list_of_k.append(kalameh)

n_kalameh=[]    
if len(list_of_k)<=1000:
    for i in list_of_k:
        n_kalameh.append(i)

for i in n_kalameh[::-1]:
    print(i)       

