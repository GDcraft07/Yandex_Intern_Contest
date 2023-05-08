# Моё решение прошло лишь 15 тестов

def search_increasing_subarrays(arr):
    result = []
    count_result = []
    temp = [arr[0]]
    temp_count = [1]
    for count in range(1, len(arr)):
        if len(temp) != 1:
            if arr[count] >= arr[count - 1]:
                temp.append(arr[count])
                temp_count.append(count + 1)
            else:
                if len(temp) > 1:
                    result.append(temp)
                    count_result.append(temp_count)
                temp = [arr[count]]
                temp_count = [count + 1]
        else:
            if arr[count] > arr[count - 1]:
                temp.append(arr[count])
                temp_count.append(count + 1)
            else:
                if len(temp) > 1:
                    result.append(temp)
                    count_result.append(temp_count)
                temp = [arr[count]]
                temp_count = [count + 1]
    if len(temp) > 1:
        result.append(temp)
        count_result.append(temp_count)
    return [result, count_result]


def subtraction(nums):
    return nums[-1] / nums[0]


number_of_days = int(input())
price_of_one_share = list(map(int, input().split()))

increasing_price = search_increasing_subarrays(price_of_one_share)

ans_count = 0
ans_num = []
price_difference = list(map(subtraction, increasing_price[0]))

for i in range(2):
    if price_difference:
        index_max_price_difference = price_difference.index(max(price_difference))
        ans_count += 1
        ans_num.append([str(increasing_price[1][index_max_price_difference][0]),
                        str(increasing_price[1][index_max_price_difference][-1])])
        increasing_price[0].pop(index_max_price_difference)
        increasing_price[1].pop(index_max_price_difference)
        price_difference.pop(index_max_price_difference)

ans_num = sorted(ans_num, key=lambda x: x[0])

print(ans_count)

for i in ans_num:
    print(' '.join(i))
