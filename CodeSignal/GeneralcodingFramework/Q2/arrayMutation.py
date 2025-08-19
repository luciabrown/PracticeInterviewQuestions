# Q2 ARRAY MUTATION
# n is an interger
# a is an array of length n
# mutate a into b where b[i] = a[i-1] + a[i] + a[i+1]
def mutate(a):
  solutionArray=[]
  for i in range(0,len(a)):
    if i==0:
      solutionArray.append(a[i]+a[i+1])
    elif i==len(a)-1:
      solutionArray.append(a[i-1]+a[i])
    else:
      solutionArray.append(a[i-1]+a[i]+a[i+1])
  return solutionArray

ans = mutate([1,2,3,4,5,6,7,8,9,10])
ans2 = mutate([200,100,-3,67,943])
print(ans)
print(ans2)
