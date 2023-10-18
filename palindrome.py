def pd(aString): ##palindrome
  if len(aString) ==1 or len(aString)==0:
    return f"It is palindrome"
  elif aString[0] == aString[-1]:
    return pd(aString[1:-1])
  else:
    return f"It is not palindrome"

print(pd("madam"))
print(pd("mom"))
print(pd("moom"))
print(pd("moas"))



temperatures = [73,74,75,71,69,72,76,73]
answer = []
for i in range(len(temperatures)):
  count = 0
  if i == len(temperatures)-1:
    answer.append(0)
  for j in range(i+1,len(temperatures)):
    if temperatures[i] < temperatures[j]:
      count+=1
      answer.append(count)
      break
    else:
      count+=1
print(answer)






