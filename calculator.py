#! /usr/bin/env python3
import sys


#try:
#	taxincome = int(sys.argv[1]) - 3500
#except:
#	print("Parameter Error")

if len(sys.argv) != 7:
	print("Parameter Error")
configfilename = 


def taxprint(taxincome):
	if taxincome <= 0:
		return format(0,".2f")
	elif taxincome <= 1500:
		tax = taxincome * 0.03
		return tax
	elif taxincome > 1500 and taxincome <= 4500:
		tax = taxincome * 0.1 - 105
		return tax
	elif taxincome >4500 and taxincome <=9000:
        	tax = taxincome * 0.2 - 555
        	return tax
	elif taxincome > 9000 and taxincome <= 35000:
        	tax = taxincome * 0.25 - 1005
        	return tax
	elif taxincome > 35000 and taxincome <= 55000:
        	tax = taxincome * 0.3 * 2755
        	return tax
	elif taxincome > 55000 and taxincome <= 80000:
        	tax = taxincome * 0.35 - 5505
        	return tax
	elif taxincome > 80000:
        	tax = taxincome * 0.45 - 13505
        	return tax

for arg in sys.argv[1:]:
	taxlist = arg.split(':')
	try:
		salary =int(taxlist[1])
	except:
		print("Parameter Error")
	fund = salary * 0.08 + salary * 0.02 + salary * 0.005 + salary * 0.06
	#print("fund: ",fund)
	taxincome = salary - fund - 3500
	#print("taxincome: ",taxincome)
	if taxincome <= 0:
		reallysalary = format(salary - fund,".2f")
	else: 
		tax = taxprint(taxincome)
		#print("tax: ",tax)
		reallysalary = format(salary - fund - tax,".2f")
	print(taxlist[0],reallysalary,sep=':')
