valores = [10, 15, 20, 35, 40, 45, 50]

'''def remove20(x):
    return x > 20;

# print(remove20, valores)

print(list(filter(remove20, valores)))
'''
print(list(filter(lambda x: x > 20, valores)))