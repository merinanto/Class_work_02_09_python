num = int(input("How many numbers"))
i =0
while  i <= num:
    print(i)
    user_input =input("Whether to continue y or n")   
    if user_input== 'y': 
     i +=1
    elif  user_input== 'n' :
      break
    else :
        print("Invalid Input")
        break
    
    
