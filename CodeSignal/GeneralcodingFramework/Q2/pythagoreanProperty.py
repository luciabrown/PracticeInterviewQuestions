# Array triplets with Pythahorean Property
import math

def pythag(n):
  solutionArray=[]
  for i in range(0,len(n)-2):
    if((math.pow(n[i],2)+math.pow(n[i+1],2)==math.pow(n[i+2],2)) or (math.pow(n[i+1],2)+math.pow(n[i+2],2)==math.pow(n[i],2))or (math.pow(n[i],2)+math.pow(n[i+2],2)==math.pow(n[i+1],2))):
      solutionArray.append(1)
    else:
      solutionArray.append(0)
  return solutionArray

ans=pythag([3, 4, 5, 6, 8, 10, 7, 24, 25, 1, 2, 3])
print(ans)
