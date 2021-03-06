read = ''
unread = input()
tmp = 0
line = 0

def spaceToDecimal(number):
	rev = number[::-1]
	base = 0
	dec = 0
	for d in rev:
		dec = dec + (int(d) - 1) * (2 ** base)
		base = base + 1
	return str(dec)

while unread != '':
	line = line + 1
	
	#For Stack Manipulation Operations:
	if (unread[0] == '1'):
		#print(unread[0], ": IMP: STACK_MANIPULATION")
		read = read + unread[0]
		unread = unread[1:]
		
		if unread[0] == '1':
			#print(unread[0], ": OPERATION : PUSH")
			print("t" + str(tmp) + " = top + 1")
			print("top = t" + str(tmp))
			tmp = tmp + 1
			read = read + unread[0]
			unread = unread[1:]
			end = unread.find('3')
			number = unread[0:end]
			print("stack[top] = " + spaceToDecimal(number))
			read = unread[0:(end+1)]
			unread = unread[(end+1):]
		
		else:
			if unread[0:2] == '31':
				#print(unread[0:2], ": OPERATION: DUPLICATE")
				print("t" + str(tmp) + " = top + 1")
				print("top = t" + str(tmp))
				tmp = tmp + 1
				print("t" + str(tmp) + " = stack[top-1]")
				print("stack[top] = t" + str(tmp))
				tmp = tmp + 1
			
			elif unread[0:2] == '32':
				#print(unread[0:2], ": OPERATION: SWAP")
				print("t" + str(tmp) + " = stack[top]")
				tmp = tmp + 1
				print("t" + str(tmp) + " = stack[top-1]")
				print("stack[top] = t" + str(tmp))
				print("stack[top-1] = t" + str(tmp-1))
				tmp = tmp + 1
			
			elif unread[0:2] == '33':
				#print(unread[0:2], ": OPERATION: DISCARD")
				print("t" + str(tmp) + " = top - 1")
				print("top = t" + str(tmp))
				tmp = tmp + 1
			
			else:
				print("Syntax Error in line number", line)
			
			read = read + unread[0:2]
			unread = unread[2:]
		continue
	
	#For Arithmetic Operations:
	elif unread[0:2] == '21':
		op = ""
		#print(unread[0:2], ": IMP: ARITHMETIC")
		read = read + unread[0:2]
		unread = unread[2:]
		
		if unread[0:2] == '11':
			#print(unread[0:2], ": OPERATION: ADD")
			op = "+"
		
		elif unread[0:2] == '12':
			#print(unread[0:2], ": OPERATION: SUBTRACT")
			op = "-"
		
		elif unread[0:2] == '13':
			#print(unread[0:2], ": OPERATION: MULTIPLY")
			op = "*"
		
		elif unread[0:2] == '21':
			#print(unread[0:2], ": OPERATION: DIVIDE")
			op = "/"
		
		elif unread[0:2] == '22':
			#print(unread[0:2], ": OPERATION: MODULO")
			op = "%"
		
		else:
			print("Syntax Error in line number", line)
		
		print("t" + str(tmp) + " = stack[top-1]")
		tmp = tmp + 1
		print("t" + str(tmp) + " = stack[top]")
		tmp = tmp + 1
		print("t" + str(tmp) + " = t" + str(tmp-2) + " " + op + " t" + str(tmp-1))
		tmp = tmp + 1
		print("t" + str(tmp) + " = top - 1")
		print("top = t" + str(tmp))
		print("stack[top] = t" + str(tmp-1))
		tmp = tmp + 1
		read = read + unread[0:2]
		unread = unread[2:]
		continue
	
	#For Heap Access:
	elif unread[0:2] == '22':
		#print(unread[0:2], ": IMP: HEAP_ACCESS")
		read = read + unread[0:2]
		unread = unread[2:]
		
		if unread[0] == '1':
			#print(unread[0], ": OPERATION: STORE")
			print("heap.store(stack[top], stack[top-1])")
			print("t" + str(tmp) + " = top - 2")
			print("top = t" + str(tmp))
			tmp = tmp + 1
		
		elif unread[0] == '2':
			#print(unread[0], ": OPERATION: RETRIEVE")
			print("stack[top] = heap.retrieve(stack[top])")
		
		else:
			print("Syntax Error in line number", line)
		
		read = read + unread[0]
		unread = unread[1:]
		continue
	
	#For Flow Control:
	elif unread[0] == '3':
		#print(unread[0], ": IMP: FLOW_CONTROL")
		read = read + unread[0]
		unread = unread[1:]
		
		if unread[0:2] == '23':
			#print(unread[0:2], ": END: SUBROUTINE")
			print("return")
			read = read + unread[0:2]
			unread = unread[2:]
			
		elif unread[0:2] == '33':
			#print(unread[0:2], ": END: PROGRAM")
			read = read + unread[0:2]
			unread = unread[2:]
			
		else:
			mark = False
			if unread[0:2] == '11':
				#print(unread[0:2], ": FLOW_CONTROL: MARK LOCATION")
				mark = True
			
			elif unread[0:2] == '12':
				#print(unread[0:2], ": FLOW_CONTROL: CALL SUBROUTINE")
				print("call ", end="")
			
			elif unread[0:2] == '13':
				#print(unread[0:2], ": FLOW_CONTROL: UNCONDITIONAL JUMP")
				print("goto ", end="")
			
			elif unread[0:2] == '21':
				#print(unread[0:2], ": FLOW_CONTROL: JUMP ON 0")
				print("goto eqz ", end="")
			
			elif unread[0:2] == '22':
				#print(unread[0:2], ": FLOW_CONTROL: JUMP ON -VE")
				print("goto ltz ", end="")
			
			else:
				print("Syntax Error in line number", line)
			
			read = read + unread[0:2]
			unread = unread[2:]
			end = unread.find('3')
			#print(unread[0:end], ": PARAMETER: LABEL")
			
			if mark:
				print(spaceToDecimal(unread[0:end]) + ": ", end="")
			
			else:
				print(spaceToDecimal(unread[0:end]))
			
			read = unread[0:(end+1)]
			unread = unread[(end+1):]
		continue
	
	#For I/O:
	elif unread[0:2] == '23':
		#print(unread[0:2], ": IMP: I/O")
		read = read + unread[0:2]
		unread = unread[2:]
		
		if unread[0:2] == '11':
			#print(unread[0:2], ": OPERATION: O/P CHARACTER")
			print("t" + str(tmp) + " = stack[top]")
			print("print(t" + str(tmp) + ")")
			tmp = tmp + 1
		
		elif unread[0:2] == '12':
			#print(unread[0:2], ": OPERATION: O/P NUMBER")
			print("t" + str(tmp) + " = stack[top]")
			print("print(t" + str(tmp) + ")")
			tmp = tmp + 1
		
		elif unread[0:2] == '21':
			#print(unread[0:2], ": OPERATION: I/P CHARACTER")
			print("t" + str(tmp) + " = read()")
			print("heap.store(stack[top], t" + str(tmp) + ")")
			tmp = tmp + 1
		
		elif unread[0:2] == '22':
			#print(unread[0:2], ": OPERATION: I/P NUMBER")
			print("t" + str(tmp) + " = read()")
			print("heap.store(stack[top], t" + str(tmp) + ")")
			tmp = tmp + 1
		
		else:
			print("Syntax Error in line number", line)
		
		read = read + unread[0:2]
		unread = unread[2:]
		continue
