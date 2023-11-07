'''
Context:
Can you find the needle in the haystack?

Problem:
Write a function findNeedle() that takes an array full of junk but containing one "needle"

After your function finds the needle it should return a message (as a string) that says:

"found the needle at position " plus the index it found the needle, so:

Pseudocode:
- def a function with a list as a argument: findNeedle(haystack).
- use the index() method to find the index with a especific content: haystack.index('needle').
- return a string formatting including the specified text and the index number.

Example(Input --> Output)
["hay", "junk", "hay",
"hay", "moreJunk", "needle",
"randomJunk"] --> "found the needle at position 5" 

'''

# def a function with a list as a argument: findNeedle(haystack).
def find_needle(haystack:str='') -> str:
# create a ver to storw the index() method to find the index with
# a especific content: haystack.index('needle').
    needle_ind= haystack.index('needle')
#return a string formatting including the specified text and the index number.
    return (f'found the needle at position {needle_ind}')

# Example:
haystack = ["paper", "pen", "book", "needle", "scissors"]
result = find_needle(haystack)
print(result)  # it'd must print "found the needle at position 3"