number = int(input())
count = 0
current_number = number
biggest_jump = 0
while number != 0:
    if current_number > number:
        biggest_jump = current_number
    count += 1
    current_number = number
    number = int(input())

print(count)
print(biggest_jump)
