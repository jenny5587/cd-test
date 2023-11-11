def solution(s):
    answer = s
    # 문자열을 숫자로 바꾸기
    dic = {'zero':0, 'one': 1, 'two': 2, 'three': 3,
           'four': 4, 'five': 5, 'six': 6,
           'seven': 7, 'eight': 8, 'nine': 9}
    for i in dic.items():
        # replace() argument 2 must be str, not int
        answer = answer.replace(i[0], str(i[1]))
    return int(answer)
