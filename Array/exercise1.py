'''
Let us say your expense for every month are listed below,
January - 2200
February - 2350
March - 2600
April - 2130
May - 2190

Create a list to store these monthly expenses and using that find out,
1. In Feb, how many dollars you spent extra compare to January?
2. Find out your total expense in first quarter (first three months) of the year.
3. Find out if you spent exactly 2000 dollars in any month
4. June month just finished and your expense is 1980 dollar. Add this item to our monthly expense list
5. You returned an item that you bought in a month of April and
got a refund of 200$. Make a correction to your monthly expense list
based on this
'''

expense = [2200, 2350, 2600, 2130, 2190]

# Question 1. In Feb, how many dollars you spent extra compare to January?

q1 = expense[1]-expense[0]
print(q1)

# Question 2. Find out your total expense in first quarter (first three months) of the year.

q2 = expense[0]+expense[1]+expense[2]
print(q2)

# Question 3. Find out if you spent exactly 2000 dollars in any month

for exp in expense:
    if exp == 2000:
        print("$2000 have been spent.")


# Question 4. June month just finished and your expense is 1980 dollar. Add this item to our monthly expense list

exp = 1980

expense.append(exp)
print(expense)


# Question 5. You returned an item that you bought in a month of April and
# got a refund of 200$. Make a correction to your monthly expense list
# based on this

expense[3] = expense[3] - 200

print(expense)
