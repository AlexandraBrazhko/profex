#1

fin=open('students.csv', 'r', encoding='utf-8')
title=fin.readline()
students=[x.strip().split(',') for x in fin]
fin.close()
bal_sum={}
bal_cnt={}
for x in students:
    if x[4]!='None':
        if x[3] in bal_sum:
            bal_sum[x[3]]+=int(x[4])
            bal_cnt[x[3]]+=1
        else:
            bal_sum[x[3]]=int(x[4])
            bal_cnt[x[3]]=1

for x in students:
    if 'Хадаров Владимир' in x[1]:
        print(f'Ты получил: {x[4]}, за проект - {x[2]}')
fout=open('students_new.csv', 'w', encoding='utf-8')
fout.write(title)
for x in students:
    s=','.join(x)
    fout.write(s)
fout.close()




