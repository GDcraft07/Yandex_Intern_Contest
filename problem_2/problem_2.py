# Моё решение прошло все тесты

number_of_sculptures, ideal_mass, times = list(map(int, input().split()))
masses_of_sculptures = list(map(int, input().split()))

mass = []

for count, i in enumerate(masses_of_sculptures):
    mass.append([abs(ideal_mass - i), count])

sorted_mass = sorted(mass, key=lambda x: x[0])


count_sculpture = 0
index_sculpture = []

for i in sorted_mass:
    times -= i[0]
    if times >= 0:
        count_sculpture += 1
        index_sculpture.append(i[1] + 1)
    else:
        break

print(count_sculpture)
if index_sculpture:
    print(' '.join(list(map(str, index_sculpture))))
