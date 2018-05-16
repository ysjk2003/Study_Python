#-*- coding:utf-8 -*-
'''
age = input("나이를 입력하세요 : ")
if age>=20:
	print("party tonight")   #괄호를 써도 되고 안써도 됨
else:
	print("study tonight")
'''
#파이썬의 코드 구분은 "들여쓰기"로 수행된다.
#함수, 조건, 반복 구조 등 내포가 필요한 구문은
#콜론으로 구분한다

'''
age = input("나이를 입력하세요 : ")
if age>=20: print("party tonight")   #괄호를 써도 되고 안써도 됨
else: print("study tonight")
'''
#삼항연산자
#format : 명령문 if 참조건 else 거짓일때의 명령문
'''
age = input("나이를 입력하세요 : ")
print("party tonight" if int(age)>=20 else "study tonight")
'''
'''
while True:
	a = input()
	if a == '1' and int(a) == 1:
		print("The end")
		break
	else:
		print("This is not one")
		'''
'''
for i in range(2,10):
	for j in range(1,10):
		print(i*j,end=" ")
	print('')
	'''

list_a = [3,6,9,12]
res1 = []
for n in list_a:
	res1.append(n-1)
print(res1)

res2 = [n-2 for n in list_a]
print(res2)