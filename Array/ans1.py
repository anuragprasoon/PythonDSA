expense=[2200,2350,2600,2130,2190]
//1
print('spend extra: ',expense[1]-expense[0])
//2
print('total spend of 1st quater: ',expense[0]+expense[1]+expense[2])
//3
for i in expense:
    if i==2000:
        print('spend 2000')
//4
expense.append(1980)
print(expense)
//5
expense[3]=expense[3]-200
print('expense of april after refund: ',expense[3])
