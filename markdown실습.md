# 헤딩(#) 

## 제목을 입력할때 사용

- '-' 순서없는 리스트
  1. 순서 있는리스트
  2. 자동으로 번호 할당

---



# 소스코드

## '''을 입력해서 사용

### tag로 붙일수도 있음

- 이렇게 `import numpy` (\` 로 입력)

``` python
def findnumber(num1,  list1, num2, list2):
  answer = []
  n1 = int(num1/2)

  pivot = list1[n1]

  for i in range(num2):
    if list2[i]>pivot:
      if list2[i] in list1[n1:len(list1)-1]:
        answer.append(1)
      else:
        answer.append(0)
    else:
      if list2[i] in list1[0:n1]:
        answer.append(1)
      else:
        answer.append(0)
  
  return printeach(answer)

def printeach(list1):
  for i in list1:
    print(i)

num1 = 0
num2 = 0
list1 = []
list2 = []
num1 = 5
list1 = [4, 1, 5, 2, 3]
num2 = 5
list2 = [1, 3, 7, 9, 5]

findnumber(num1, list1, num2, list2)
```

[나의 깃허브](https://github.com/mlbase/)

* \[]\(url) 하면 링크 첨부가능
* \!\[]\(url)하면 이미지파일 업로드가능

![암거나](C:/Users/admin/Pictures/2%EC%A3%BC%EC%B0%A8%20%EA%B3%BC%EC%A0%9C_2.png)

---



# text

## bolding, *talic* ~~strikeout~~

### 그냥 연습

* \*\*text\** 이면 굵게 **이렇게**
* \*text\* 이면 *이렇게*
* \~\~text\~\~ 이면 ~~이렇게~~

