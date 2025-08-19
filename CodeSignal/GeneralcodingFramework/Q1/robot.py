def robot(lr):
  if(lr==""):
    return ""
  leftCount=0
  rightCount=0
  for char in lr:
    if (char=="L"):
      leftCount+=1
    else:
      rightCount+=1
  if(leftCount>rightCount):
    return "L"
  elif(rightCount>leftCount):
    return "R"
  else:
    return ""

print(robot("LRLRLRLR"))
print(robot("LLLLRRR"))
print(robot("LLLRRRR"))
print(robot(""))
