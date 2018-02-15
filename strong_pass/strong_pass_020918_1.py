# -*- coding: utf-8 -*-

# ! /usr/local/Cellar/python3/3.6.1

# Strong Password Detection
# for training regex
# 
# https://regexr.com/3kj5r

import re

#####################################
# REGEX
#####################################

eightCharRegex = re.compile(r'''
		(
			.{8,} # 8 characters minimum or more
		)
	''', re.VERBOSE)

lowCaseRegex = re.compile(r'''
		(
			[a-z] # has lower case characters
		)
	''', re.VERBOSE)

upCaseRegex = re.compile(r'''
		(
			[A-Z] # has upper case characters
		)
	''', re.VERBOSE)

oneDigitPlusRegex = re.compile(r'''
		(
			[\d]+ # has 1 or more digits
		)
	''', re.VERBOSE)

#####################################
# END REGEX
#####################################

#####################################
# INPUT THE PASSWORD
#####################################

print("Password Strength Checker")

pass_input = input("> Please Enter The Password To Be Checked\n")

# print(pass_input) # testing

#####################################
# END INPUT THE PASSWORD
#####################################

#####################################
# ANALYZE THE PASSWORD
#####################################

def analyze_password():
	if len(eightCharRegex.findall(pass_input)) and len(lowCaseRegex.findall(pass_input)) and len(upCaseRegex.findall(pass_input)) and len(oneDigitPlusRegex.findall(pass_input)):
		print("The password entered meets the minimum criteria to be considered a strong password.")
	else:
		print("Password does not meet the minimum criteria to be considered a strong password.  This puts your personal security at risk.")

#####################################
# END ANALYZE THE PASSWORD
#####################################

#####################################
# EXECUTE
#####################################

analyze_password()

#####################################
# END EXECUTE
#####################################

# Documentation
# 
# ABSP: 279
# 
# Write a function that uses regular expressions to make sure the password string it is passed is strong. A strong password is defined as one that is at least eight characters long, contains both uppercase and lowercase characters, and has at least one digit. You may need to test the string against multiple regex patterns to validate its strength.