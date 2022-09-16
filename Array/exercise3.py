'''
Create a list of all odd numbers between 1 and a max number. Max number is something you need to take from a user using input() function
'''

print(f"please enter the number : ")
number = int(input())
odd_number = []
for i in range(1, number):
    if i % 2 != 0:
        odd_number.append(i)
print(odd_number)