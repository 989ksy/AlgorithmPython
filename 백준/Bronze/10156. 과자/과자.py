a, b, c = map(int, input().split())

money_pay = a * b
money_parent = (money_pay) - c

print(money_parent if c < money_pay else 0)