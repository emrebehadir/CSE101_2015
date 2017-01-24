 
import random

global 	QUEUE, STACK, SORTEDLIST

QUEUE = [] 
STACK = []
SORTEDLIST = []

# QUEUE Data Structure Functions 
def enqueue(item):  #Queuede sol taraf bas sag taraf kuyruktur. 
	global 	QUEUE
	QUEUE = QUEUE +[item]
	
def dequeue():
	global 	QUEUE
	dequeue_number = QUEUE[0]
	QUEUE[0:1] = []
	return dequeue_number
	
# STACK Data Structure Functions 
def push(item):
	global 	STACK 
	STACK  = STACK  +[item]
	
def pop():
	global 	STACK 
	pop_number= STACK[-1]
	STACK  = STACK[0:len(STACK)-1]
	return pop_number
	
# SORTED LIST Data Structure Functions 
def insert(item):
	global SORTEDLIST
	
	if (len(SORTEDLIST) == 0):
		SORTEDLIST= SORTEDLIST + [item]
	
	else:
		i=0
		test_entry=SORTEDLIST[i]
		
		while(item >test_entry and i<(len(SORTEDLIST)-1) ):
			i=i+1
			test_entry=SORTEDLIST[i]
			
		if(item < test_entry):
			SORTEDLIST= SORTEDLIST[0:i] + [item] +SORTEDLIST[i:len(SORTEDLIST)]
		else:
			SORTEDLIST= SORTEDLIST + [item]

def remove(item):# Silebilmek icin buldugum itemin indexsini buldum ve o index si sildim
	global SORTEDLIST
	
	if (len(SORTEDLIST) > 0):

		i=0
		test_entry=SORTEDLIST[i]
		
		while(item>test_entry and i<len(SORTEDLIST) ):
			i=i+1
			test_entry=SORTEDLIST[i]
			
		if(item == test_entry):
			remove_item=i
	
	SORTEDLIST = SORTEDLIST[:remove_item] + SORTEDLIST[remove_item+1:]	

def search(SORTEDLIST,item):# Search de hangi item oldugunu buldum.
	
	if (len(SORTEDLIST) == 0):
		return None
	else:	
		test_entry=SORTEDLIST[(len(SORTEDLIST)/2)]
		
		if (item  == test_entry):
			return SORTEDLIST

		if (item < test_entry):
			sublist =SORTEDLIST[:len(SORTEDLIST)/2]
			search(sublist,item)
		if (item > test_entry):
			sublist=SORTEDLIST[len(SORTEDLIST)/2+1:]
			search(sublist,item)	

def main():
	
	numberList = random.sample(xrange(0,1000),10)

	for number in numberList:
		enqueue(number)
		push(number)
		insert(number)

	print '\n'
	print QUEUE
	print "Dequeue number>>", dequeue()
	print "Dequeue number>>", dequeue()
	print QUEUE
	print '\n'
	print STACK
	print "Pop number>>", pop()
	print "Pop number>>", pop()
	print STACK
	print '\n'
	print SORTEDLIST
	number = random.randint(0,1000)
	while(not search(SORTEDLIST, number)):
		number = random.randint(0,1000)
		
	remove(number)
	print SORTEDLIST
	print '\n'

main()



