# Question 4

# old code
#result = 0
#counter = 1

#while counter <= 50:
    #if counter % 9 == 0:
        #result -= counter
        #counter += 2
        #continue
    #result += counter
    #print(f"Adding {counter} to the result: {result}")
    #counter -= 1
    #if counter % 17 == 0:
        #continue

#print("\nThe final generated number is:", int(result/10))

#new code

#result = 0
#counter = 1

#while counter <= 50:
    #if counter % 9 == 0:
        #result -= counter
        #counter += 2
        #continue
    #result += counter
    #print(f"Adding {counter} to the result: {result}") 
    #counter -= 1 
    #if counter % 17 == 0:
        #continue

#print("\nThe final generated number is:", result) 

# Do not run as the code is still broken and goes into loop

result = 0
counter = 1

while counter <= 50:
    if counter % 9 == 0:
        result -= counter
        counter += 2
        continue
    result += counter
    print(f"Adding {counter} to the result: {result}") 
    counter += 1  
    if counter % 17 == 0:
        break  # Terminate the loop if counter is divisible by 17

print("\nThe final generated number is:", result/10)