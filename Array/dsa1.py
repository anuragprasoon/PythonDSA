expense=[2200,2350,2600,2130,2190]
print('spend extra: ',expense[1]-expense[0])
print('total spend of 1st quater: ',expense[0]+expense[1]+expense[2])
for i in expense:
    if i==2000:
        print('spend 2000')
expense.append(1980)
print(expense)
expense[3]=expense[3]-200

