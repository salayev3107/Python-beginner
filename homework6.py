#1
with open('text.txt') as file:
    f = file.read()

print(f)

#3
with open('pi_million_digits.txt','r') as fayl:
    r = fayl.read()
    #print(r.find('31072004')) # yoq ekan 


#4
import pickle
t1 =(r) 
t1 =float(t1[:15])
with open('info1','wb') as file1:
    pickle.dump(t1,file1)
#5

with open('newf.txt','a+') as file3:
    file2 = input('write your Name, surname and your birth date:')
    file3.write('\n' + file2)
