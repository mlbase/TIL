# 올림
def ceil(number):
    if int (number) != number:
        number +=1
    
    return number


# 스플릿해서 새 리스트 선언
def split_list(li, chr):
    answer = []
    for i in range(len(li)):
        answer[i] = li.split(chr)
    return answer

# 중복제거
def eliminateoverlap(li):
    nullist = []
    for i in li:
        if i not in nullist:
            nullist.append(i)
    li = nullist
    return li

# n진법 만들기
def k_decimal(number, k):
    decistr = ""
    
    while(number/k != 0)

# 소수구하기



if __name__ =='__main__':