print("Testing for loop with range:")
for i in range(5):
    print("Loop number:", i)

print("\nTesting for loop with a list:")
skills = ["Python", "JavaScript", "Git"]
for skill in skills:
    print("Skill name:", skill)



print("\nTesting while loop:")
count = 1
while count <= 3:
    print("Count is:", count)
    count += 1  



print("\nTesting loop control:")
for num in range(1, 6):
    if num == 2:
        print("Skipping 2")
        continue  
        
    if num == 4:
        print("Found 4, stopping loop completely")
        break
        
    print("Number:", num)
