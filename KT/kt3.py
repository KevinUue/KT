##ÜL3
numbrid1 = [11,15,6,13,13,25,32,11,20,5,31,16,32,29,11,13,3,29,28,24]
numbrid2 = [5,19,16,4,12,7,2,28,34,29,29,36,6,8,24,18,31,7,1,7]

#1
print('Ühised arvud listides on: ')
for a in numbrid1:
    for b in numbrid2:
        if a==b:
            print(a)
print('----')

#2
print('Kahe listi suurim number on: ')
print(max(numbrid1 + numbrid2))

print('----')

#3
print('Kahe listi väikseim number on: ')
print(min(numbrid1 + numbrid2))

print('----')

#4
summa = sum(numbrid1)
keskmine = summa / 20
print('Esimese listi arvude keskmine on: ')
print(keskmine)
print('')
summa2 = sum(numbrid2)
keskmine2 = summa2 / 20
print('Teise listi arvude keskmine on: ')
print(keskmine2)
print('----')

#5
summa3 = summa + summa2
keskmine3 =  summa3 / 40
print('Mõlema listi arvude keskmine on:')
print(keskmine3)


