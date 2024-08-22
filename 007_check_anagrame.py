# function to check if two strings are anagram or not 
def check(str1, str2):
	
	# the sorted strings are checked 
	if(sorted(str1)== sorted(str2)):
		print(f'"{str1}" and "{str2}" are anagrams.') 
	else:
		print(f'"{str1}" and "{str2}" are not anagrams.')		 
		
# driver code 
str1 = input("Enter first string: ").replace(" ", "").lower()
str2 = input("Enter second string: ").replace(" ", "").lower()
check(str1, str2)
