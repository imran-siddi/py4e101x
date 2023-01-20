score = input("Enter Score between 0.0 and 1.0: ")
try :
    x = float(score)
except :
    print ('Entered Score is not a number')
    quit()
if x >= 0.9 and x <= 1.0 :
    x = 'A'
elif x >= 0.8 and x <= 0.9 :
    x = 'B'
elif x >= 0.7 and x <= 0.8 :
    x = 'C'
elif x >= 0.6 and x <= 0.7 :
    x = 'D'
elif x < 0.6 and x >= 0.0 :
    x = 'F'
else :
    print ('Entered Score is not in range')
    quit()    
print (x)