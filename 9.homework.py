
stud_marks = [12,23,20,11,20,30,21,22,30,14,17,19,25,24,28]
odd = []
even = []
for i in stud_marks:
    if i % 2 == 0:
        odd.append(i)

    else : 
         even.append(i)
print(f'odd marks = {odd}')
print(f'even marks = {even}')

'''------------------------------
OUTPUT : 
odd = [12, 20, 20, 30, 22, 30, 14, 24, 28]
even = [23, 11, 21, 17, 19, 25]
----------------------------------'''