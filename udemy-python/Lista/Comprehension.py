frutas1 = ['Abacate', 'banana', 'morango', 'kiwi', 'abacaxi']
''''
frutas2 =  []

for item in frutas1:
    if 'b' in item:
        frutas2.append(item)
'''
frutas2 = [iten for iten in frutas1 if 'k' in iten]
print(frutas2)