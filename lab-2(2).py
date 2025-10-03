cities = input("Введите города:").split()

i = 0
result = []
while i<len(cities):
    result.append(cities[i])
    i += 2

print("Через один:", result)
print("Количество городов:", len(cities))