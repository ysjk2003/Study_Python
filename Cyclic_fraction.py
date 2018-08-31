#-*- coding:utf-8 -*-
x = float(input("소수 입력"))

start, term = map(int, input("순환이 시작되는 소수자리와 순환되는 숫자의 개수 입력").split())

coe_a, coe_b = 10 ** (start+term-1), 10 ** (start-1)

molec = round(x * coe_a - x * coe_b)
denom = coe_a - coe_b

print(molec,"/", denom)