# Моё решение прошло все тесты

number_of_keys = int(input())
character_identifiers = list(map(int, input().split()))
row_numbers = list(map(int, input().split()))
number_of_characters_in_the_abstract = int(input())
the_identifiers_of_the_abstract = list(map(int, input().split()))

ans = 0

character_and_row = {}

for i in range(number_of_keys):
    character_and_row[str(character_identifiers[i])] = row_numbers[i]

for i in range(1, number_of_characters_in_the_abstract):
    row_now = character_and_row[str(the_identifiers_of_the_abstract[i])]
    row_late = character_and_row[str(the_identifiers_of_the_abstract[i - 1])]
    if row_late != row_now:
        ans += 1

print(ans)