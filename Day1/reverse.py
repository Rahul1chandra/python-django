def reverse(arr):
	## keeping in mind that we should not use extra space
	##  we can use slicing 
	##  we can use reversed keyword
	##  we use multiple variable to store and print it to the reverse way
	##  ....................
	
	#return (arr[::-1])

	st_index  = 0
	end_index  = len(arr)-1

	while st_index <= end_index:
		arr[st_index], arr[end_index] = arr[end_index], arr[st_index]

		st_index +=	1
		end_index -= 1


	return  arr




print ("before reverse")
print ([1,2,3,4,5 ])


print ("after reverse")
print (reverse( [1,2,3,4,5 ] ) )


