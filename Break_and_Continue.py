# Use of break statement inside For loop
for val in "string":
    if val == "i":
        break
    print(val)

print("The end")

#Use of continue statement inside For loop

for val in "string":
    if val == "i":
        continue
    print(val)

print("The end")

# Use of break statement inside While loop

my_list = ['Siya', 'Tiya', 'Guru', 'Daksh', 'Riya', 'Guru'] 
i = 0

while True:
    print(my_list[i])
    if (my_list[i] == 'Guru'):
        print('Found the name Guru')
        break
        print('After break statement')
    i += 1

print('After while-loop exit')

#Use of continue statement inside While loop

i = 0
while i <= 10:    
    if i == 7:
        i += 1
        continue  
    print("The Number is  :" , i)
    i += 1

