import sys
import random
import ipdb
breakP = ipdb.set_trace

def main():
	outputP = []
	#for i in range(0,5):
	S = [1,2,3,4,5,6,7,8,9,10]
	ans = randomP(S)
	#for i in range(0,5):
	print ans
	cycleNotation(ans)	

	
def randomP(numbers):
	temp_num = numbers
	Perm = []
	for i in range(0,len(numbers)):
		Perm.append(random.choice(temp_num))
		temp_num.remove(Perm[i])
	return Perm

def cycleNotation(perm):
	cycle_not = []
	cycle = []
	notfirst_cycle = []
	notfirst = True
	count = 1
	cy_len = []
	A = []
	cycle_not.append(perm[0])
	print perm
	for i in range(1,len(perm)):
		# IF THE MOST RECENT ELEMENT AND ITS NEXT MEMBER ARE SEPERATED BY 1 
		# CONTINUE BUILDING CYCLE
		if(abs(perm[i-1]-perm[i])==1) | (abs(perm[i-count]-perm[i])==1):
			print "FOUND A SEQUENCE: ", perm[i-1], perm[i]
			# ADD THE OLD COMPONENTS OF THE CYCLE
			A = cycle_not.pop()
			cycle.append(A)
			cycle.append(perm[i])
			count = len(cycle)-1
		
		# IF THEY ARENT AND A CYCLE HASNT COMPLETED YET
		elif (abs(perm[i-1]-perm[i])!=1) & (notfirst):
			# ADD NEWLY COMPARED ELEMENT TO REST OF SET
			# FOUND SINGLE SET
			cycle_not.append(perm[i])
			
		# IF THEY ARENT AND A CYCLE HAS COMPLETED ALREADY
		elif (abs(perm[i-1]-perm[i])!=1) & (not notfirst):
			# CHECK IF CURRENT SINGLE CAN BE RECONNECTED AT OTHER END OF CYCLE
			if abs(perm[i] - cycle[0]) == 1: 
				cycle.append(perm[i])
				cycle_not.pop()
				cycle_not.append(cycle)
				cycle = []
			# ELSE IT IS A SINGLE THAT NEEDS ITS OWN CYCLE
			else:
				cycle_not.append(perm[i])
				cycle = []
		# ELSE ATTACH THE CYCLE THAT WAS FOUND IF IT EXISTS
		if (len(cycle) != 0):
			cycle_not.append(cycle)
			cycle = []		
		#if(len(cycle) == 0) & (not notfirst):
		#	if abs(perm[i-1] - perm[i]) == 1:
		#		old_cycle = cycle_not.pop()
		#		new_cycle = old_cycle.append(cycle)
		#		cycle_not.append(new_cycle)
		#		print "ADD SINGLE TO END OF LAST CYCLE"
		#elif(len(cycle) == 0) & (notfirst):
                #      	print "FOUND TWO FIRST SINGLES: "
		#	cycle_not.append(perm[i-1])
		#	cycle_not.append(perm[i])
		
		#if(len(cycle) != 0) & (abs(perm[i-1]-perm[i])!=1) & notfirst:
		#	cycle_not.append(cycle)
		#	cy_len.append(count)
		#	notfirst = False
		#	cycle = []
		
		#elif(len(cycle) != 0) & (abs(perm[i-1]-perm[i])!=1):
		#	print "THESE ARE THE CYCLE LENGTHS: ", cy_len
		#	cy_num = len(cy_len)-1
		#	print "ACCESS INDEX: ", i-count-cy_len[cy_num]
		#	if(abs(perm[i]-perm[i-count-cy_len[cy_num]]) == 1):
		#		old_cycle = cycle_not.pop()
		#		new_cycle = old_cycle.append(cycle)
		#		cycle_not.append(new_cycle)
		#		print "NEED TO CONCAT OLD CYCLE WITH NEW: ", old_cycle, cycle, new_cycle
		#		old_cycle = []
		#		new_cycle = []
		#		cycle = []
		#	else:
		#		old_cycle = cycle_not[len(cycle_not)-1]
		#		print "OLD AND NEW CYCLES ARE SEPERATE: ", old_cycle, cycle
		#		cycle_not.append(cycle)
		#		old_cycle = []
		#		cycle = []

		print "STEP: ", i, cycle_not
		#if(len(cycle) != 0):
			#if (abs(perm[i-1]-perm[i])==1) & (abs(notfirst_num-perm[i])!=1):
                        #	cycle_not.append(cycle)
			#	cycle_not.append(perm[i])
			#elif(abs(perm[i-1]-perm[i])!=1 ) & (abs(notfirst_num-perm[i])==1):
			#	cycle.append(perm[i])
                        #        cycle_not.append(cycle)
			#elif(abs(perm[i-count]-perm[i])==1) & (abs(perm[i-1]-perm[i])==1):
			#	cycle.append(perm[i])
			#	cycle_not.append(cycle)	
			#else:
			#	cycle_not.append(cycle)
                        #        cycle_not.append(perm[i])	
			#print "FULL CYCLE ", notfirst
			#cycle = []
			#notfirst = 1
			#notfirst_num = 100 
			#count = 1
		#else:
		#	print "SINGLE CYCLE"
		#	cycle_not.append(perm[i])	
	#if(len(cycle) != 0):
	#	cycle.append(perm[i+1])
	#	cycle_not.append(cycle)
	#else:
	#	cycle_not.append(perm[i+1])
	#print cycle_not

if __name__ == '__main__':
    sys.exit(main())

