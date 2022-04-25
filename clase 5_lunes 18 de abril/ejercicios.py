brackets = "[[[[]]][][][]"
check = 0


for bracket in brackets:
    if bracket == "[":
        check += 1
    
    elif bracket == "]":
        check -= 1
    
    if check <0:
        check== 0
print(check== 0)
        
#False