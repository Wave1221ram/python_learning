import math

# Test Credit Card Account Numbers:
# American Express 378282246310005
# American Express 371449635398431
# American Express Corporate 378734493671000
# Australian Bankcard 5610591081018250
# Diners Club 30569309025904
# Diners Club 38520000023237
# Discover 6011111111111117
# Discover 6011000990139424
# JCB 3530111333300000
# JCB 3566002020360505
# MasterCard 5555555555554444
# MasterCard 5105105105105100
# Visa 4111111111111111
# Visa 4012888888881881

# Python credit card validator program

# 1. Remove any '-' or ' '
# 2. Add all digits in the odd places from right to left
# 3. Double every second digit from right to left.
#        (If result is a two-digit number,
#        add the two-digit number together to get a single digit.)
# 4. Sum the totals of steps 2 & 3
# 5. If sum is divisible by 10, the credit card # is valid

# credit_card = input("Please enter your credit card: ").replace(" ", "").replace("_", "")
credit_card = "378282246310005"
# 50162883
# 0034227
# 0 + 0 + 6 + 8 + 4 + 4 + 14 = 36

print(credit_card)
odd_digits_sum = sum(int(credit_card[i]) for i in range(len(credit_card)-1, -1, -2))
# odd_digits_sum = sum(int(credit_card[i]) for i in range(len(credit_card)-2, -1, -2))
print(odd_digits_sum)

odd_digits_sum = sum( (math.floor(double_val/10) + double_val%10 if (double_val := (int(credit_card[i]) * 2)) > 10 else double_val) for i in range(len(credit_card)-2, 0, -2))
print(odd_digits_sum)

odd_digits_sum = sum(math.floor(int(credit_card[i]) * 2 / 10) + (int(credit_card[i]) * 2) % 10 for i in range(len(credit_card)-2, 0, -2))
print(odd_digits_sum)


odd_digits_sum = sum(math.floor(i / 10) + (i) % 10 for i in (credit_card[-1::-1]) * 2)
print(odd_digits_sum)
    
credit_card[-1::-1]





# odd_digits_sum = sum( (math.floor(double_val/10) + double_val%10 if (double_val := (int(credit_card[i]) * 2)) > 10 else double_val) for i in range(len(credit_card)-2, 0, -2))
# double_val[0] + double_val[1] if double_val := (int(credit_card[i]) * 2) > 10 else double_val






# sum_odd_digits = 0
# sum_even_digits = 0
# total = 0

# # Step 1
# card_number = input("Enter a credit card #: ")
# card_number = card_number.replace("-", "")
# card_number = card_number.replace(" ", "")
# card_number = card_number[::-1]

# # Step 2
# for x in card_number[::2]:
#     sum_odd_digits += int(x)

# # Step 3
# for x in card_number[1::2]:
#     x = int(x) * 2
#     if x >= 10:
#         sum_even_digits += (1 + (x % 10))
#     else:
#         sum_even_digits += x

# # Step 4
# total = sum_odd_digits + sum_even_digits

# # Step 5
# if total % 10 == 0:
#     print("VALID")
# else:
#     print("INVALID")