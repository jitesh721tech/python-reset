# age = 15

# if age > 18:
#     print("eligible")

# else:
#     print("no eligible")

# for n in range(1, 6):
#     print("heyyyyyyyy")

# def add(a, b):
#     return a + b 

# res = add(5, 5)
# print(res)

# ocm = 85
# sp = 59
# maths = 84
# hindi = 74
# eng = 77
# percentage = (ocm+sp+maths+hindi+eng)/3
# print(f"the total percentage is {percentage}")

# numbers = 1, 5, 6, 7, 8, 9

# for num in numbers:    
#     print(num)

# data = {
#     "name":"jitesh",
#     "age":23,
#     "course":"BCA"
# }

# print(data)

# expenses = [300, 250, 600, 785, 255, 900, 800]

# def calc_total():
#     t = sum(expenses)
#     print(f"Total Expenses: {t}")
# calc_total()    

# def calc_avg():
#     avg = sum(expenses)/len(expenses)
#     print(f"Avergae of Expenses: {avg}")
# calc_avg()

# def find_highest():
#     high = max(expenses)
#     print(f"heighest Expenses: {high}")
# find_highest()

# def find_lowest():
#     low = min(expenses)
#     print(f"lowest Expenses: {low}")
# find_lowest()

# def find_count():
#     count = len(expenses)
#     print(f"count of Expenses: {count}")
# find_count()

# def calc_total(expenses):
#     if len(expenses) == 0:
#         return None
#     return sum(expenses)

# def calc_avg(expenses):
#     if len(expenses) == 0:
#         return None
#     return sum(expenses)/len(expenses)

# def calc_max(expenses):
#     if len(expenses) == 0:
#         return None
#     return max(expenses)

# def calc_min(expenses):
#     if len(expenses) == 0:
#         return None
#     return min(expenses)

# def calc_above_limit(expenses, limit):
#     count = 0
#     for num in expenses:
#         if num > limit:
#             count+=1
#     return count
    
# expenses = [200, 400, 500, 600, 700, 800]
# print(f"total:{calc_total(expenses)}")    
# print(f"average:{calc_avg(expenses)}")
# print(f"max:{calc_max(expenses)}")
# print(f"min:{calc_min(expenses)}")
# print(f"above limit:{calc_above_limit(expenses, 500)}")


transactions = [
    {"category": "Food", "amount": 500},
    {"category": "Travel", "amount": 300},
    {"category": "Food", "amount": 200},
    {"category": "Shopping", "amount": 1000},
    {"category": "Travel", "amount": 150}
]


def category_total(transactions):

    totals = {}

    for transaction in transactions:

        category = transaction["category"]
        amount = transaction["amount"]

        if category in totals:
            totals[category] += amount

        else:
            totals[category] = amount

    return totals


result = category_total(transactions)

print(result)








