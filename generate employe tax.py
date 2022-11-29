#employe tax
empo=int(input('enter employe phno:'))
emname=(input('enter employe name:'))
a=int(input('enter basic salary:'))
b=int(input('enter daily allowance'))
c=int(input('enter travelling allowance:'))
d=int(input('enter house rental allowance:'))
netsalary=a+b+c+d
if netsalary>100000:
            tax=netsalary*10/100
            print('tax:',tax)            
elif netsalary>50000:
            tax=netsalary*7/100
            print('tax:',tax)
elif netsalary>40000:
            tax=netsalary*4/100
            print('tax:',tax)
elif netsalary>20000:
            tax=netsalary*2/100
            print('tax:',tax)
            
if netsalary<20000:
        print('tax=0')
            
            
         
            
         
            
            
         
