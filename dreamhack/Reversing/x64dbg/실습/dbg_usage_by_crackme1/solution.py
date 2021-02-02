# $ python solve.py 
# answer: 5678 1234
for x in range(0x2000 + 1):
    for y in range(0x2000 + 1):
        if x * y != 0x6ae9bc:
            continue
        
        if x // y != 4:
            continue
        
        if x ^ y != 0x12fc:
            continue
        
        print('answer:', x, y)


# PS C:\> .\easy-crackme1.exe
# input: 5678 1234
# correct!


# better solution
# $ python solve.py 
# answer: 5678 1234
for x in range(0x2000 + 1):
    y = x ^ 0x12fc
    if x * y != 0x6ae9bc:
        continue
    
    if x // y != 4:
        continue
        
    print('answer:', x, y)

#  문제는 풀었지만, solve.py를 실행하보면 답이 나오는데 시간이 좀 걸린다는 것을 알 수 있습니다. 모든 경우의 수를 하나씩 체크하는 방식으로 답을 찾았기 때문에 느린 것인데, 어떤 문제의 경우는 이러한 방식으로 답을 찾을 경우 굉장히 오랜 시간이 걸리는 경우도 있습니다. 이 문제 역시 0x2000보다 작거나 같다란 조건이 없으면 굉장히 시간이 오래 걸렸을 것입니다.
# 이번에는 solve.py를 조금 더 개선시켜서 매우 빠른 시간 안에 답이 나오도록 바꿔보도록 하겠습니다.
# 두 인자의 조건중 다음과 같은 조건이 있었습니다.
# 첫 번째 인자 ^ 두 번째 인자 가 0x12fc여야 한다.
# xor은 특이한 성질을 가지고 있는데 수식으로 정리하면 다음과 같습니다. (A와 B와 C는 임의의 정수입니다)
# A ^ B ^ B == A
# A ^ A == 0
# A ^ B == C 일 때, C ^ A == B이고 C ^ B == A이다.
# 문제에서는 첫 번째 인자 ^ 두 번째 인자 == 0x12fc이니, 두 번째 인자 == 첫 번째 인자 ^ 0x12fc라는걸 알 수 있습니다. 이를 이용해 다시 solve.py를 작성한 것이 오른쪽의 코드입니다. 직접 돌려보면 처음의 solve.py보다 훨씬 빠른 속도로 답이 나오는 걸 확인할 수 있습니다.

