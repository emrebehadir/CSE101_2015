
#Liste uzun oldugunda binary search daha kisa surede diger durumda ise iki arama yaklasik ayni surede gerceklesiyor.
 
#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random
import timeit

def createRandomNumberFile(min, max, count, output_FileName):
	
	outputFile = open(output_FileName, "a+")
	for item in range(0, count):
		randomNumber = random.randint(min,max)
		outputFile.write(str(randomNumber)+"\n")
	
	list = outputFile.read().splitlines() #outputFile i okuyarak listeye string seklinde aktarir.
	for i in range(0,len(list)):   		  #Siralama yapabilmemiz icin stiring diziyi integer diziye cevirir.
		list[i]= int(list[i])
	
	insertion_sort(list)				  
	
	start = timeit.default_timer()
	binary_search(list,61)
	stop = timeit.default_timer()		
	print "binary search time >>",( stop - start ) *1000
	print "--------------------"
	start1 = timeit.default_timer()
	linear_search(list,61)	
	stop1 = timeit.default_timer()
	print "linear search time >>",( stop1 - start1 ) *1000


def insertion_sort(list):

	n=1
	while (n<len(list)):
		i=n
		temp=list[n]
		
		while (i>0 and list[i-1]>temp):
			list[i]=list[i-1]
			i=i-1
			
		list[i]=temp
		n=n+1
		

def linear_search(list,target_value):
	
	if (len(list) == 0):
		print "Linear search a failure."
	
	else:
		i=0
		test_entry=list[i]
		
		while(target_value>test_entry and i<len(list) ):
			i=i+1
			test_entry=list[i]
			
		if(target_value == test_entry):
			print "Linear search a success."
		else:
			print "Linear search a failure."
	
def binary_search(list,target_value):
	
	if (len(list) == 0):
		print "Binary search  failed."	
	else:	
		test_entry=list[(len(list)/2)]
		
		if (target_value  == test_entry):
			print "Binary search succeded."
		if (target_value < test_entry):
			sublist =list[:len(list)/2]
			binary_search(sublist,target_value)
		if (target_value > test_entry):
			sublist=list[len(list)/2:]
			binary_search(sublist,target_value)
	
	
createRandomNumberFile(1, 250, 50, "Output_File")

