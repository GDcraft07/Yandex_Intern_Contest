# Мое решение прошло лишь 12 тестов, но в отличие от прошлого здесь основная проблема это алгоритм
# Его сложность: О(n * k), где n - это кол-во учеников, а k - это кол-во стран


number_of_countries = int(input())
minimum_income = list(map(int, input().split()))
availability_of_higher_education = list(map(int, input().split()))
children_of_citizens = list(map(int, input().split()))
number_of_classmates = int(input())
income = list(map(int, input().split()))
there_is_a_higher_education = list(map(int, input().split()))
citizenship_of_parents = list(map(int, input().split()))

countries = {}

for i in range(1, number_of_countries + 1):
    countries[str(i)] = [minimum_income[i - 1], availability_of_higher_education[i - 1], children_of_citizens[i - 1]]

classmates = {}

for i in range(1, number_of_classmates + 1):
    classmates[str(i)] = [income[i - 1], there_is_a_higher_education[i - 1], citizenship_of_parents[i - 1]]
ans = []
for _, i in classmates.items():
    country = '0'
    for name, item in countries.items():
        if (i[2] == int(name) and item[2]) or (i[0] >= item[0] and i[1]) or (i[0] >= item[0] and not item[1]):
            country = name
            break

    ans.append(country)

print(' '.join(ans))
