##ÜL 1
a = int(input('Sisestage esimene arv: '))
b = int(input('Sisestage teine arv: '))

even = []
numbers = [i for i in range(a, b+1) if i % 2 == 0]
print('Paarisarvud teie sisestatud arvude vahel on: ')
print(numbers)

print('----')
##ÜL 2
#1
num_words = 0
with open('kttekst.txt', 'r' )as f:
    for line in f:
        words = line.split()
        num_words += len(words)
print('Kttekst.txt failis on sõnu kokku: ')
print(num_words)

print('----')
#2
c = 0
with open('kttekst.txt', 'r' )as e:
    for line in e:
        words = line.split()
        c += len(words) > 5
print('Sõnade arv mis on väiksemad kui 5: ')
print(c)




    

        
