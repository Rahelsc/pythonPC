user_id = input('enter your id')
weights = []
sum_of_digits = 0
if len(user_id) > 9:
    print('sorry your id is too long')
else:
    user_id = '0' * (9 - len(user_id)) + user_id
    for x in range(0, len(user_id)):
        weights.append(1) if x % 2 == 0 else weights.append(2)  # calculating the weight of each digit in the id number

    for num_id, weight in zip(user_id, weights):  # traversing list of weights and the id itself
        # adding the digits of the resulting number into a single digit number and adding that to our sum:
        sum_of_digits += (int(num_id) * weight) % 10 + (int(num_id) * weight) // 10

    print('your id is valid') if sum_of_digits % 10 == 0 else print('the id you have entered is invalid')

    '''
    I found that the method for calculating the validity of an id number is as follows:
    you first calculate the weight of each digit in the id number. in the following pattern 1, 2, 1 ...
    then you multiply each digit with its weight and sum up the result of the resulting digits 
    
    then the sum of all sums is divided by 10, and if it's without a remainder it means that it's a valid id
    '''
