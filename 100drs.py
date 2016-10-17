import string


szamok_list = ['close']*100


for n in range (1,100):
    
    for j in range(n,100,n):
    
        if szamok_list[j] == 'close':
            szamok_list[j] = 'open'
        elif szamok_list[j] == 'open':
            szamok_list[j] = 'close'

for x in range(1,100):
        if szamok_list[x] == 'open':
            print (x)

