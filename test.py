#!/usr/bin/env python3

import sys
import os.path

class Config(object):
	def __init__(self,configfile):
		self._config = {}
		with open(configfile) as file:
			configList = file.readlines()
			for c in configList:
				self._config[c.split('=')[0].strip()] = c.split('=')[1].strip().replace('\n','')
	def get_config(self,key):
		return self._config[key]
	def check_print(self):
		print(self._config)

class UserData(object):
    def __init__(self, userdatafile,cfg={}):
    	self.userdatafile = userdatafile
    	self.cfg = cfg
    	with open(self.userdatafile) as file:
    		userList = file.readlines()
    		for user in userList:
    			self.cfg[user.split(',')[0]] = user.split(',')[1].replace('\n','')
    def __getitem__(self, key):
        return self.cfg[key]

args = sys.argv[1:]
indexc = args.index('-c')
config_file = args[indexc+1]
indexd = args.index('-d')
user_file = args[indexd+1]
indexo = args.index('-o')
op_file = args[indexo+1]

if not os.path.exists(config_file):
	print("config file error")
	exit()
if not os.path.exists(user_file):
	print("user file errot")
	exit()

user = UserData(user_file)
config = Config(config_file)

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
		tax = taxincome * 0.45 - 13500
		return tax

for key,value in user.cfg:
	taxlist = arg.split(',')[1].replace('\n','')
	try:
		salary =int(taxlist)
	except:
		print("Parameter Error in user")
	if salary >= float(config.get_config('JiShuL')) and salary <= float(config.get_config('JiShuH')):
		fund = salary * float(config.get_config('YangLao')) + salary * YiLiao + salary * ShiYe + salary * GongShang + salary * ShengYu + salary * GongJiJin
	else:
		if salary < JiShuL:
			fund = JiShuL * YangLao + JiShuL * YiLiao + JiShuL * ShiYe + JiShuL * GongShang + JiShuL * ShengYu + JiShuL * GongJiJin
		if salary > JiShuH:
			fund = JiShuH * YangLao + JiShuH * YiLiao + JiShuH * ShiYe + JiShuH * GongShang + JiShuH * ShengYu + JiShuH * GongJiJin
	print("fund: ",fund)
	taxincome = salary - fund - 3500
	print("taxincome: ",taxincome)
	if taxincome <= 0:
		tax = 0
		reallysalary = format(salary - fund,".2f")
	else:
		tax = taxprint(taxincome)
		print("tax: ",tax)
		reallysalary = format(salary - fund - tax,".2f")
	print(taxlist[0],reallysalary,sep=':')



