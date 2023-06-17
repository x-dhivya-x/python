import find_max		#find_max is a module.we import the module to use the max_value function
print(find_max.max_value([77,55,44,33,22]))

#this is another method of import the specific function from module
from find_max import max_value
print(max_value([33,66,44,11,44])) 
