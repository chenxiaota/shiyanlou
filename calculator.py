#! /usr/bin/env python3
import sys
import os.path

#try:
#	taxincome = int(sys.argv[1]) - 3500
#except:
#	print("Parameter Error")

#judge
if len(sys.argv) != 7:
	print("Parameter Error")
else:
	if sys.argv[1] == '-c':
		config_file = sys.argv[2]
	else:
		print("-c Error")
		exit()
	if sys.argv[3] == '-d':
		data_file = sys.argv[4]
	else:
		print("-d Error")
		exit()
	if sys.argv[5] == '-o':
		op_file = sys.argv[6]
	else:
		print("-o Error")
		exit()
	
	if not os.path.exists(config_file):
		print("config file is not exists")
		exit()
	if not os.path.exists(data_file):
		print("data file is not exists")
		exit()
	print("config: ",config_file)
	print("data: ",data_file)
	print("op: ",op_file)

	with open(config_file) as file:
		JiShuL = (file.readline().split('='))[1].strip()
		JiShuH = (file.readline().split('='))[1].strip()
		YangLao = (file.readline().split('='))[1].strip()
		YiLiao = (file.readline().split('='))[1].strip()
		ShiYe = (file.readline().split('='))[1].strip()
		GongShang = (file.readline().split('='))[1].strip()
		ShengYu = (file.readline().split('='))[1].strip()
		GongJiJin = (file.readline().split('='))[1].strip()
		print("JiShuL: ",JiShuL)
		print("JiShuH: ",JiShuH)
		print("YangLao: ",YangLao)
		print("YiLiao: ",YiLiao)
		print("ShiYe: ",ShiYe)
		print("GongShang: ",GongShang)
		print("ShengYu: ",ShengYu)
		print("GongJiJin: ",GongJiJin)
'''
	count = 1
	print(sys.argv)
	
	for i in sys.argv[1:]:
		if i == "-c":
			configfile_name = sys.argv[count+1]
		elif i == "-d":
			datafile_name = sys.argv[count+1]
		elif i == "-o":
			opfile_name = sys.argv[count+1]
		else:
			print("Parameter Error")
			break
	
	judge(sys.argv[1],sys.argv[2])
	judge(sys.argv[3],sys.argv[4])
	judge(sys.argv[5],sys.argv[6])
		

	print("configfile: " , configfile_name)
	print("datafile: ",datafile_name)
	print("opfile: ",opfile_name)

def judge(command,adress):
	if command == '-c':
		global configfile_name = address
	elif command == '-d':
		global datafile_name = address
	elif command == '-o':
		global opfile_name = address
	else:
		print("Parameter Error")


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
'''
