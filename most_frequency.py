# each occurrence frequency using 
# collections.Counter()
from collections import Counter
  
# initializing string 
test_str = "MISSISSIPPI"
  
# using collections.Counter() to get 
# count of each element in string 
res = Counter(test_str)
  
# printing result 
print ("Count of all characters in MISSISSIPPI is :\n "
                                           +  str(res))
