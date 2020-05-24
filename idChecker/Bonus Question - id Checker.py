user_id = input('enter your id')
weights = []
sum_of_digit = 0
if len(user_id) > 9:
    print('sorry your id is too long')
else:
    user_id = '0' * (9 - len(user_id)) + user_id
    for x in range(0, len(user_id)):
        weights.append(1) if x % 2 == 0 else weights.append(2)

for num_id, weight in zip(user_id, weights):
    sum_of_digit += int(num_id) * weight

print('invalid id') if sum_of_digit % 10 == 0 else print('valid id')
