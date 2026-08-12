# import time

# for number in range(5):
#     if (number < 3):
#         continue
#     print(number)
# #    time.sleep(1)

# value = 0
# while value < 5:
#     print(value)
#     value += 1

value = 0
while True:
    value += 1
    if (value < 3):
        continue
    print(value)
    if (value>6):
        break