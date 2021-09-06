


def BinarySearch( n, A, m, B):
    
    answer = []
    A.sort()
    k=sorted(A)
    pivot = len(k) //2

    for i in range(len(B)):
        if B[i] > k[pivot]:
            if B[i] in k[pivot:-1]:
               answer.append(1)
            else:
                answer.append(0)
                
        elif B[i] <=k[pivot]:
            if B[i] in k[0:pivot]:
                answer.append(1)
            else:
                answer.append(0)
    for i in answer:
        print(answer[i])
    
BinarySearch(5, [4,1,5,2,3], 5, [1,3,7,9,5])        
    
