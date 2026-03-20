def solve1(numbers):
    # Q: 3의 배수이면서 홀수인 수의 합을 구하여 반환
    answer = 0
    
    # 여기에 코드를 하십시오.
    for i in numbers:
        if i%3==0 and not i%2==0:
            answer+=i
            
    return answer
