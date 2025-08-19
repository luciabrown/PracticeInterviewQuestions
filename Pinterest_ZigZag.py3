# Pinterest Practice Question from CodeSignal

def solution(numbers):
    if all_equal(numbers):
        return [0]
    
    outputList=[]
    for i in range(1,len(numbers)-1):
        if((numbers[i-1]<numbers[i]and numbers[i]>numbers[i+1]) or(numbers[i-1]>numbers[i]and numbers[i]<numbers[i+1])):
            outputList.append(1)
        else:
            outputList.append(0)
    
    return outputList
        
def all_equal(numbers):
    return len(set(numbers))==1
