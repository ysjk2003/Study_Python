#function that no return value
def func1(a):
    print(a*3)

print ('start')
func1('asdf')

#function that return value
def sum(a,b):
    return a+b

a,b=input().split()
res=sum(int(a),int(b))
print(res)
#함수는 선언하고 호출하는 위치가 중요하다
#c언어처럼 앞에서 프로토타입을 선언할 수 없을까? 아마 안됨

def adf(a):
    user_input = ' '
    while a!="quit":
        user_input = input('input:')
        if a=="skip":
            print("rejected")
        else: print (a)
        print("----------")

a = input()

#skip을 포함하는 문자열인 경우 rejected를 출력하고
#구분선을 출력하지 않는 함수
def print_without_skip(string):
    if 'skip' in string:
        print('rejected')
        return
    else:
        print(string)
    print('-'*10)

user_input = ' '
while user_input != 'quit':
    user_input = input('input:')
    print_without_skip(user_input)