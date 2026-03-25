def solve2(format_str):
    # Q: Readme 파일의 두 번째 문제
    answer = 0
    
    # 여기에 코드를 작성하십시오.
    a=format_str[0]
    if a=='N':
        answer=10
    elif a=='C':
        answer=26
    
    b={'N':10,'C':26}
    for i in range(1,len(format_str)):
        c=b.get(format_str[i])
        if format_str[i-1]==format_str[i]:
            answer=answer*(c-1)
        elif format_str[i-1]!=format_str[i]:
            answer=answer*c
    return answer
