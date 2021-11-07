def solution(participant, completion):
    
    a= dict()

    for val in participant:
        if val in a.keys():
            a[val]+= 1
        else:
            a[val] = 1
        
    for val in completion:
        if a[val] == 1:
            a.pop(val)
        else:
            a[val] -=1
    
    str =""
    
    for val in a.keys():
        Str = val

    return str



    

if __name__=='__main__':
    a=["leo","kiki","eden"]
    b=["eden","kiki"]
    print((solution(a,b)))