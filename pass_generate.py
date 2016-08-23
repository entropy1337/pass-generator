import itertools
import sys



if len(sys.argv) == 4:
	user_list1 = sys.argv[1]
	user_list2 = sys.argv[2]
	user_list3 = sys.argv[3]
else:
		
	print '\nUsage: %s custom.lst dictionary.lst symbols.lst\n'%sys.argv[0]
	sys.exit(1) 

comboList = ['']

list1 = open(user_list1,'r').read().split()
list2 = open(user_list2,'r').read().split()
list3 = open(user_list3,'r').read().split()

comboList.append(map(''.join, itertools.chain(itertools.product(list1, list2, list3), itertools.product(list3,list2, list1))))
comboList.append(map(''.join, itertools.chain(itertools.product(list1, list2, list3), itertools.product(list3,list1, list2))))
comboList.append(map(''.join, itertools.chain(itertools.product(list1, list2, list3), itertools.product(list2,list3, list1))))
comboList.append(map(''.join, itertools.chain(itertools.product(list1, list2, list3), itertools.product(list1,list2, list3))))
comboList.append(map(''.join, itertools.chain(itertools.product(list1, list2, list3), itertools.product(list1,list3, list2))))
comboList.append(map(''.join, itertools.chain(itertools.product(list1, list2), itertools.product(list1,list2))))
comboList.append(map(''.join, itertools.chain(itertools.product(list1, list2), itertools.product(list1,list1))))
comboList.append(map(''.join, itertools.chain(itertools.product(list2, list3), itertools.product(list2,list3))))
comboList.append(map(''.join, itertools.chain(itertools.product(list3, list2), itertools.product(list3,list2))))
comboList.append(list1)
comboList.append(list2)


created_dictionary = open('generated_dictionary.txt','ab+')

lDictionary = []

for i in comboList:
	for word in i:
		lDictionary.append(word)
		


for i in sorted(set(lDictionary)):
	created_dictionary.write(i+'\n')
	
	
created_dictionary.close()
