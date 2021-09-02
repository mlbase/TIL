def findnumber(num1,  list1, num2, list2):
  answer = []
  n1 = int(num1/2)

  list1= list1.sort()
  list2= list2.sort()
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




